# Generated by Django 3.2.9 on 2021-11-16 17:13

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('user_perfil', '0006_rename_usuario_perfil_usuario_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='perfil_usuario',
            name='user',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
