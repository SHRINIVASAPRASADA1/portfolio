from django.conf import settings
from django.core.mail import send_mail
from django.shortcuts import render
from .models import *
from .models import blog as blg
from .models import gallery as gal


# Create your views here.
def index(request):
    return render(request, "app1/index.html", context={
        "project": projects.objects.all()
    })


def product_view(request, name, title):
    if request.method == "POST":
        return render(request, "app1/product.html", context={
            "project": projects.objects.filter(id=int(request.POST["projectid"])).get()
        })


def blog(request):
    return render(request, "app1/blog.html", context={
        "blog": blg.objects.all(),
        "category": blog_catogory.objects.all(),
    })


def blogfilter(request, catogory):
    selected = request.POST["selected"]
    for i in blg.objects.all():
        if i.under == selected:
            print(True)
        else:
            print(type(str(i.under)))
    if request.method == 'POST':
        return render(request, "app1/blogfilter.html", context={
            "blog": blg.objects.all(),
            "category": blog_catogory.objects.all(),
            "selected": request.POST["selected"],
        })


def render_blog(request, name):
    # blogid = request.POST["blognumber"]
    print(name)
    if request.method == "POST":
        return render(request, "app1/viewBlog.html", context={
            "product": blg.objects.filter(id=name).get(),
            "extra": add_content_to_blog.objects.all(),
        })
    return render(request, "app1/viewBlog.html", context={
        "product": blg.objects.filter(id=name).get(),
        "extra": add_content_to_blog.objects.all(),
    })


def gallery(request):
    return render(request, "app1/gallery.html", context={
        "images": gal.objects.all(),
    })


def render_gallery(request):
    return render(request, "app1/gallery.html")


def contact(request):
    if request.method == "POST":
        email = request.POST["email"]
        subject = request.POST["subject"]
        body = request.POST["body"]
        send_mail(f"Thanks For contacting us.. subject= {subject}",
                  f"Your Request has been submited our support team contact you ... for further query email = {email}, body ={body} ",
                  settings.EMAIL_HOST_USER, ["prasadashrinivasa@gmail.com", email])
    return render(request, "app1/contact.html")


def render_contact(request):
    return render(request, "app1/contact.html")
