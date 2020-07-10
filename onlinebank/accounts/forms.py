from django import forms
from .models import CustomerAccount, Transaction

class CreateAccountForm(forms.ModelForm):
    
    class Meta:
        model = CustomerAccount
        fields = ['account_type', 'balance']

class CreateTransactionForm(forms.ModelForm):

    class Meta:
        model = Transaction
        fields = ['account', 'transaction_type', 'amount']