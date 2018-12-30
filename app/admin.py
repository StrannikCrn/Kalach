from django.contrib import admin
from .models import *
from django_summernote.admin import SummernoteModelAdmin


class NewsPhotoInline(admin.TabularInline):
    model = NewsPhotoSpecif
    extra = 3


class NewsAdmin(SummernoteModelAdmin):
    inlines = [NewsPhotoInline]
    readonly_fields = ["url"]

admin.site.register(News,NewsAdmin)