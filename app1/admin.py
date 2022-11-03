from django.contrib import admin
from .models import *


# Register your models here.
@admin.register(projects)
class RoomsAvailable(admin.ModelAdmin):
    list_display = ('title', 'image', 'date', 'des', 'start', 'end', 'lang', 'Platform')


@admin.register(blog)
class RoomsAvailable(admin.ModelAdmin):
    list_display = ('under', 'title', 'des', 'img', 'date', 'source', 'source_link')


@admin.register(add_content_to_blog)
class RoomsAvailable(admin.ModelAdmin):
    list_display = ('blog_number', 'img', 'des')


@admin.register(blog_catogory)
class RoomsAvailable(admin.ModelAdmin):
    list_display = ('blog_catogorys_name', 'date', 'des')


@admin.register(gallery)
class RoomsAvailable(admin.ModelAdmin):
    list_display = ('img', 'title', 'des', 'date')
