# Generated by Django 3.1 on 2020-08-22 15:29

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('madde', '0034_auto_20200822_1629'),
    ]

    operations = [
        migrations.AlterField(
            model_name='maddeler',
            name='duyurmaTarihi',
            field=models.DateTimeField(verbose_name=datetime.datetime(2020, 8, 22, 15, 29, 33, 214899, tzinfo=utc)),
        ),
    ]
