from django.contrib import admin
from .models import *


# Register your models here.
@admin.register(Project)
class ProjectsComplited(admin.ModelAdmin):
    list_display = ('title', 'image', 'date', 'des', 'start', 'end', 'lang', 'Platform')


@admin.register(Blogs)
class MyBlogs(admin.ModelAdmin):
    list_display = ('under', 'title', 'des', 'img', 'date', 'source', 'source_link')


@admin.register(InsertContent)
class ContentsForBlog(admin.ModelAdmin):
    list_display = ('id', 'blog_number', 'img')


@admin.register(BlogCatogory)
class BlogsCatogory(admin.ModelAdmin):
    list_display = ('blog_catogorys_name', 'date')


@admin.register(Gallery)
class MyGallery(admin.ModelAdmin):
    list_display = ('img', 'title', 'des', 'date')


@admin.register(VisitorIpAddress)
class UserIpAddress(admin.ModelAdmin):
    list_display = ('ip', 'device', 'date')


@admin.register(LinksAddOn)
class Links(admin.ModelAdmin):
    list_display = ('link', 'title', 'thumb', 'date')


@admin.register(NotesUpload)
class Notes(admin.ModelAdmin):
    list_display = ('title', 'file', 'date')


@admin.register(AddNotes)
class AddNotes(admin.ModelAdmin):
    list_display = ('title', 'fkey', 'date')


@admin.register(SocialLink)
class SocialMedia(admin.ModelAdmin):
    list_display = ('link', 'logo', 'date')


@admin.register(skills)
class SkillsSet(admin.ModelAdmin):
    list_display = ('title', 'link', 'expertise')
