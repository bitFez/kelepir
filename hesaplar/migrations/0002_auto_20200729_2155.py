# Generated by Django 3.0.8 on 2020-07-29 21:55

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('hesaplar', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='kullanici',
            name='Kullanici',
        ),
        migrations.AddField(
            model_name='kullanici',
            name='kullanici',
            field=models.OneToOneField(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]
