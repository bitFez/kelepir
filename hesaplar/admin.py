from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

# Register your models here.
from .models import Kullanici


class KullaniciAdmin(admin.ModelAdmin):

    list_display = ('user_name', 'paylasimlar', 'yorumlar', 'ensicak', 'takipciler', 'sehir', 'insta')
    fields = ['user_name', 'paylasimlar', 'yorumlar', 'ensicak', 'takipciler', 'sehir', 'insta']

admin.site.register(Kullanici, KullaniciAdmin)
