from django.db import models
from django.urls import reverse


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

    def get_absolute_url(self):
        return reverse('render_blog', args=[str(self.id)])


class add_content_to_blog(models.Model):
    blog_number = models.ForeignKey(blog, on_delete=models.CASCADE)
    img = models.ImageField(blank=True, upload_to="vlog")
    youtubeLink = models.URLField(blank=True)
    des = models.TextField(blank=True)

    def __str__(self):
        aumate = str(self.blog_number) + str(self.id)
        return aumate


class ListFoContent(models.Model):
    title = models.TextField(blank=True)
    blogPostNumber = models.ForeignKey(add_content_to_blog, on_delete=models.CASCADE)
    listText = models.TextField(blank=False)

    def __str__(self):
        return str(self.blogPostNumber)


class ListOfImage(models.Model):
    blogPostNumber = models.ForeignKey(add_content_to_blog, on_delete=models.CASCADE)
    ImageSelect = models.ImageField(blank=True)
    imageUrl = models.URLField(blank=True)

    def __str__(self):
        return str(self.blogPostNumber)


class gallery(models.Model):
    img = models.ImageField(blank=False, upload_to="gallery")
    title = models.TextField(blank=True)
    des = models.TextField(blank=True)
    date = models.DateTimeField(auto_now=True, blank=False)

    def __str__(self):
        return str(self.title)

    def get_absolute_url(self):
        return f'/media/{self.img}'


class HtmlCode(models.Model):
    title = models.TextField(blank=False)
    image = models.ImageField(blank=True)
    css = models.TextField(blank=False)
    js = models.TextField(blank=True)
    html = models.TextField(blank=False)
    description = models.TextField(blank=True)
    date = models.DateTimeField(auto_now=True, blank=False)

    def __str__(self):
        return str(self.title)

    def get_absolute_url(self):
        return reverse('codeblock', args=[str(self.id)])


class CssFiles(models.Model):
    title = models.TextField(blank=False)
    file_choice = models.FileField(blank=False)
    date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.title)

    def get_absolute_url(self):
        return f'/media/{self.file_choice}'


class ViewCount(models.Model):
    data1 = models.TextField(blank=False)
    system = models.TextField(blank=False)
    meta = models.TextField(blank=False)

    def __str__(self):
        return str(self.system)


class Quiz_topic(models.Model):
    title = models.TextField(blank=False)

    def __str__(self):
        return str(self.title)


class CreateQuiz(models.Model):
    catogory = models.ForeignKey(Quiz_topic, on_delete=models.CASCADE, blank=True, null=True)
    title = models.TextField(blank=False)
    name = models.TextField(blank=False)
    auth_mail = models.TextField(blank=False)

    def __str__(self):
        return str(self.title)

    def get_absolute_url(self):
        return f"quizz/{self.id}/%3F"


class Quizs(models.Model):
    catogory = models.ForeignKey(CreateQuiz, on_delete=models.CASCADE, blank=True, null=True)
    qus = models.TextField(blank=False)
    op1 = models.TextField(blank=False)
    op2 = models.TextField(blank=False)
    op3 = models.TextField(blank=False)
    op4 = models.TextField(blank=False)
    ans = models.TextField(blank=False)

    def __str__(self):
        out = self.catogory if not None else self.qus
        return str(out)


class QuizResult(models.Model):
    selected = models.TextField(blank=False)
    total = models.TextField(blank=False)
    output = models.TextField(blank=False)
    date = models.DateTimeField(auto_now=True, blank=False)
    email = models.TextField(blank=False)

    def __str__(self):
        return str(self.email)


class VisitorIpAddress(models.Model):
    ip = models.TextField(blank=True)
    req = models.TextField(blank=True)

    def __str__(self):
        return str(self.ip)
