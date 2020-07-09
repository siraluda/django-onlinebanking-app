from django.shortcuts import render
from .models import CustomerAccount, Transaction
from users.models import CustomerProfile
from django.views.generic import DetailView


class CustomerAccountView(DetailView):
    model = CustomerAccount
    template_name = 'accounts/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['transaction_list'] = Transaction.objects.all()

        return context
