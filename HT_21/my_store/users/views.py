from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from .forms import UserLoginForm


def custom_login(request):
    if request.method == 'POST':
        form = UserLoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, 'You have logged in!')
                return redirect('ui:index')
            else:
                messages.error(request, 'Invalid login credentials.')
        else:
            messages.error(request, 'Invalid form submission. Please check your inputs.')
    else:
        form = UserLoginForm()

    return render(request, 'users/login.html', context={'form': form})


@login_required
def custom_logout(request):
    logout(request)
    messages.success(request, 'You have logged out!')
    return redirect('users:custom_login')



