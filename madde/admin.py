from django.contrib import admin

# Register your models here.
from .models import Maddeler, Votes, Katagoriler


class MaddelerAdmin(admin.ModelAdmin):
    fields = ['paylasan','url', 'satici','fiyat', 'orjinalFiyat', 'kargo', 'kupon', 'baslik', 'goruntu', 'katagori', 'bas_tarih', 'son_tarih', 'online', 'diyar', 'derece','kaynamavakti','duyurmaTarihi','aktif','oylar']
    list_display = ('paylasan', 'url', 'satici', 'fiyat', 'orjinalFiyat', 'kargo', 'kupon', 'baslik', 'goruntu', 'bas_tarih', 'son_tarih', 'online', 'diyar', 'derece','duyurmaTarihi','kaynamavakti','aktif','oylar')

    list_filter = ('paylasan','url', 'satici','fiyat', 'kargo', 'kupon', 'baslik', 'katagori', 'bas_tarih', 'son_tarih', 'online', 'diyar','derece','duyurmaTarihi','kaynamavakti','aktif','oylar')


admin.site.register(Maddeler, MaddelerAdmin)
admin.site.register(Votes)
admin.site.register(Katagoriler)
