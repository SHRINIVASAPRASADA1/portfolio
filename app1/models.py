from django.db import models


# Create your models here.

class projects(models.Model):
    title = models.TextField(blank=False)
    image = models.ImageField(blank=False, upload_to="projects")
    date = models.DateTimeField(blank=False, auto_now=True)
    des = models.TextField(blank=True)
    start = models.DateField(auto_now=True)
    end = models.DateField(auto_now=True)
    lang = models.TextField(blank=True)
    Platform = models.TextField(blank=True)

    def __str__(self):
        return self.title


class blog_catogory(models.Model):
    blog_catogorys_name = models.TextField(blank=False)
    date = models.DateTimeField(auto_now=True)
    des = models.TextField(blank=True)

    def __str__(self):
        return str(self.blog_catogorys_name)


class blog(models.Model):
    under = models.ForeignKey(blog_catogory, on_delete=models.CASCADE)
    title = models.TextField(blank=False)
    des = models.TextField(blank=False)
    img = models.ImageField(upload_to="blog/%Y/%m/%d")
    date = models.DateTimeField(auto_now=True)
    source = models.TextField(blank=False)
    source_link = models.URLField(blank=True)

    def __str__(self):
        return self.title


class add_content_to_blog(models.Model):
    blog_number = models.ForeignKey(blog, on_delete=models.CASCADE)
    img = models.ImageField(blank=True, upload_to="blog/%Y/%m/%d")
    des = models.TextField(blank=True)

    def __str__(self):
        return str(self.blog_number)


class gallery(models.Model):
    img = models.ImageField(blank=False, upload_to="gallery")
    title = models.TextField(blank=True)
    des = models.TextField(blank=True)
    date = models.DateTimeField(auto_now=True, blank=False)

    def __str__(self):
        return str(self.title)