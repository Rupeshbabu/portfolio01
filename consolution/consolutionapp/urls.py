from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('about', views.about),
    path('projects', views.projects),
    path('services', views.services),
    path('blog', views.blog),
    path('contact', views.contact),
    path('single_blog', views.view_blog)
]