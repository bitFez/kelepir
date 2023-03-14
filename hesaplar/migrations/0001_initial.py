# Generated by Django 4.1.7 on 2023-03-14 10:33

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Kullanici',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('paylasimlar', models.IntegerField(default=0)),
                ('yorumlar', models.IntegerField(default=0)),
                ('ensicak', models.IntegerField(default=0)),
                ('takipciler', models.IntegerField(default=0)),
                ('dogum', models.DateField(blank=True, null=True)),
                ('resim', models.ImageField(blank=True, default='profiler/profile.png', null=True, upload_to='profiler')),
                ('sehir', models.CharField(max_length=200)),
                ('insta', models.CharField(blank=True, max_length=200, null=True)),
                ('kullanici', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
