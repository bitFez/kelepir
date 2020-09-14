from django.contrib import admin
from ckeditor.widgets import CKEditorWidget

# Register your models here.
from .models import Maddeler, Katagoriler, Kuponlar

class MaddelerAdmin(admin.ModelAdmin):
    fields = ['paylasan','url', 'satici','fiyat', 'orjinalFiyat', 'kargo', 'kupon', 'baslik', 'ayrintilar', 'goruntu', 'katagori', 'bas_tarih', 'son_tarih', 'online', 'diyar', 'derece','kaynamavakti','duyurmaTarihi','oyveren', 'bookmarked','aktif','oylar', 'tukenmiscagiri', 'tukenmisSayi']
    list_display = ('paylasan', 'url', 'satici', 'fiyat', 'orjinalFiyat', 'kargo', 'kupon', 'baslik', 'bas_tarih', 'son_tarih', 'online', 'diyar', 'derece','duyurmaTarihi','kaynamavakti','aktif')

    list_filter = ('paylasan','url', 'satici','fiyat', 'kargo', 'kupon', 'baslik', 'katagori', 'bas_tarih', 'son_tarih', 'online', 'diyar','derece','duyurmaTarihi','kaynamavakti','aktif','oylar')

class KuponlarAdmin(admin.ModelAdmin):
    fields = ['paylasan','url', 'satici','kupon', 'kuponCesiti', 'baslik', 'ayrintilar', 'goruntu', 'bas_tarih', 'son_tarih', 'derece','duyurmaTarihi','oyveren', 'bookmarked','aktif','oylar', 'tukenmiscagiri', 'tukenmisSayi']
    list_display = ('paylasan','url', 'satici','kupon', 'kuponCesiti', 'baslik', 'bas_tarih', 'son_tarih', 'derece','duyurmaTarihi','aktif','oylar')

    list_filter = ('paylasan','url', 'satici', 'kupon', 'baslik', 'kuponCesiti', 'bas_tarih', 'son_tarih', 'derece','duyurmaTarihi','aktif','oylar')



admin.site.register(Maddeler, MaddelerAdmin)
admin.site.register(Kuponlar, KuponlarAdmin)
#admin.site.register(Votes)
admin.site.register(Katagoriler)
