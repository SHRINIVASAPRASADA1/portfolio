from django.contrib.sitemaps import Sitemap
from .models import *
from django.contrib import sitemaps
from django.urls import reverse

from django.contrib.sitemaps import Sitemap
from .models import *


class BlogSitemap(Sitemap):
    changefreq = "never"
    priority = 0.9

    def items(self):
        return Blogs.objects.all()

    def lastmod(self, obj):
        return obj.date


class GallerySiteMap(Sitemap):
    changefreq = "never"
    priority = 0.9

    def items(self):
        return Gallery.objects.all()

    def lastmod(self, obj):
        return obj.date


class ProjectSitemap(Sitemap):
    changefreq = "never"
    priority = 0.9

    def items(self):
        return Project.objects.all()

    def lastmod(self, obj):
        return obj.date


class NotesUploadSiteMap(Sitemap):
    changefreq = "never"
    priority = 0.9

    def items(self):
        return NotesUpload.objects.all()

    def lastmod(self, obj):
        return obj.date


class SocialLinkSiteMap(Sitemap):
    changefreq = "never"
    priority = 0.9

    def items(self):
        return SocialLink.objects.all()

    def lastmod(self, obj):
        return obj.date
