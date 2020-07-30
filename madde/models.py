from django.db import models
from hesaplar.models import Kullanici


# Create your models here.
class Maddeler(models.Model):
    paylasan = models.ForeignKey(Kullanici, on_delete=models.CASCADE)
    url = models.URLField(max_length=200, blank=True, null=True)
    fiyat = models.DecimalField(max_digits=5, decimal_places=2)
    orjinalFiyat = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    kargo = models.BooleanField()
    kupon = models.CharField(max_length=100, blank=True)
    baslik = models.CharField(max_length=300)
    ayrintilar = models.TextField()
    goruntu = models.ImageField(upload_to='madde_goruntuleri', null=True, blank=True, default="madde_goruntuleri/shopping.jpg")
    katagori = models.CharField(max_length=100)
    bas_tarih = models.DateField(blank=True, null=True)
    son_tarih = models.DateField(blank=True, null=True)
    online = models.BooleanField()
    diyar = models.CharField(max_length=100, blank=True)
    derece = models.IntegerField(default=0)
    duyurmaTarihi = models.DateTimeField(null=True, auto_now=False, auto_now_add=True, blank=True)
    kaynamavakti = models.DateTimeField(null=True, blank=True, auto_now=False, auto_now_add=False)
    aktif = models.BooleanField(default=True)
    oylar = models.IntegerField(default=0)


    def __str__(self):
        return f"{self.id}, {self.baslik}"


class Votes(models.Model):
    kullanici = models.ForeignKey(Kullanici, on_delete=models.CASCADE)
    madde = models.ForeignKey(Maddeler, on_delete=models.CASCADE)
