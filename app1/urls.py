from . import views
from django.contrib.sitemaps.views import sitemap
from .sitemap import *
from django.urls import path
from django.contrib.sitemaps.views import sitemap

# from django.conf.urls import handler400, handler403, handler404, handler500

urlpatterns = [
    path('', views.index, name='index'),
    path('form_handler', views.index, name='form_handler'),
    path('blog', views.blog, name='blogs'),
    path('contact', views.contact, name='contact'),
    path('gallery', views.gallery, name='gallery'),
    path('csslink', views.csslink, name='css'),
    path('code', views.display_code_content, name='code'),
    path('code/?/title=<title>', views.html_render, name='codeblock'),
    path('render_blog/blog=<name>/?', views.render_blog, name='render_blog'),
    path('catogory_blog/<catogory>/?', views.blogfilter, name='blogfilter'),
    path('product_view/<name>/?/<title>/?', views.product_view, name='product_view'),
    path('sitemap.xml', sitemap, {
        'sitemaps': {"BlogSitemap": BlogSitemap, "ImageSitemap": GallerySiteMap, "HtmlSiteMap": HtmlSiteMap,
                     "cssSiteMap": CssLinkSiteMap}},
         name='django.contrib.sitemaps.views.sitemap')
]

handler400 = 'app1.views.bad_request'
handler403 = 'app1.views.permission_denied'
handler404 = 'app1.views.page_not_found'
handler500 = 'app1.views.server_error'
