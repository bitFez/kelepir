# Generated by Django 3.1 on 2020-08-30 12:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('django_comments', '0003_add_submit_date_index'),
        ('madde', '0007_auto_20200829_2003'),
    ]

    operations = [
        migrations.DeleteModel(
            name='CustomComment',
        ),
    ]
