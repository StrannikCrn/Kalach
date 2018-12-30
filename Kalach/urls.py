"""Rusmaster URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls import url
from django.contrib import admin
from app.views import *
from django.views.static import serve
from django.conf.urls import include
from django.conf.urls.static import static

urlpatterns = [
    url(r'^summernote/', include('django_summernote.urls')),
    url (r'^robots.txt$',serve , { 'path' : "/robots.txt",'document_root': settings.MEDIA_ROOT,'show_indexes': False } ),
    url (r'^sitemap.xml$',serve , { 'path' : "/sitemap.xml",'document_root': settings.MEDIA_ROOT,'show_indexes': False } ),
    url (r'^cebb6da2106d.html$',serve , { 'path' : "/cebb6da2106d.html",'document_root': settings.MEDIA_ROOT,'show_indexes': False } ),
    url (r'^wmail_288e8d87a0822ecae39fefc201f12e52.html$',serve , { 'path' : "/wmail_288e8d87a0822ecae39fefc201f12e52.html",'document_root': settings.MEDIA_ROOT,'show_indexes': False } ),
    url (r'^BingSiteAuth.xml$',serve , { 'path' : "/BingSiteAuth.xml",'document_root': settings.MEDIA_ROOT,'show_indexes': False } ),
    url (r'^favicon.ico$',serve , { 'path' : "/favicon.ico",'document_root': settings.MEDIA_ROOT,'show_indexes': False } ),
    url(r'^$', index),
    url(r'^novosti-i-stati/(?P<url>.+)', news_item),
    url(r'^novosti-i-stati/$', news),
    url(r'^o-nas', aboutUs),
    url(r'^kto-nam-pomogaet', our_helpers),
    url(r'^contacts$', contacts),
    url(r'^napravleniya/peshera', peshera),
    url(r'^napravleniya/hram', hram),
    url(r'^napravleniya/gorod', gorod),
    url(r'^admin/', admin.site.urls),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
