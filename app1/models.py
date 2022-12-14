from django.db import models
from django.urls import reverse


# Create your models here.

class Project(models.Model):
    title = models.TextField(blank=False)
    image = models.ImageField(blank=False, upload_to="projects")
    date = models.DateTimeField(blank=False, auto_now=True)
    des = models.TextField(blank=True)
    start = models.DateField(auto_now=True)
    end = models.DateField(auto_now=True)
    lang = models.TextField(blank=True)
    Platform = models.TextField(blank=True)
    link = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return f'/product_view/{self.id}/%3F/{self.title}/%3F'


class BlogCatogory(models.Model):
    blog_catogorys_name = models.TextField(blank=False)
    date = models.DateTimeField(auto_now=True)
    des = models.TextField(blank=True)

    def __str__(self):
        return str(self.blog_catogorys_name)


class Blogs(models.Model):
    under = models.ForeignKey(BlogCatogory, on_delete=models.CASCADE)
    title = models.TextField(blank=False)
    des = models.TextField(blank=False)
    img = models.ImageField(upload_to="blog/%Y/%m/%d")
    date = models.DateTimeField(auto_now=True)
    source = models.TextField(blank=False)
    source_link = models.URLField(blank=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('render_blog', args=[str(self.id)])


class InsertContent(models.Model):
    title = models.TextField(blank=True, null=True)
    code = models.TextField(blank=True, null=True)
    blog_number = models.ForeignKey(Blogs, on_delete=models.CASCADE)
    img = models.ImageField(blank=True, upload_to="vlog")
    youtubeLink = models.URLField(blank=True)
    des = models.TextField(blank=True)

    def __str__(self):
        aumate = str(self.blog_number) + str(self.id)
        return aumate


class Gallery(models.Model):
    img = models.ImageField(blank=False, upload_to="gallery")
    title = models.TextField(blank=True)
    des = models.TextField(blank=True)
    date = models.DateTimeField(auto_now=True, blank=False)

    def __str__(self):
        return str(self.title)

    def get_absolute_url(self):
        return f'/media/{self.img}'


class VisitorIpAddress(models.Model):
    ip = models.TextField(blank=True)
    req = models.TextField(blank=True)
    date = models.DateTimeField(blank=True, auto_now=True)
    device = models.TextField(blank=True)

    def __str__(self):
        return str(self.ip)


class NotesUpload(models.Model):
    title = models.TextField(blank=False)
    des = models.TextField(blank=False)
    file = models.FileField(blank=True)
    file2 = models.FileField(blank=True)
    file3 = models.FileField(blank=True)
    date = models.DateTimeField(blank=False, auto_now=True)

    def __str__(self):
        return str(self.title)

    def get_absolute_url(self):
        return f'/Notes/{self.title}/{self.id}'


class LinksAddOn(models.Model):
    link = models.URLField(blank=True)
    title = models.TextField(blank=False)
    thumb = models.ImageField(blank=True,
                              default="https://img.icons8.com/ios-glyphs/512/link.png")
    extra = models.TextField(blank=True)
    date = models.DateTimeField(auto_now=True, blank=False)

    def __str__(self):
        return str(self.title)


class AddNotes(models.Model):
    fkey = models.ForeignKey(NotesUpload, blank=False, null=True, on_delete=models.CASCADE)
    title = models.TextField(blank=False)
    des = models.TextField(blank=False)
    file = models.FileField(blank=True)
    date = models.DateTimeField(blank=False, auto_now=True)

    def __str__(self):
        return str(self.title)


class SocialLink(models.Model):
    link = models.URLField(blank=False, null=False)
    logo = models.ImageField(blank=False, null=False)
    platform = models.TextField(blank=True)
    date = models.DateTimeField(blank=False, null=False, auto_now=True)

    def __str__(self):
        return str(self.link)


class skills(models.Model):
    link = models.URLField(blank=True)
    title = models.TextField(blank=False)
    logo = models.ImageField(blank=True)
    expertise = models.IntegerField(blank=True)

    def __str__(self):
        return str(self.title)
