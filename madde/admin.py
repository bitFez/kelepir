from django.contrib import admin
from ckeditor.widgets import CKEditorWidget

# Register your models here.
from .models import Maddeler, Votes, Katagoriler, Comment, Commentlike


class MaddelerAdmin(admin.ModelAdmin):
    fields = ['paylasan','url', 'satici','fiyat', 'orjinalFiyat', 'kargo', 'kupon', 'baslik', 'goruntu', 'katagori', 'bas_tarih', 'son_tarih', 'online', 'diyar', 'derece','kaynamavakti','duyurmaTarihi', 'slug','oyveren', 'bookmarked','aktif','oylar']
    list_display = ('paylasan', 'url', 'satici', 'fiyat', 'orjinalFiyat', 'kargo', 'kupon', 'baslik', 'goruntu', 'bas_tarih', 'son_tarih', 'online', 'diyar', 'derece','duyurmaTarihi','kaynamavakti','aktif','oylar')

    list_filter = ('paylasan','url', 'satici','fiyat', 'kargo', 'kupon', 'baslik', 'katagori', 'bas_tarih', 'son_tarih', 'online', 'diyar','derece','duyurmaTarihi','kaynamavakti','aktif','oylar')

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('kullanici', 'body', 'madde', 'created_on', 'active')
    list_filter = ('active', 'created_on')
    search_fields = ('kullanici', 'body')
    actions = ['approve_comments']

    def approve_comments(self, request, queryset):
        queryset.update(active=True)



admin.site.register(Maddeler, MaddelerAdmin)
admin.site.register(Votes)
admin.site.register(Katagoriler)
admin.site.register(Commentlike)
