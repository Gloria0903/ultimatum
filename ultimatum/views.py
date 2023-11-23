from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.views import LoginView
from django.contrib.auth.forms import UserCreationForm
from django.views import generic
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from .models import Property
from .forms import PropertyForm


class MyRegistrationView(generic.CreateView):
    form_class = UserCreationForm
    success_url = '/accounts/login/'
    template_name = 'register.html'


class MyLoginView(LoginView):
    template_name = 'signin.html'


def index(request):
    return render(request, 'index.html')


def register(request):
    return render(request, 'register.html')


def signin(request):
    return render(request, 'signin.html')


# def properties(request):
#     return render(request, 'properties.html')


# def properties_detail(request):
#     return render(request, 'properties-detail.html')


def gallery(request):
    return render(request, 'gallery.html')


def blog_archive(request):
    return render(request, 'blog-archive.html')


def blog_single(request):
    return render(request, 'blog-single.html')


def contact(request):
    return render(request, 'contact.html')


# CRUD LOGIC
def index(request):
    return render(request, 'index.html')


def properties(request):
    properties = Property.objects.all()
    return render(request, 'properties.html', {'properties': properties})


def properties_detail(request, property_id):
    property = get_object_or_404(Property, pk=property_id)
    return render(request, 'properties-detail.html', {'property': property})


def properties_new(request):
    if request.method == "POST":
        form = PropertyForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/properties/")
    else:
        form = PropertyForm()
    return render(request, 'properties-new.html', {'form': form})


def properties_edit(request, property_id):
    property = get_object_or_404(Property, pk=property_id)
    if request.method == "POST":
        form = PropertyForm(request.POST, instance=property)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/properties/")
    else:
        form = PropertyForm(instance=property)
    return render(request, 'properties-edit.html', {'form': form})


def properties_delete(request, property_id):
    property = get_object_or_404(Property, pk=property_id)
    if request.method == "POST":
        property.delete()
        return HttpResponseRedirect("/properties/")
    else:
        return render(request, 'properties-delete.html', {'property': property})


# def gallery(request):
#     return render(request, 'gallery.html')


# def contact(request):
#     return render(request, 'contact.html')


# Register Login
def register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        myuser = User.objects.create_user(username, password)
    myuser.save()
    return render(request, 'register.html')


def signin(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        myuser = authenticate(username=username, password=password)

        if myuser is not None:
            signin(request, myuser)
            return redirect('/')
        else:
            return redirect('/register')
    return render(request, 'signin.html')


def signout(request):
    signout(request)
    return redirect('/register')
