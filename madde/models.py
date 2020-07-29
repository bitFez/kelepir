from django.db import models

# Create your models here.
class Maddeler(models.Model):
    url = models.URLField(max_length=200)
    fiyat = models.DecimalField(decimal_places=2)
    kargo = models.BooleanField()
    kupon = models.CharField(max_length=100)
    baslik = models.CharField(max_length=300)
    ayrintilar = models.TextField()
    bas_tarih = models.DateField()
    son_tarih = models.DateField()
    online = kargo = models.BooleanField()
    mekan = models.CharField(max_length=100)
