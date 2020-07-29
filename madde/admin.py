from django.contrib import admin

# Register your models here.
from .models import Maddeler


class MaddelerAdmin(admin.ModelAdmin):
    list_display = ('paylasan', 'url', 'fiyat', 'kargo', 'kupon', 'baslik', 'ayrintilar', 'katagori', 'bas_tarih', 'son_tarih', 'online', 'diyar', 'derece','duyurmaTarihi','kaynamavakti','aktif','oylar')
    fields = ['paylasan','url', 'fiyat', 'kargo', 'kupon', 'baslik', 'ayrintilar', 'katagori', 'bas_tarih', 'son_tarih', 'online', 'diyar', 'derece','kaynamavakti','aktif','oylar']

    list_filter = ('paylasan','url', 'fiyat', 'kargo', 'kupon', 'baslik', 'ayrintilar', 'katagori', 'bas_tarih', 'son_tarih', 'online', 'diyar','derece','duyurmaTarihi','kaynamavakti','aktif','oylar')


admin.site.register(Maddeler, MaddelerAdmin)
