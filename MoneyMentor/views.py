from django.shortcuts import render
from django.http import JsonResponse
from datetime import datetime
from decimal import Decimal, InvalidOperation
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from django.views.decorators.http import require_GET, require_POST
from MoneyMentor.models import Transaction

from MoneyMentor.utils.analytics import (
    get_monthly_summary,
    get_category_breakdown,
    get_daily_spending,
    get_daily_transactions,
    get_daily_totals,
    generate_insights
)


# -------------------------------
# Static Pages
# -------------------------------
def home(request):
    return render(request, 'home.html')


def about(request):
    return render(request, 'about.html')


# -------------------------------
# Analytics Page (UI only)
# -------------------------------
@login_required
def analytics_page(request):
    return render(request, "analytics.html")


# -------------------------------
# Analytics API (DATA ENGINE)
# -------------------------------
@login_required
@require_POST
def add_transaction(request):
    date_value = request.POST.get("date")
    transaction_type = request.POST.get("type")
    amount_value = request.POST.get("amount")
    category = (request.POST.get("category") or "").strip()

    if transaction_type not in dict(Transaction.TRANSACTION_TYPE):
        return JsonResponse({"status": "error", "message": "Invalid transaction type."}, status=400)

    if not date_value or not amount_value or not category:
        return JsonResponse({"status": "error", "message": "Date, amount, and category are required."}, status=400)

    try:
        parsed_date = datetime.strptime(date_value, "%Y-%m-%d").date()
        amount = Decimal(amount_value)
    except (ValueError, InvalidOperation):
        return JsonResponse({"status": "error", "message": "Invalid date or amount."}, status=400)

    if amount <= 0:
        return JsonResponse({"status": "error", "message": "Amount must be greater than zero."}, status=400)

    Transaction.objects.create(
        user=request.user,
        date=parsed_date,
        type=transaction_type,
        amount=amount,
        category=category,
        subcategory=(request.POST.get("subcategory") or "").strip(),
        note=(request.POST.get("note") or "").strip(),
    )
    return JsonResponse({"status": "success"})


@login_required
@require_GET
def analytics_api(request):
    user = request.user

    now = timezone.localdate()
    try:
        month = int(request.GET.get("month", now.month))
        year = int(request.GET.get("year", now.year))
    except ValueError:
        return JsonResponse({"status": "error", "message": "Month and year must be numbers."}, status=400)

    if month < 1 or month > 12:
        return JsonResponse({"status": "error", "message": "Month must be between 1 and 12."}, status=400)

    # Core Data
    summary = get_monthly_summary(user, month, year)
    categories = get_category_breakdown(user, month, year)
    trend = get_daily_spending(user, month, year)

    # UI Data
    daily_data = get_daily_transactions(user, month, year)
    daily_totals = get_daily_totals(daily_data)

    # Insights
    insights = generate_insights(summary)

    return JsonResponse({
        "summary": summary,
        "categories": categories,
        "trend": trend,
        "daily_data": daily_data,
        "daily_totals": daily_totals,
        "insights": insights
    })
