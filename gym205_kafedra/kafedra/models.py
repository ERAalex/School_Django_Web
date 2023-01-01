from django.db import models


class article_main(models.Model):
    id = models.AutoField(primary_key=True, unique=True)
    title = models.CharField('название', max_length=150)
    text = models.TextField('описание', max_length=2000)
    show_item = models.BooleanField('Отобразить', default=False)


    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Главная страница - статьи'
        verbose_name_plural = 'Главная страница - статьи'



class gallery_main(models.Model):
    id = models.AutoField(primary_key=True, unique=True)
    position = models.CharField('позиция', max_length=150)
    title = models.CharField('название', max_length=150)
    text = models.TextField('описание', max_length=2000)
    show_item = models.BooleanField('Отобразить', default=False)
    image = models.ImageField(null=True, blank=True, upload_to='static/img/gallery_temporal/', verbose_name='Фото')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Галерея новостей'
        verbose_name_plural = 'Галерея новостей'