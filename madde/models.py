from django.db import models
from hesaplar.models import Kullanici


# Create your models here.
class Maddeler(models.Model):
    paylasan = models.ForeignKey(Kullanici, on_delete=models.CASCADE)
    url = models.URLField(max_length=200)
    fiyat = models.DecimalField(max_digits=5, decimal_places=2)
    kargo = models.BooleanField()
    kupon = models.CharField(max_length=100)
    baslik = models.CharField(max_length=300)
    ayrintilar = models.TextField()
    katagori = models.CharField(max_length=100)
    bas_tarih = models.DateField()
    son_tarih = models.DateField()
    online = models.BooleanField()
    mekan = models.CharField(max_length=100)
    derece = models.IntegerField(default=0)
    duyurmaTarihi = models.DateTimeField(auto_now=False, auto_now_add=True)
    kaynamavakti = models.DateTimeField(null=True, auto_now=False, auto_now_add=False)
    aktif = models.BooleanField(default=True)
    oylar = models.IntegerField(default=0)

class Votes(models.Model):
    kullanici = models.ForeignKey(Kullanici, on_delete=models.CASCADE)
    madde = models.ForeignKey(Maddeler, on_delete=models.CASCADE)
