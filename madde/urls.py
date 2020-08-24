from django.urls import path
from .import views

#app_name = 'madde'

urlpatterns = [
    path('', views.index, name='index'),
    path('serialised',views.madde_serialised, name='serialised_view'),
    #path('new', IndexView.as_view(), name='newindex'),
    path('katogori/<int:kat_id>', views.dealcategory, name='dealcategory'),
    path('yenikelepirler', views.newdeals, name='newdeals'),
    path('ateslikelepirler', views.hottestdeals, name='ensicakkel'),
    path('kuponlar', views.kuponlarindeksi, name='kuponlarindeksi'),
    #path('madde/<int:pk>', views.MaddeDetailView.as_view(), name='madde_detay'),
    path('madde/<int:pk>', views.madde_detay, name='madde_detay'),
    path('profil/<int:pk>', views.profil_detay, name='profil_detay'),
    #path('upvote', views.upvote, name='upvote'),
    #path('downvote', views.downvote, name='downvote'),
    path('vote/', views.product_vote, name='vote' ),
    #path('<int:madde_id>/vote/<int:votepref>/', views.vote, name='vote'),
    path('paylas/', views.submitdeal, name='paylas'),
    path('kpaylas/', views.submitkupon, name='kpaylas'),
    # Bookmarking a post
    path('kayitla/<int:id>/', views.bookmark, name='bookmark'),
    # for likes and votes
    path('like/', views.like_comment, name='like_comment'),
    path('expire/<int:id>', views.expire, name='expire'),

]
