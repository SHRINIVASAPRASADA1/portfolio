from django.conf import settings
from django.core.mail import send_mail
from django.shortcuts import render, redirect
from .forms import QuizForm
from .models import *
from .models import blog as blg
from .models import gallery as gal
from django.http import HttpResponse


def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return str(ip)


# Create your views here.
def index(request):
    collect = VisitorIpAddress(ip=get_client_ip(request), req=str(request.META))
    collect.save()
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
    # selected = request.POST["selected"]
    # for i in blg.objects.all():
    #     if i.under == selected:
    #         print(True)
    #     else:
    #         print(type(str(i.under)))
    if request.method == 'POST':
        return render(request, "app1/blogfilter.html", context={
            "blog": blg.objects.all(),
            "category": blog_catogory.objects.all(),
            "selected": request.POST["selected"],
        })


def render_blog(request, name):
    if request.method == "POST":
        blogid = request.POST["blognumber"]
        return render(request, "app1/viewBlog.html", context={
            "product": blg.objects.filter(id=blogid).get(),
            "extra": add_content_to_blog.objects.all(),
            "ListOfContent": ListFoContent.objects.all(),
            "ListOfImages": ListOfImage.objects.all()
        })
    return render(request, "app1/viewBlog.html", context={
        "product": blg.objects.filter(id=name).get(),
        "extra": add_content_to_blog.objects.all(),
        "ListOfContent": ListFoContent.objects.all(),
        "ListOfImages": ListOfImage.objects.all()
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
    return render(request, "app1/contact.html")


def render_contact(request):
    return render(request, "app1/contact.html")


def display_code_content(request):
    return render(request, "app1/codecontent.html", context={
        "codes": HtmlCode.objects.all()
    })


def html_render(request, title):
    code = HtmlCode.objects.filter(id=int(title)).get()
    if request.method == "POST":
        if request.POST["para"] == "view":
            code = HtmlCode.objects.filter(id=int(request.POST["nowid"])).get()
            full_process = f"""
                 <!DOCTYPE html>
            <html lang="en">
              <head>
                <meta charset="UTF-8" />
                <meta http-equiv="X-UA-Compatible" content="IE=edge" />
                <meta name="viewport" content="width=device-width, initial-scale=1.0" />
                <title>{code.title}</title>
                <style>
                 {code.css}
                </style>
              </head>
              <body>
                   {code.html}

                  <script>
                   {code.js}
                  </script>
              </body>
                """
            return HttpResponse(full_process)
        if request.POST["para"] == "code":
            code = HtmlCode.objects.filter(id=int(request.POST["nowid"])).get()
            return render(request, "app1/codeshow.html", context={
                "code": code,
            })

    full_process = f"""
                     <!DOCTYPE html>
                <html lang="en">
                  <head>
                    <meta charset="UTF-8" />
                    <meta http-equiv="X-UA-Compatible" content="IE=edge" />
                    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
                    <title>{code.title}</title>
                    <style>
                     {code.css}
                    </style>
                  </head>
                  <body>
                       {code.html}

                      <script>
                       {code.js}
                      </script>
                  </body>
                    """
    return HttpResponse(full_process)


def bad_request(request, exception):
    return HttpResponse(f"bad req {exception}")


def permission_denied(request, exception):
    return HttpResponse(f"permission_denied req {exception}")


def page_not_found(request, exception):
    return HttpResponse(f"page_not_found req {exception}")


def server_error(request):
    return HttpResponse("server_error req")


def csslink(request):
    return render(request, "app1/cssLink.html", context={
        "css": CssFiles.objects.all()
    })


def Quiz(request):
    return render(request, "app1/quiz.html", context={
        "quiz": CreateQuiz.objects.all(),
        "cat": Quiz_topic.objects.all()
    })


def QUizView(request, cat):
    if request.method == "POST":
        return render(request, "app1/openquiz.html", context={
            "items": Quizs.objects.filter(catogory=cat).all(),
            "catogory": CreateQuiz.objects.filter(catogory=cat).get().title
        })
    return render(request, "app1/openquiz.html")


def report_answer(request):
    if request.method == "POST":
        if "catos" not in request.POST:
            return redirect("quiz")
        rightans = []
        alter = sorted(list(request.POST))
        alter.pop()
        alter.pop()
        alter.pop()
        for item in alter:
            rightans.append(request.POST[item])
        result = QuizResult(selected=request.POST["catos"], total=len(alter) / 2,
                            output=len(alter) - len(set(rightans)),
                            email=request.POST["email"])
        result.save()
        return redirect("simple_redirect", email=request.POST["email"])
    return HttpResponse("Server Busy")


def search_report(request):
    if request.method == "POST":
        if "search" in request.POST:
            return render(request, "app1/output.html", context={
                "email": request.POST["email"],
                "all": QuizResult.objects.filter(email=request.POST["email"]).order_by("-date").all()
            })
    return HttpResponse("Report")


def simple_redirect(request, email):
    return render(request, "app1/output.html", context={
        "email": email,
        "all": QuizResult.objects.filter(email=email).order_by("-date").all()
    })


def createQuiz(request):
    return render(request, "app1/createquiz.html", context={
        "myform": QuizForm(request.POST, request.FILES)
    })
