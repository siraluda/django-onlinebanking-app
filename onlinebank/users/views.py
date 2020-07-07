from django.shortcuts import render, reverse, redirect
from .forms import UserSignUp


def signUp(request):
    if request.method == "POST":
        form = UserSignUp(request.POST)

        if form.is_valid():
            form.save()
            return redirect(reverse('users:home'))

        return render(reverse('users:signup'))

    form = UserSignUp()
    return render(request, 'users/signup.html', {'form': form})


def index(request):
    return render(request, 'users/index.html')
