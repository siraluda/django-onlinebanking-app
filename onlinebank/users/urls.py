from django.urls import path
from .views import signUp, index, logout_view, CustomerProfileUpdate, CustomLoginView

app_name='users'

urlpatterns=[
    path('', index, name='home'),
    path('signup/', signUp, name='signup'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', logout_view, name='logout'),
    path('customer-profile/', CustomerProfileUpdate.as_view(), name='customer_profile'),
]
