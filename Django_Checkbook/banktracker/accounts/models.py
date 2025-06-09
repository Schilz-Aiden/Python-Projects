from django.db import models
from django.utils import timezone

# Create your models here.

class Account(models.Model):
    first_name = models.CharField(max_length=60)
    last_name = models.CharField(max_length=60)
    starting_balance = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    def current_balance(self):
        transactions = self.transactions.all()
        balance = self.starting_balance
        for t in transactions:
            if t.transaction_type == 'Deposit':
                balance += t.amount
            else:
                balance -= t.amount
        return balance

class Transaction(models.Model):
    TRANSACTION_TYPES = [
        ('deposit', 'Deposit'),
        ('withdrawal', 'Withdrawal'),
    ]

    account = models.ForeignKey(Account, on_delete=models.CASCADE, related_name='transactions')
    date = models.DateTimeField(default=timezone.now)
    transaction_type = models.CharField(max_length=10, choices=TRANSACTION_TYPES)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()

    def __str__(self):
        return f"{self.transaction_type} of ${self.amount} on {self.date}"
