from django import forms
from .models import CustomerAccount, Transaction

ACCOUNT_TYPES = [
    ('SAVINGS', 'Savings'),
    ('CHECKING', 'Checking'),
]

TRANSACTION_TYPES = [
    ('WITHDRAWAL','Withdrawal'),
    ('DEPOSIT','Deposit'),
]

class CreateAccountForm(forms.Form):
    account_type = forms.ChoiceField(choices=ACCOUNT_TYPES)

class CreateTransactionForm(forms.Form):
    account_type = forms.ChoiceField(choices=ACCOUNT_TYPES)
    transaction_type = forms.ChoiceField(choices=TRANSACTION_TYPES)
    amount = forms.DecimalField(max_digits=10, decimal_places=2)
