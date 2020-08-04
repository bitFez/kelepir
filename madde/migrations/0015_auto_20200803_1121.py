# Generated by Django 3.0.8 on 2020-08-03 10:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('madde', '0014_auto_20200802_1928'),
    ]

    operations = [
        migrations.AddField(
            model_name='maddeler',
            name='satici',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AlterField(
            model_name='maddeler',
            name='url',
            field=models.URLField(blank=True, help_text='<small>Kelepir internetten bulunduysa şurda websiteyi palşın</small>', null=True),
        ),
        migrations.AlterField(
            model_name='maddeler',
            name='w3w',
            field=models.CharField(blank=True, help_text='<a href="https://what3words.com/susma.hurma.e%C5%9Fyal%C4%B1"><small>Yardım ve örnek için şurayı tıklayın</small></a>', max_length=100, verbose_name='What3Words'),
        ),
    ]