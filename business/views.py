from django.shortcuts import render, redirect
from django.db.models import F
from .forms import BusinessForm
from .models import Business, BusinessCat
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url='login')
def businessView(request):
    return render(request, 'business/business.html')

@login_required(login_url='login')
def Apartments(request):

    businesses = Business.objects.filter(category=1)
    cat = BusinessCat.objects.filter(id=1)[0]

    context = {
        'businesses': businesses,
        'cat': cat
    }
    return render(request, 'business/businesses.html', context)

@login_required(login_url='login')
def GroceryStores(request):

    businesses = Business.objects.filter(category=4)
    cat = BusinessCat.objects.filter(id=4)[0]

    context = {
        'businesses': businesses,
        'cat': cat
    }
    return render(request, 'business/businesses.html', context)

@login_required(login_url='login')
def HaircutShops(request):

    businesses = Business.objects.filter(category=2)
    cat = BusinessCat.objects.filter(id=2)[0]

    context = {
        'businesses': businesses,
        'cat': cat
    }
    return render(request, 'business/businesses.html', context)

@login_required(login_url='login')
def Restaurants(request):

    businesses = Business.objects.filter(category=3)
    cat = BusinessCat.objects.filter(id=3)[0]

    context = {
        'businesses': businesses,
        'cat': cat
    }
    return render(request, 'business/businesses.html', context)

@login_required(login_url='login')
def createBusiness(request):

    form = BusinessForm()
    if request.method == 'POST':
        form = BusinessForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('business')
            

    context = {'form': form}
    return render(request, 'business/createBusiness.html', context)

@login_required(login_url='login')
def updateBusiness(request, pk):

    business = Business.objects.get(id=pk)
    form = BusinessForm(instance=business)

    context = {'form': form}
    return render(request, 'business/createBusiness.html', context)

@login_required(login_url='login')
def viewBusiness(request, pk):
    business = Business.objects.get(id=pk)
    cat_name = business.category
    if request.method == 'POST':
        a = Business.objects.filter(id=pk).update(upvotecount=F('upvotecount') + 1)

    context = {
        'business': business,
        'cat_name':cat_name
        }
    return render(request, 'business/viewbusiness.html', context)

@login_required(login_url='login')
def top5apartment(request):

    businesses = Business.objects.filter(category=1).order_by('-upvotecount')[:5]
    business_cat =  BusinessCat.objects.filter(id=1)[0]
    
    context = {
        'businesses': businesses,
        'business_cat': business_cat
    }
    return render(request, 'business/top5.html', context)

@login_required(login_url='login')
def top5haircut(request):

    businesses = Business.objects.filter(category=2).order_by('-upvotecount')[:5]
    business_cat =  BusinessCat.objects.filter(id=2)[0]
    
    context = {
        'businesses': businesses,
        'business_cat': business_cat
    }
    return render(request, 'business/top5.html', context)

@login_required(login_url='login')
def top5restaurants(request):

    businesses = Business.objects.filter(category=3).order_by('-upvotecount')[:5]
    business_cat =  BusinessCat.objects.filter(id=3)[0]
    
    context = {
        'businesses': businesses,
        'business_cat': business_cat
    }
    return render(request, 'business/top5.html', context)

@login_required(login_url='login')
def top5grocerystores(request):

    businesses = Business.objects.filter(category=4).order_by('-upvotecount')[:5]
    business_cat =  BusinessCat.objects.filter(id=4)[0]
    
    context = {
        'businesses': businesses,
        'business_cat': business_cat
    }
    return render(request, 'business/top5.html', context)