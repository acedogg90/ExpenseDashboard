from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

# Create your views here.
def home(request):
    # check to see if user is logging in
    if request.method == 'POST':
        # get the form data
        username = request.POST['username']
        password = request.POST.get('password')
        # authenticate the user
        user = authenticate(request, username=username, password=password)
        if user is not None:
            # login the user
            login(request, user)
            messages.success(request, 'You have successfully logged in.')
            return render(request, 'home.html', {})
        else:
            messages.error(request, 'Invalid username or password.')
            return render(request, 'home.html', {})
    else:
        return render(request, 'home.html', {})

def logout_user(request):
    logout(request)
    messages.success(request, 'You have successfully logged out.')
    return render(request, 'home.html', {})

def dashboard(request):
    return render(request, 'dashboard.html', {})
