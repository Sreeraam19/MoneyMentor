from django.db.models import Sum
from collections import defaultdict
from MoneyMentor.models import Transaction
import random


# -------------------------------
# 1. Monthly Summary
# -------------------------------
def get_monthly_summary(user, month, year):
    transactions = Transaction.objects.filter(
        user=user,
        date__month=month,
        date__year=year
    )

    income = transactions.filter(type='INCOME').aggregate(Sum('amount'))['amount__sum'] or 0
    expense = transactions.filter(type='EXPENSE').aggregate(Sum('amount'))['amount__sum'] or 0

    return {
        "income": float(income),
        "expense": float(expense),
        "savings": float(income - expense)
    }


# -------------------------------
# 2. Category Breakdown
# -------------------------------
def get_category_breakdown(user, month, year):
    expenses = Transaction.objects.filter(
        user=user,
        type='EXPENSE',
        date__month=month,
        date__year=year
    )

    data = expenses.values('category').annotate(total=Sum('amount')).order_by('-total')

    return list(data)


# -------------------------------
# 3. Daily Spending Trend (for graphs)
# -------------------------------
def get_daily_spending(user, month, year):
    expenses = Transaction.objects.filter(
        user=user,
        type='EXPENSE',
        date__month=month,
        date__year=year
    )

    data = expenses.values('date').annotate(total=Sum('amount')).order_by('date')

    return list(data)


# -------------------------------
# 4. Daily Transactions (FOR UI)
# -------------------------------
def get_daily_transactions(user, month, year):
    transactions = Transaction.objects.filter(
        user=user,
        date__month=month,
        date__year=year
    ).order_by('-date', '-created_at')

    grouped = defaultdict(list)

    for txn in transactions:
        grouped[str(txn.date)].append({
            "id": txn.id,
            "type": txn.type,
            "category": txn.category,
            "subcategory": txn.subcategory,
            "amount": float(txn.amount),
            "note": txn.note or ""
        })

    return dict(grouped)


# -------------------------------
# 5. Daily Totals (Expense only)
# -------------------------------
def get_daily_totals(daily_data):
    totals = {}

    for date, txns in daily_data.items():
        total = sum(t["amount"] for t in txns if t["type"] == "EXPENSE")
        totals[date] = total

    return totals


# -------------------------------
# 6. Smart Insights
# -------------------------------
def generate_insights(summary):
    insights = []

    if summary["expense"] > summary["income"]:
        insights.append(random.choice([
            "Spending exceeded income this month.",
            "Expenses are higher than earnings.",
            "You're in a negative balance zone."
        ]))

    if summary["savings"] > 0:
        insights.append(random.choice([
            "Good job maintaining savings.",
            "You're financially stable this month.",
            "Savings trend is positive."
        ]))

    if summary["expense"] > summary["income"] * 0.7:
        insights.append(random.choice([
            "Expenses are approaching your income limit.",
            "Spending is getting close to earnings.",
            "You're nearing a high expense ratio."
        ]))

    if not insights:
        insights.append("No major financial issues detected this month.")

    return insights