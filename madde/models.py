from django.db import models
from hesaplar.models import Kullanici
from django.urls import reverse
from django.utils import timezone

KATEGORI_SECIMLERI=(
    ('Elektronik','Elektronik'), ('Moda ve aksesuarlar', 'Moda ve aksesuarlar'), ('Bahçe ve DIY','Bahçe ve DIY'),('Kültür ve boş zaman','Kültür ve boş zaman'), ('bakkal alışveriş','bakkal alışveriş'), ('Oyun','Oyun'),
    )

# Create your models here.
class Maddeler(models.Model):
    paylasan = models.ForeignKey(Kullanici, on_delete=models.CASCADE)
    url = models.URLField(max_length=200, blank=True, null=True, help_text='<small>Kelepir internetten bulunduysa şurda websiteyi palşın</small>',)
    satici = models.CharField(max_length=200, blank=True)
    fiyat = models.DecimalField(max_digits=5, decimal_places=2,help_text='İndirimi fıyat', verbose_name='Fıyat')
    orjinalFiyat = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True,help_text='Orjinal fıyat',verbose_name='orjinal Fıyatı')
    kargo = models.BooleanField(help_text='Kargo ücretsizse burayı tıklayın')
    kupon = models.CharField(max_length=100, blank=True, help_text='Bildirmek istediğiniz kupon varsa, buraya yazın')
    baslik = models.CharField(max_length=300, help_text='Kısa bir tanımlayıcı başlık', verbose_name='Başlık')
    ayrintilar = models.TextField(help_text='Kelepiri kendi sözlerinizle anlatın ve neden kaçılmaz fırsat olduğunu başkalarına açıklayın.' ,verbose_name='Detaylı ayrıntılar')
    goruntu = models.ImageField(upload_to='madde_goruntuleri', null=True, blank=True, default="madde_goruntuleri/shopping.jpg", help_text='bir resim yüklemek, başkalarının anlaşmayı daha iyi anlamasına yardımcı olur', verbose_name='Görüntü')
    katagori = models.CharField(null=True, max_length=50, choices=KATEGORI_SECIMLERI)
    bas_tarih = models.DateField(blank=True, null=True,verbose_name='İndirimin Başlangıç Tarihi')
    son_tarih = models.DateField(blank=True, null=True, verbose_name='İndirimin bitme tarihi')
    online = models.BooleanField(help_text='Yerel fırsat (mağazada / çevrimdışı)')
    diyar = models.CharField(max_length=100, blank=True)
    derece = models.IntegerField(default=0)
    duyurmaTarihi = models.DateTimeField(default=timezone.now) # auto_now=False, auto_now_add=True, blank=True
    kaynamavakti = models.DateTimeField(null=True, blank=True, auto_now=False, auto_now_add=False)
    aktif = models.BooleanField(default=True)
    oylar = models.IntegerField(default=0)
    w3w = models.CharField(max_length=100, blank=True,verbose_name='What3Words', help_text='<a href="https://what3words.com/susma.hurma.e%C5%9Fyal%C4%B1"><small>Yardım ve örnek için şurayı tıklayın</small></a>')


    def __str__(self):
        return f"{self.id}, {self.baslik}"

    def get_absolute_url(self):
        """Returns the url to access a particular product detail (madde_detay)."""
        return reverse('madde_detay', args=[str(self.id)])

class Kuponlar:
    paylasan = models.ForeignKey(Kullanici, on_delete=models.CASCADE)
    url = models.URLField(max_length=200, blank=True, null=True, help_text='<small>Kelepir internetten bulunduysa şurda websiteyi palşın</small>',)
    satici = models.CharField(max_length=200, blank=True)
    kupon = models.CharField(max_length=100, blank=True, help_text='Bildirmek istediğiniz kupon varsa, buraya yazın')
    baslik = models.CharField(max_length=300, help_text='Kısa bir tanımlayıcı başlık', verbose_name='Başlık')
    ayrintilar = models.TextField(help_text='Kelepiri kendi sözlerinizle anlatın ve neden kaçılmaz fırsat olduğunu başkalarına açıklayın.' ,verbose_name='Detaylı ayrıntılar')
    bas_tarih = models.DateField(blank=True, null=True,verbose_name='İndirimin Başlangıç Tarihi')
    son_tarih = models.DateField(blank=True, null=True, verbose_name='İndirimin bitme tarihi')
    duyurmaTarihi = models.DateTimeField(default=timezone.now) # auto_now=False, auto_now_add=True, blank=True
    aktif = models.BooleanField(default=True)

class Votes(models.Model):
    kullanici = models.ForeignKey(Kullanici, on_delete=models.CASCADE)
    madde = models.ForeignKey(Maddeler, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.id} , {self.madde}"
