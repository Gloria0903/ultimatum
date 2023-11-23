"""
URL configuration for ultimatum project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from . import views
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('register/', views.register, name='register'),
    path('signin/', views.signin, name='signin'),
    path('properties/', views.properties, name='properties'),
    path('properties-detail/', views.properties_detail, name='properties_detail'),
    path('gallery/', views.gallery, name='gallery'),
    path('blog-archive/', views.blog_archive, name='blog_archive'),
    path('blog-single/', views.blog_single, name='blog_single'),
    path('contact/', views.contact, name='contact'),

    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/signin/', views.MyLoginView.as_view(), name='signin'),
    path('accounts/register/', views.MyRegistrationView.as_view(), name='register'),

    path('properties/', views.properties, name='properties'),
    path('properties/new/', views.properties_new, name='properties_new'),
    path('properties/<int:property_id>/', views.properties_detail, name='properties_detail'),
    path('properties/<int:property_id>/edit/', views.properties_edit, name='properties_edit'),
    path('properties/<int:property_id>/delete/', views.properties_delete, name='properties_delete'),

]
