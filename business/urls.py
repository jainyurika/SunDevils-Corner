"""sdCorner URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from .views import businessView, createBusiness, updateBusiness, Apartments, viewBusiness, top5apartment, GroceryStores, Restaurants, HaircutShops, top5grocerystores, top5haircut, top5restaurants

urlpatterns = [
    # path('', home, name='home'),
    path('business/', businessView, name='business'),
    path('apartments/', Apartments, name='apartment'),
    path('apartments/top-5/', top5apartment, name='top5apartment'),
    path('grocerystores/', GroceryStores, name='grocerystores'),
    path('grocerystores/top-5/', top5grocerystores, name='top5grocerystores'),
    path('haircutshops/', HaircutShops, name='haircutshops'),
    path('haircutshops/top-5/', top5haircut, name='top5haircut'),
    path('restaurants/', Restaurants, name='restaurants'),
    path('restaurants/top-5/', top5restaurants, name='top5restaurants'),
    path('business/<str:pk>/', viewBusiness, name='view_business'),
    path('createBusiness/', createBusiness, name='create_business'),
    path('updateBusiness/<str:pk>/', updateBusiness, name='update_business'),
    # path('login/', loginPage, name='login'),
    # path('thanks/', thanks, name='thanks'),
    
]
