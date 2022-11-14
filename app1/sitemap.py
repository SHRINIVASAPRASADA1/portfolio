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
        return blog.objects.all()

    def lastmod(self, obj):
        return obj.date

class GallerySiteMap(Sitemap):
    changefreq = "never"
    priority = 0.9

    def items(self):
        return gallery.objects.all()

    def lastmod(self, obj):
        return obj.date

class HtmlSiteMap(Sitemap):
    changefreq = "never"
    priority = 0.9

    def items(self):
        return HtmlCode.objects.all()

    def lastmod(self, obj):
        return obj.date

class CssLinkSiteMap(Sitemap):
    changefreq = "never"
    priority = 0.9

    def items(self):
        return CssFiles.objects.all()

    def lastmod(self, obj):
        return obj.date