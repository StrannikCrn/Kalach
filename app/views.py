from django.core.mail import send_mail
from django.shortcuts import get_object_or_404
from django.shortcuts import redirect
from django.shortcuts import render

from .models import *

# mailAddress="strannikcrn@yandex.ru"
mailAddressFrom = "site@rusmaster48.ru"
mailAddress = "zakaz@rusmaster48.ru"
# mailAddress="nuclear_crew@mail.ru"
# mailAddress="plotnikov@gorstroy36.ru"
defaultNone = "Отсутствует"


######## AJAX METHODS ########


##################################

def index(request):
    news = News.objects.all().order_by("-date")[:3]
    news_f = News.objects.all().order_by("-date")[:6]
    return render(request, 'app/index.html', {'isIndex': True, 'some_news':news, 'footer_news':news_f})


def contacts(request):
    news_f = News.objects.all().order_by("-date")[:6]
    return render(request, 'app/contacts.html', {'footer_news':news_f})


def aboutUs(request):
    news_f = News.objects.all().order_by("-date")[:6]
    return render(request, 'app/aboutUs.html', {'footer_news':news_f})


def our_helpers(request):
    news_f = News.objects.all().order_by("-date")[:6]
    return render(request, 'app/our_helpers.html', {'footer_news':news_f})


def news(request):
    news_f = News.objects.all().order_by("-date")[:6]
    news_list = News.objects.all().order_by("-date")
    return render(request, 'app/news.html', {"news_list": news_list,'footer_news':news_f})


def news_item(request, url):
    news_f = News.objects.all().order_by("-date")[:6]
    news_list = News.objects.all().order_by("-date")[:6]
    result = get_object_or_404(News, url=url)
    return render(request, 'app/news_item.html',
                  {"res_news": result, "bot_news": news_list,'footer_news':news_f})


def peshera(request):
    news_f = News.objects.all().order_by("-date")[:6]
    return render(request, 'app/services/peshera.html', {'footer_news':news_f})


def gorod(request):
    news_f = News.objects.all().order_by("-date")[:6]
    return render(request, 'app/services/gorod.html',{'footer_news':news_f})


def hram(request):
    news_f = News.objects.all().order_by("-date")[:6]
    return render(request, 'app/services/hram.html', {'footer_news':news_f})

######################################################

def checkRequest(request):
    if 'mess' in request.POST:
        name = request.POST.get('name', '')
        cellphone = request.POST.get('email', '')
        text = request.POST.get('text', '')
        mailText = "Имя: " + name
        mailText += "\nТелефон/Email: " + cellphone
        mailText += "\nСообщение: " + text
        send_mail('(с сайта) Сообщение', mailText, mailAddressFrom, [mailAddress], fail_silently=False)
    if 'ItsCallMe' in request.POST:
        name = request.POST.get('name', '')
        cellphone = request.POST.get('cellphone', '')
        mailText = "Имя: " + name
        mailText += "\nТелефон: " + cellphone
        send_mail('(с сайта) Перезвоните мне', mailText, mailAddressFrom, [mailAddress], fail_silently=False)
        return redirect(request.META.get('HTTP_REFERER'))
    if 'Zayavka' in request.POST:
        name = request.POST.get('name', '')
        cellphone = request.POST.get('cellphone', '')
        mail = request.POST.get('mail', '')
        text = request.POST.get('description', '')
        mailText = "Имя: {}\nТелефон {}\nEmail {}\nТекст {}".format(name, cellphone, mail, text)

        send_mail('(с сайта) Заявка', mailText, mailAddressFrom, [mailAddress], fail_silently=False)
