from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import article_main, gallery_main, gallery_foto



def index(request):
    article_main_position1 = article_main.objects.filter(title='position1')
    gallery_main_title = gallery_main.objects.filter(position='position_main')
    gallery_main_articles = gallery_main.objects.filter(show_item=True)
    gallery_foto_sch = gallery_foto.objects.filter(show_item=True)

    # блок отправки письма
    return render(request, 'index.html', {'article_main_position1': article_main_position1,
                                          'gallery_main_title': gallery_main_title,
                                          'gallery_foto_sch': gallery_foto_sch,
                                          'gallery_main_articles': gallery_main_articles})