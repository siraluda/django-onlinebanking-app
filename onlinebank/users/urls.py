from django.urls import path
from .views import signUp, index, CustomerProfileUpdate
from django.contrib.auth.views import (
    LoginView, 
    LogoutView,)

app_name='users'

urlpatterns=[
    path('', index, name='home'),
    path('signup/', signUp, name='signup'),
    path('login/', LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name='users/index.html'), name='logout'),
    path('customer-profile/', CustomerProfileUpdate.as_view(), name='customer_profile'),
]
