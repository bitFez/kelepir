from django.db import models
#from hesaplar.models import Kullanici
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils import timezone
from ckeditor.fields import RichTextField


KATEGORI_SECIMLERI=(
    ('Elektronik','Elektronik'), ('Moda ve aksesuarlar', 'Moda ve aksesuarlar'), ('Bahçe ve DIY','Bahçe ve DIY'),('Kültür ve boş zaman','Kültür ve boş zaman'), ('bakkal alışveriş','bakkal alışveriş'), ('Oyun','Oyun'),
    )
class Katagoriler(models.Model):
    kategori = models.CharField(max_length=200, blank=True)
    ikon = models.CharField(max_length=50, blank=True)

    def __str__(self):
        return self.kategori

    def icon(self):
        return f"{self.ikon}"

# Create your models here.
class Maddeler(models.Model):
    paylasan = models.ForeignKey(User, on_delete=models.CASCADE)
    url = models.URLField(max_length=200, blank=True, null=True, help_text='<small>Kelepir internetten bulunduysa şurda websiteyi palşın</small>')
    satici = models.CharField(max_length=200, blank=True)
    fiyat = models.DecimalField(max_digits=8, decimal_places=2, help_text='İndirimli fıyat', verbose_name='Fıyat')
    orjinalFiyat = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True, help_text='Orjinal fıyat', verbose_name='orjinal Fıyatı')
    kargo = models.BooleanField(help_text='Kargo ücretsizse burayı tıklayın',null=True)
    kupon = models.CharField(max_length=100, null=True, blank=True, help_text='Bildirmek istediğiniz kupon varsa, buraya yazın')
    baslik = models.CharField(max_length=300, help_text='Kısa bir tanımlayıcı başlık', verbose_name='Başlık')
    ayrintilar = RichTextField(max_length=1000, help_text='Kelepiri kendi sözlerinizle anlatın ve neden kaçılmaz fırsat olduğunu başkalarına açıklayın.' ,verbose_name='Detaylı ayrıntılar')
    goruntu = models.ImageField(upload_to='madde_goruntuleri', null=True, blank=True, default="madde_goruntuleri/shopping.jpg", help_text='bir resim yüklemek, başkalarının anlaşmayı daha iyi anlamasına yardımcı olur', verbose_name='Görüntü')
    katagori = models.ManyToManyField('Katagoriler')
    bas_tarih = models.DateField(blank=True, null=True,verbose_name='İndirimin Başlangıç Tarihi')
    son_tarih = models.DateField(blank=True, null=True, verbose_name='İndirimin bitme tarihi')
    online = models.BooleanField(help_text='Yerel fırsat (mağazada / çevrimdışı)')
    diyar = models.CharField(max_length=100, null=True, blank=True)
    derece = models.IntegerField(default='0', null=True, blank=True)
    duyurmaTarihi = models.DateTimeField(default=timezone.now) # auto_now=False, auto_now_add=True, blank=True
    kaynamavakti = models.DateTimeField(null=True, blank=True, auto_now=False, auto_now_add=False)
    bookmarked = models.ManyToManyField(User, related_name='bookmarked', default=None, blank=True)
    tukenmiscagiri = models.ManyToManyField(User, related_name='expired_call', default=None, blank=True)
    aktif = models.BooleanField(default=True)
    oylar = models.IntegerField(default=0, null=True, blank=True)
    oyveren = models.ManyToManyField(User, blank=True, related_name="collected_votes")
    w3w = models.CharField(max_length=100, null=True, blank=True,verbose_name='What3Words', help_text='<a href="https://what3words.com/susma.hurma.e%C5%9Fyal%C4%B1"><small>Yardım ve örnek için şurayı tıklayın</small></a>')

    def __str__(self):
        return f"{self.id}, {self.baslik}"

    def get_categories(self):
        return "\n".join([k.katagori for k in self.katagori.all()])

    """@property
    def total_degrees(self):
        return self.derece"""

    def get_absolute_url(self):
        """Returns the url to access a particular product detail (madde_detay)."""
        return reverse('madde_detay', args=[self.slug])

KUPON_CESIT = (('YE','% İndirim'),('Tİ','<span class="fas fa-lira-sign"></span> İndirimi'),('BK','Bedava Kargo'))

class Kuponlar:
    paylasan = models.ForeignKey(User, on_delete=models.CASCADE)
    url = models.URLField(max_length=200, blank=True, null=True, help_text='<small>Kelepir internetten bulunduysa şurda websiteyi palşın</small>',)
    satici = models.CharField(max_length=200, blank=True)
    kupon = models.CharField(max_length=100, blank=True, help_text='Bildirmek istediğiniz kupon varsa, buraya yazın')
    kuponCesiti = models.CharField(null=True, max_length=50, choices=KUPON_CESIT, verbose_name='Küpon çeşiti')
    baslik = models.CharField(max_length=300, help_text='Kısa bir tanımlayıcı başlık', verbose_name='Başlık')
    ayrintilar = RichTextField(help_text='Kelepiri kendi sözlerinizle anlatın ve neden kaçılmaz fırsat olduğunu başkalarına açıklayın.' ,verbose_name='Detaylı ayrıntılar')
    bas_tarih = models.DateField(blank=True, null=True,verbose_name='İndirimin Başlangıç Tarihi')
    son_tarih = models.DateField(blank=True, null=True, verbose_name='İndirimin bitme tarihi')
    duyurmaTarihi = models.DateTimeField(default=timezone.now) # auto_now=False, auto_now_add=True, blank=True
    aktif = models.BooleanField(default=True)

class Votes(models.Model):
    kullanici = models.ForeignKey(User, on_delete=models.CASCADE)
    madde = models.ForeignKey(Maddeler, on_delete=models.CASCADE)
    date= models.DateTimeField(auto_now= True)
    oy = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.kullanici} , {self.madde}"



class Comment(models.Model):
    madde = models.ForeignKey(Maddeler, on_delete=models.CASCADE,related_name='comments')
    kullanici = models.ForeignKey(User, on_delete=models.CASCADE)
    body = RichTextField()
    created_on = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=False)
    #comment_slug = models.SlugField(unique=True, default=uuid.uuid4)
    likes = models.ManyToManyField(User, related_name='likes', blank=True)
    #parent = models.ForeignKey("self", null=True, blank=True, on_delete=models.CASCADE)

    class Meta:
        ordering = ['created_on']

    def __str__(self):
        return 'Comment {} by {}'.format(self.body, self.kullanici)

    '''def children(self): #replies
        return Comment.objects.filter(parent=self)

    def is_parent(self):
        if self.parent is not None:
            return False
        return True'''
    def total_likes(self):
        return self.likes.count()

class Commentlike(models.Model):
    comment = models.ForeignKey(Comment, related_name='related_comment', on_delete=models.CASCADE)
