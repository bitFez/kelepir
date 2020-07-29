from django.contrib import admin

# Register your models here.
from .models import Maddeler


class MaddelerAdmin(admin.ModelAdmin):
    list_display = ('url', 'fiyat', 'kargo', 'kupon', 'baslik', 'ayrintilar', 'katagori', 'bas_tarih', 'son_tarih', 'online', 'mekan')
    fields = ['url', 'fiyat', 'kargo', 'kupon', 'baslik', 'ayrintilar', 'katagori', 'bas_tarih', 'son_tarih', 'online', 'mekan']

    list_filter = ('url', 'fiyat', 'kargo', 'kupon', 'baslik', 'ayrintilar', 'katagori', 'bas_tarih', 'son_tarih', 'online', 'mekan')


admin.site.register(Maddeler, MaddelerAdmin)
