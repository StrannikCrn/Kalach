from django.db import models
import transliterate
import os


class News(models.Model):
    url = models.CharField(max_length=255, verbose_name="URL",default="",blank=True)
    name = models.CharField(max_length=255, verbose_name="Название")
    date = models.DateTimeField( verbose_name="Дата")
    text = models.TextField(verbose_name="Текст")
    short_text = models.CharField(max_length=255,verbose_name="Текст на главную", default="")

    def save(self, *args, **kwargs):
        trimed_name = self.name.replace(" ","_").replace("ь","").replace("ъ","")
        url = transliterate.translit(trimed_name, reversed=True)
        self.url = url
        super(News, self).save(*args, **kwargs)

    def __str__(self):
        return str(self.name)

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости и статьи'


class NewsPhotoSpecif(models.Model):
    news_item = models.ForeignKey(News,related_name="gallery_photos",verbose_name="Фото в галлерею",on_delete=models.CASCADE)
    image = models.ImageField(upload_to="News/", verbose_name="Фото")
    caption = models.TextField(verbose_name="Подпись", default="")

    def __str__(self):
        return str("")

    class Meta:
        verbose_name = 'Фото в галлерею'
        verbose_name_plural = 'Фото в галлерею'