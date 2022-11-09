from django.contrib import admin
from .models import *


# Register your models here.
@admin.register(projects)
class ProjectsComplited(admin.ModelAdmin):
    list_display = ('title', 'image', 'date', 'des', 'start', 'end', 'lang', 'Platform')


@admin.register(blog)
class MyBlogs(admin.ModelAdmin):
    list_display = ('under', 'title', 'des', 'img', 'date', 'source', 'source_link')


@admin.register(add_content_to_blog)
class ContentsForBlog(admin.ModelAdmin):
    list_display = ('id','blog_number', 'img', 'des')


@admin.register(blog_catogory)
class BlogsCatogory(admin.ModelAdmin):
    list_display = ('blog_catogorys_name', 'date', 'des')


@admin.register(gallery)
class MyGallery(admin.ModelAdmin):
    list_display = ('img', 'title', 'des', 'date')


@admin.register(ListFoContent)
class ListOfContents(admin.ModelAdmin):
    list_display = ('blogPostNumber', 'listText')


@admin.register(ListOfImage)
class ListOfImages(admin.ModelAdmin):
    list_display = ('blogPostNumber', 'ImageSelect', 'imageUrl')
