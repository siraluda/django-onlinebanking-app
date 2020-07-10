from django.shortcuts import render
from .models import CustomerAccount, Transaction
from users.models import CustomerProfile
from django.views.generic import DetailView, View
from .forms import CreateAccountForm, CreateTransactionForm


class CustomerAccountView(DetailView):
    model = CustomerProfile
    template_name = 'accounts/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        customer_info = CustomerProfile.objects.get(id=self.kwargs['pk'])
        customer_accounts = CustomerAccount.objects.filter(
            customer__customer__id=self.kwargs['pk'])
        customer_transactions = Transaction.objects.filter(
            customer__customer__id=self.kwargs['pk']).order_by('-transaction_date')
        total_balance = 0

        # add balances from each account
        for account_balance in customer_accounts:
            total_balance += account_balance.balance

        context = {
            'customer_accounts': customer_accounts,
            'customer_info': customer_info,
            'total_balance': total_balance,
            'customer_transactions': customer_transactions
        }

        return context

class MakeTransaction(View):

    def get(self, request):
        create_transaction = CreateTransactionForm(instance=request.user)

        return render(request, 'accounts/transaction_form.html', {'t_form': create_transaction})

    def post(self, request):
        t_form = CreateTransactionForm(request.POST, instance=request.user)

        def form_valid(self, t_form):
            t_form.instance.customer = self.request.user
            return super().form_valid(t_form)
        
