# Generated by Django 3.2.9 on 2021-11-18 02:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Post_noticias', '0006_auto_20211117_2320'),
    ]

    operations = [
        migrations.AddField(
            model_name='postagem',
            name='subtitulo',
            field=models.CharField(default='subtitulo', max_length=400),
        ),
    ]
