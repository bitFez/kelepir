# Generated by Django 3.1 on 2020-09-25 21:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('madde', '0012_auto_20200913_1553'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='kuponlar',
            name='allow_comments',
        ),
        migrations.RemoveField(
            model_name='maddeler',
            name='allow_comments',
        ),
    ]