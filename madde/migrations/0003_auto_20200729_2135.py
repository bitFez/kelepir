# Generated by Django 3.0.8 on 2020-07-29 21:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('madde', '0002_auto_20200729_2124'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='maddeler',
            name='mekan',
        ),
        migrations.AddField(
            model_name='maddeler',
            name='diyar',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='maddeler',
            name='bas_tarih',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='maddeler',
            name='baslik',
            field=models.CharField(max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='maddeler',
            name='kargo',
            field=models.BooleanField(null=True),
        ),
        migrations.AlterField(
            model_name='maddeler',
            name='kupon',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='maddeler',
            name='son_tarih',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='maddeler',
            name='url',
            field=models.URLField(null=True),
        ),
    ]