from django.contrib.sitemaps import Sitemap
from .models import *
from django.contrib import sitemaps
from django.urls import reverse

from django.contrib.sitemaps import Sitemap
from .models import *


class BlogSitemap(Sitemap):
    changefreq = "never"
    priority = 0.5

    def items(self):
        return blog.objects.all()

    def lastmod(self, obj):
        return obj.date
