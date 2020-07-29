# Generated by Django 3.0.8 on 2020-07-29 11:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Maddeler',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.URLField()),
                ('fiyat', models.DecimalField(decimal_places=2, max_digits=5)),
                ('kargo', models.BooleanField()),
                ('kupon', models.CharField(max_length=100)),
                ('baslik', models.CharField(max_length=300)),
                ('ayrintilar', models.TextField()),
                ('katagori', models.CharField(max_length=100)),
                ('bas_tarih', models.DateField()),
                ('son_tarih', models.DateField()),
                ('online', models.BooleanField()),
                ('mekan', models.CharField(max_length=100)),
            ],
        ),
    ]
