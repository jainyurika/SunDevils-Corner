from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import HttpResponseRedirect
from .forms import SignUpForm
from .decorators import unauthenticated_user
from post.models import Post
from.models import Account

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

@login_required(login_url='login')
def profile(request):
    user = request.user
    posts = Post.objects.filter(author_id=user.id)
    post_count = posts.count()

    context = {
        'user':user,
        'posts': posts,
        'post_count':post_count
        }
    return render(request, 'accounts/profile.html', context)

@login_required(login_url='login')
# update view for details
def update_view(request, pk):
    # dictionary for initial data with 
    # field names as keys
    # fetch the object related to passed id
    obj = get_object_or_404(Account, pk = request.user.id)
    # pass the object as instance in form
    form = SignUpForm(request.POST or None, instance = obj)
    # save the data from the form and
    # redirect to detail_view
    if form.is_valid():
        form.save()
        return HttpResponseRedirect("/"+id)
    # add form dictionary to context
    
    context ={
        'form':form
    }
    return render(request, "accounts/edit_profile.html", context)


def logout_view(request):
    logout(request)
    return redirect('login')