from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.
class Kullanici(models.Model):
    kullanici = models.OneToOneField(User, on_delete=models.CASCADE)
    paylasimlar = models.IntegerField()
    yorumlar = models.IntegerField()
    ensicak = models.IntegerField()
    takipciler = models.IntegerField()
    sehir = models.CharField(max_length=200)

    def __str__(self):
        return self.kullanici.username
