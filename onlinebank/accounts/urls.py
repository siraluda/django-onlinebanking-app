from django.urls import path
from .views import CustomerAccountView

app_name = "accounts"

urlpatterns = [
    path('customer-account/<int:pk>', CustomerAccountView.as_view(), name='customer-account-page'),
]