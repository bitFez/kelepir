from django.db import models

# Create your models here.
class Maddeler(models.Model):
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
