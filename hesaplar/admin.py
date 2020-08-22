from django.contrib import admin

# Register your models here.
from .models import Kullanici


class KullaniciAdmin(admin.ModelAdmin):

    list_display = ('kullanici', 'paylasimlar', 'yorumlar', 'ensicak', 'takipciler', 'sehir', 'insta')
    fields = ['kullanici', 'paylasimlar', 'yorumlar', 'ensicak', 'takipciler', 'sehir', 'insta', 'resim']

admin.site.register(Kullanici, KullaniciAdmin)
