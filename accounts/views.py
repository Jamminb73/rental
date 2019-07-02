from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User, auth

def login(request):
    if request.method == 'POST':
        username = request.Post['username']
        password = request.Post['password']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            messages.success(request, 'You are now logged in!')
            return redirect('home')
        else:
            messages.error(request, 'Invalid credentials')
            return redirect('login')
    else:
        return render(request, "accounts/login.html")

def register(request):
    if request.method == 'POST':
        # Get form values
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']

        # Check if passwords match

        if password == password2:
            #Check username
            if User.objects.filter(username=username).exists():
                messages.error(request, 'That username is taken')
                return redirect('register')
            else:
                # Looks good
                user = User.objects.create_user(username= username, password=password,
                email=email)
                # Login after register
                # auth.login(request, user)
                # messages.success(request, 'You are now logged in')
                # return redirect('index') (all previous comments are an alternate method)
                user.save()
                messages.success(request, 'You are now registered and can log in.')
                return redirect('login')
        else:
            messages.error(request, 'Passwords do not match')
            return redirect('register')

    else:
        return render(request, 'accounts/register.html')

def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        message.success(request, "You are now logged out")
        return redirect("home")
