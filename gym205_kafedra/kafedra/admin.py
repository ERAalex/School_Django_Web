from django.contrib import admin
from .models import article_main, gallery_main
from django.utils.safestring import mark_safe


@admin.register(article_main)
class Article_mainAdmin(admin.ModelAdmin):
    list_display = ['title', 'text', 'show_item']

@admin.register(gallery_main)
class Gallery_main_mainAdmin(admin.ModelAdmin):
    list_display = ['title', 'text', 'show_item', 'position']

