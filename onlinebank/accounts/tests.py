from django.test import TestCase
from .models import CustomerAccount
from onlinebank.users.models import User, CustomerProfile

class CustomerAccountTest(TestCase):

    def _create_user_obj(self):
        email = 'test@email.com'
        password = 'testing123'
        return User.objects.create_user(email, password)

    def _create_customerProfile(self):
        phone_number = '+1-234-467-8910'
        date_of_birth = '01/13/1992'
        address = '23 Wall St'
        city = 'St. Johns'
        postalcode = 'A1B2C3'

        user = self._create_user_obj()

        return CustomerProfile(user, phone_number, date_of_birth, address, city, postalcode)

    def test_create_customer_account(self):
        customer_profile = self._create_customerProfile()
        customer_account = CustomerAccount(customer_profile, 'Savings')

        self.assertTrue(isinstance(customer_account, CustomerAccount))

