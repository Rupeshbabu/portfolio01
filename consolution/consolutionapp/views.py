from django.shortcuts import render
from django.core.paginator import Paginator
from .models import Blog, Project, Service


# Create your views here.

def index(request):
    pro = Project.objects.order_by("-upload_at")[:4]
    ser = Service.objects.order_by("-upload_at")[:3]
    blg = Blog.objects.order_by("-upload_at")[:3]

    return render(request, 'index.html', {'pro': pro, 'ser': ser, 'blg': blg})


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
    paginator = Paginator(blg, 3)
    page = request.GET.get('page')
    blogs = paginator.get_page(page)
    return render(request, 'blog.html', {'blogs': blogs})


def view_blog(request, id):
    vblg = Blog.objects.filter(id=id)
    return render(request, 'single_blog.html', {'vblg': vblg})


def contact(request):
    context = {}
    return render(request, 'contact.html', {})


def meta(request):
    return render(request, '../../base.html', {'tag': "profile"})
