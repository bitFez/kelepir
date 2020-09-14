from django.urls import path
from .import views

#app_name = 'madde'

urlpatterns = [
    path('', views.index, name='index'),
    #path('serialised',views.madde_serialised, name='serialised_view'),
    #path('new', IndexView.as_view(), name='newindex'),
    path('katogori/<int:kat_id>', views.dealcategory, name='dealcategory'),
    path('yenikelepirler', views.newdeals, name='newdeals'),
    path('ateslikelepirler', views.hottestdeals, name='ensicakkel'),
    path('kuponlar', views.kuponlarindeksi, name='kuponlarindeksi'),
    path('ateslikuponlar', views.ateslikuponlar, name='ateslikuponlar'),
    path('yenikuponlar', views.yenikuponlar, name='yenikuponlar'),
    path('kupon/<int:pk>', views.kupon_detay, name='kupon_detay'),

    path('madde/<int:pk>', views.madde_detay, name='madde_detay'),
    path('madde_guncelle', views.madde_guncelle, name='madde_guncelle'),

    path('profil/<int:pk>', views.profil_detay, name='profil_detay'),

    path('vote/', views.product_vote, name='vote' ),
    path('kvote/', views.coupon_vote, name='kvote' ),
    path('paylas/', views.submitdeal, name='paylas'),
    path('kpaylas/', views.submitkupon, name='kpaylas'),
    # Bookmarking a post
    path('kayitla/<int:id>/', views.bookmark, name='bookmark'),
    path('kkayitla/<int:id>/', views.bookmark, name='bookmark_coupons'),
    # for likes and votes
    path('expire/<int:id>', views.expire, name='expire'),
    path('expirek/<int:id>', views.expirek, name='expire_coupons'),

]
