from django.conf import settings
from django.core.mail import send_mail
from django.shortcuts import render, redirect
from .models import *
from .models import Blogs as blg
from .models import Gallery as gal
from django.http import HttpResponse

from .sitemap import BlogSitemap


def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return str(ip)


# Create your views here.
def index(request):
    collect = VisitorIpAddress(ip=get_client_ip(request), req=str(request.META),
                               device=str(request.META['HTTP_USER_AGENT']))
    collect.save()
    return render(request, "app1/index.html", context={
        "projects": Project.objects.all(),
        "social": SocialLink.objects.all(),
        "skill":skills.objects.all()
    })


def product_view(request, name, title):
    if request.method == "POST":
        return render(request, "app1/product.html", context={
            "project": Project.objects.filter(id=int(name)).get()
        })
    return render(request, "app1/product.html", context={
        "project": Project.objects.filter(id=int(name)).get()
    })


def blog(request):
    return render(request, "app1/blog.html", context={
        "blog": blg.objects.all(),
        "category": BlogCatogory.objects.all(),
    })


def blogfilter(request, catogory):
    if request.method == 'POST':
        return render(request, "app1/blogfilter.html", context={
            "blog": blg.objects.all(),
            "category": BlogCatogory.objects.all(),
            "selected": request.POST["selected"],
        })
    return render(request, "app1/blogfilter.html", context={
        "blog": blg.objects.all(),
        "category": BlogCatogory.objects.all(),
        "selected": str(catogory),
    })


def render_blog(request, name):
    main_obj = blg.objects.get(id=name)
    demo = InsertContent.objects.all().filter(blog_number_id=main_obj.id)
    return render(request, "app1/viewBlog.html", context={
        "product": main_obj,
        "extra": demo,

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
                  settings.EMAIL_HOST_USER, ["prasadashrinivasa@gmail.com"])
    return redirect("thank")


def bad_request(request, exception):
    return render(request, "app1/error.html")


def permission_denied(request, exception):
    return render(request, "app1/error.html")


def page_not_found(request, exception):
    return render(request, "app1/error.html")


def server_error(request):
    return render(request, "app1/error.html")


def NotesView(request):
    data = NotesUpload.objects.all()
    return render(request, "app1/notes.html", context={
        "note": data
    })


def LinkAdded(request):
    data = LinksAddOn.objects.all()
    return render(request, "app1/links.html", context={
        "note": data
    })


def HandleNotes(request, notesName, id):
    data = NotesUpload.objects.filter(id=id).get()
    add = AddNotes.objects.filter(fkey_id=data.id).all()
    return render(request, "app1/notesview.html", context={
        "item": data,
        "add": add
    })


def thank(request):
    return render(request, "app1/thank.html")


def error404page(request):
    return render(request, "app1/error.html")


def search(request):
    if request.method == "POST":
        search_res = request.POST["myquerry"]
        if search_res == "":
            pass
    return render(request, "app1/search.html")
