"""NewsProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
from NewsApplication import views
from rest_framework.routers import DefaultRouter
from NewsApplication.views import USERViewset
from django.urls import include,path

router=DefaultRouter()
router.register('queryset', USERViewset, basename='queryset')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name = "index"),
    path('Home/', views.home, name ="home"),
    path('User_info/', include (router.urls)),
    path('Sign-up/',views.register,name ="sign-up"),
    path('aboutUs/',views.aboutUs,name="aboutUs"),
    path('service/',views.services,name="services"),
]
