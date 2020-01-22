from django.conf import settings
from django.shortcuts import render
from django.core.paginator import Paginator
from .models import Blog, Project, Service
from django.views.generic import ListView, DetailView
from django.http import HttpResponse
from .forms import ContactForm
from django.core.mail import send_mail


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


class BlogView(ListView):
    model = Blog
    template_name = 'blog.html'
    context_object_name = "blogs"


# def BlogView(List):
#     blg = Blog.objects.all()
#     paginator = Paginator(blg, 3)
#     page = request.GET.get('page')
#     blogs = paginator.get_page(page)
#     return render(request, 'blog.html', {'blogs': blogs})


def view_blog(request, pk):
    vblg = Blog.objects.get(id=pk)
    return render(request, 'single_blog.html', {'vblg': vblg})


def contact(request):
    context = {}
    return render(request, 'contact.html', {})


def meta(request):
    return render(request, '../templates/base.html', {'tag': "profile"})


def contact_us(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        subject = request.POST['subject']
        message = request.POST['message']
        send_mail(ContactForm, message, email, name, subject, settings.EMAIL_HOST_USER, 'nrupesh08@gmail.com')
        return render(request, 'contact.html')

    # if request.method == 'POST':
    #     form = ContactForm(request.POST)
    #     if form.is_valid():
    #         return HttpResponse('Thanks for contacting us!')
    # else:
    #     form = ContactForm()
    # return render(request, 'contact.html', {'form': form})
    #
    # sender_name = form.cleaned_data['name']
    # sender_email = form.cleaned_data['nrupesh08@gmail.com']
    #
    # message = "{0} has sent you a new message:\n\n{1}".format(sender_name, form.cleaned_data['message'])
    # send_mail('New Enquiry', message, sender_email, ['nrupesh08@gmail.com'])
