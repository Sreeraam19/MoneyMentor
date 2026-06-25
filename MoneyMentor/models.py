from django.conf import settings
from django.db import models


class Transaction(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    TRANSACTION_TYPE = [
        ('INCOME', 'Income'),
        ('EXPENSE', 'Expense'),
        ('SAVING', 'Saving'),  # Optional but useful later
    ]

    type = models.CharField(max_length=10, choices=TRANSACTION_TYPE)

    category = models.CharField(max_length=50)
    subcategory = models.CharField(max_length=50, blank=True, null=True)

    amount = models.DecimalField(max_digits=10, decimal_places=2)

    note = models.TextField(blank=True, null=True)

    date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user} | {self.type} | Rs. {self.amount} | {self.date}"
