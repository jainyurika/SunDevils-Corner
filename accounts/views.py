from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import HttpResponseRedirect
from .forms import SignUpForm
from .decorators import unauthenticated_user

@unauthenticated_user
def SignUpView(request):
    form = SignUpForm()
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            # email = form.cleaned_data.get('email')
            # print(email)
            fname = form.cleaned_data.get('fname')
            lname = form.cleaned_data.get('lname')
            user = fname + " " + lname
            messages.info(request, user)
            return redirect('thanks')
            # return redirect('login')
    
    context = {'form': form}
    return render(request, 'accounts/signup.html', context)

@unauthenticated_user
def thanks(request):
    return render(request, 'accounts/thanks.html')

@unauthenticated_user
def loginPage(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        if request.method == 'POST':
            email = request.POST.get('username')
            password = request.POST.get('password')
            print("Email: " + email)
            print("Password: " + password)
            
            user = authenticate(request, email=email, password=password)
            
            if user is not None:
                login(request, user)
                print("Goign Home!")
                return redirect('home')
        context = {}
        return render(request, 'accounts/login.html', context)

@login_required(login_url='login')
def home(request):
    return render(request, 'accounts/index.html')


def logout_view(request):
    logout(request)
    return redirect('login')