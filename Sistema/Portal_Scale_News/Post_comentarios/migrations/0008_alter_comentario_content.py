# Generated by Django 3.2.9 on 2021-11-17 21:15

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Post_comentarios', '0007_auto_20211117_2115'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comentario',
            name='content',
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
    ]
