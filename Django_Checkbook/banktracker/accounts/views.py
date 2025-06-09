from django.shortcuts import render, get_object_or_404, redirect
from .models import Account,Transaction
from .forms import AccountForm, TransactionForm

# Create your views here.
def home(request):
    accounts = Account.objects.all()

    # If a form was submitted (via GET), redirect to that account's detail page
    account_id = request.GET.get('account_id')
    if account_id:
        return redirect('view_account', account_id=account_id)

    return render(request, 'home.html', {'accounts': accounts})

def create_account(request):
    if request.method == 'POST':
        form = AccountForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = AccountForm()
    return render(request, 'CreateNewAccount.html', {'form': form})


def view_account(request, account_id):
    account = get_object_or_404(Account, pk=account_id)
    transactions = Transaction.objects.filter(account=account).order_by('date')

    # Calculate running balance
    balance = account.initial_deposit
    transaction_data = []
    for t in transactions:
        if t.transaction_type == 'Deposit':
            balance += t.amount
        elif t.transaction_type == 'Withdrawal':
            balance -= t.amount
        transaction_data.append({
            'date': t.date,
            'type': t.transaction_type,
            'description': t.description,
            'amount': t.amount,
            'balance': balance,
        })

    return render(request, 'balance_sheet.html', {
        'account': account,
        'transactions': transaction_data,
        'current_balance': balance
    })

def add_transaction(request, account_id):
    account = get_object_or_404(Account, pk=account_id)

    if request.method == 'POST':
        form = TransactionForm(request.POST)
        if form.is_valid():
            transaction = form.save(commit=False)
            transaction.account = account
            transaction.save()
            return redirect('view_account', account_id=account.id)
    else:
        form = TransactionForm(initial={'account': account})

    return render(request, 'add_transaction.html', {'form': form, 'account': account})