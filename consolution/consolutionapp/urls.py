from django.urls import path
from .views import BlogView
from . import views

urlpatterns = [
    path('', views.index),
    path('about', views.about),
    path('projects', views.projects),
    path('services', views.services),
    path('blog', BlogView.as_view(), name="blog-list"),
    path('contact', views.contact),
    path('single_blog/<str:pk>/', views.view_blog, name="single-blog")
]