from django.shortcuts import render, reverse, redirect
from .forms import UserSignUp, CustomerProfileForm
from django.views.generic import View


class CustomerProfileUpdate(View):
     
    def get(self, request):
        customer_profile_form = CustomerProfileForm(instance=request.user.customerprofile)
        user_signup_form = UserSignUp(instance=request.user)

        context = {
            'c_form': customer_profile_form,
            'u_form': user_signup_form,
        }

        return render(request, 'users/profile.html', context)
    
    def post(self, request):
        c_form = CustomerProfileForm(request.POST, instance=request.user.customerprofile)
        u_form = UserSignUp(request.POST, instance=request.user)
        c_form.instance.customer = request.user
        customer_id = request.user.id 
        

        if u_form.is_valid() and c_form.is_valid():
            u_form.save()
            c_form.save()
            return redirect(reverse('accounts:customer-account-page', args=(customer_id,)))

def signUp(request):
    if request.method == "POST":
        form = UserSignUp(request.POST)

        if form.is_valid():
            form.save()
            return redirect(reverse('users:home'))

        return render(request, 'users/signup.html', {'form': form})

    form = UserSignUp()
    return render(request, 'users/signup.html', {'form': form})


def index(request):
    return render(request, 'users/index.html')
