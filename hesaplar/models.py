from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.
class Kullanici(models.Model):
    kullanici = models.OneToOneField(User, on_delete=models.CASCADE)
    paylasimlar = models.IntegerField(default=0)
    yorumlar = models.IntegerField(default=0)
    ensicak = models.IntegerField(default=0)
    takipciler = models.IntegerField(default=0)
    dogum = models.DateField(null=True, blank=True)
    resim = models.ImageField(upload_to='profiler', null=True, blank=True, default="profiler/profile.png")
    sehir = models.CharField(max_length=200)
    insta = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self):
        return self.kullanici.username
