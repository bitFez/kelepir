from django.contrib import admin
from ckeditor.widgets import CKEditorWidget

# Register your models here.
from .models import Maddeler, Katagoriler

class MaddelerAdmin(admin.ModelAdmin):
    fields = ['paylasan','url', 'satici','fiyat', 'orjinalFiyat', 'kargo', 'kupon', 'baslik', 'ayrintilar', 'goruntu', 'katagori', 'bas_tarih', 'son_tarih', 'online', 'diyar', 'derece','kaynamavakti','duyurmaTarihi','oyveren', 'bookmarked','aktif','oylar']
    list_display = ('paylasan', 'url', 'satici', 'fiyat', 'orjinalFiyat', 'kargo', 'kupon', 'baslik', 'bas_tarih', 'son_tarih', 'online', 'diyar', 'derece','duyurmaTarihi','kaynamavakti','aktif')

    list_filter = ('paylasan','url', 'satici','fiyat', 'kargo', 'kupon', 'baslik', 'katagori', 'bas_tarih', 'son_tarih', 'online', 'diyar','derece','duyurmaTarihi','kaynamavakti','aktif','oylar')



admin.site.register(Maddeler, MaddelerAdmin)
#admin.site.register(Votes)
admin.site.register(Katagoriler)
