from django.shortcuts import render
from .models import Blog, Project, Service


# Create your views here.

def index(request):
    context = {}
    return render(request, 'index.html', {})


def about(request):
    context = {}
    return render(request, 'about.html', {})


def projects(request):
    pro = Project.objects.all()
    return render(request, 'projects.html', {'pro': pro})


def services(request):
    ser = Service.objects.all()
    return render(request, 'services.html', {'ser': ser})


def blog(request):
    blg = Blog.objects.all()
    return render(request, 'blog.html', {'blg': blg})


def view_blog(request, id):
    context = {}
    return render(request, 'single_blog.html', {'id': id})


def contact(request):
    context = {}
    return render(request, 'contact.html', {})


def meta(request):
    return render(request, '../../base.html', {'tag': "profile"})
