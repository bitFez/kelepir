from django.urls import path
from .import views

# app_name = 'madde'

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
    path('kupon_guncelle/<int:pk>', views.kupon_guncelle, name='kupon_guncelle'),

    path('madde/<int:pk>', views.madde_detay, name='madde_detay'),
    path('madde_guncelle/<int:pk>', views.madde_guncelle, name='madde_guncelle'),

    path('profil/<int:pk>', views.profil_detay, name='profil_detay'),

    path('upvote/<int:id>', views.product_upvote, name='upvote' ),
    path('downvote/<int:id>', views.product_downvote, name='downvote' ),
    path('bookmarkLV/<int:id>', views.bookmarkInListView, name='bookmarklv'),
    path('kvote/', views.coupon_vote, name='kvote' ),
    path('paylas/', views.submitdeal, name='paylas'),
    path('kpaylas/', views.submitkupon, name='kpaylas'),
    # Bookmarking a post
    path('kayitla/<int:id>/', views.bookmark, name='bookmark'),
    #path('kayitla/', views.bookmark, name='bookmark'),
    path('kkayitla/<int:id>/', views.kbookmark, name='kbookmark'),
    # for likes and votes
    path('expire/<int:id>', views.expire, name='expire'),
    path('expirek/<int:id>', views.expirek, name='expire_coupons'),

]
