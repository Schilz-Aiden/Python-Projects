from django import forms
from .models import Account, Transaction

class AccountForm(forms.ModelForm):
    class Meta:
        model = Account
        fields = ['first_name', 'last_name', 'starting_balance']
        labels = {
            'first_name': 'First Name',
            'last_name': 'Last Name',
            'initial_balance': 'Initial Balance',
        }

class TransactionForm(forms.ModelForm):
    class Meta:
        model = Transaction
        fields = ['account', 'description', 'transaction_type', 'amount']