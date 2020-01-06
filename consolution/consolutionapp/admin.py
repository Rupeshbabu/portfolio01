from django.contrib import admin
from .models import Blog, Project,Service


# Register your models here.
class BlogAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'content', 'image', 'status', 'upload_at')


class ProjectAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'technologies', 'website', 'image', 'status', 'upload_at')


class ServiceAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'fav_icon', 'content', 'status', 'upload_at')


admin.site.register(Blog, BlogAdmin)
admin.site.register(Project, ProjectAdmin)
admin.site.register(Service, ServiceAdmin)
