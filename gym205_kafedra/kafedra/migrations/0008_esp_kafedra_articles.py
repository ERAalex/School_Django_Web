# Generated by Django 4.0.3 on 2023-01-01 11:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kafedra', '0007_gallery_foto'),
    ]

    operations = [
        migrations.CreateModel(
            name='esp_kafedra_articles',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, unique=True)),
                ('position', models.CharField(max_length=150, null=True, verbose_name='позиция')),
                ('title', models.CharField(max_length=150, verbose_name='название')),
                ('text', models.TextField(max_length=2000, null=True, verbose_name='описание')),
                ('show_item', models.BooleanField(default=False, verbose_name='Отобразить')),
            ],
            options={
                'verbose_name': 'Кафедра испанского - статьи',
                'verbose_name_plural': 'Кафедра испанского - статьи',
            },
        ),
    ]