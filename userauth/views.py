from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout
from django.contrib import messages


def register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Account registered successfully!!')
            return redirect('userauth:login')


    form = UserCreationForm
    context={
        'form':form
    }
    return render(request, 'userauth/register.html', context)


def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request,user)
            # message
            return redirect('info:home')
        else:
            messages.error(request, 'Invalid username or password')


    form = AuthenticationForm
    context = {
        'form':form
    }
    return render(request, 'userauth/login.html', context)


def logout_view(request):
    logout(request)
    messages.success(request, 'Logged out successfully!!')
    return redirect('userauth:login')