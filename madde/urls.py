from django.urls import path
from . import views
#from .views import *

urlpatterns = [
    path('', views.index, name='index'),
    #path('new', IndexView.as_view(), name='newindex'),
    path('katogori/<int:kat_id>', views.dealcategory, name='dealcategory'),
    path('yenikelepirler', views.newdeals, name='newdeals'),
    path('ateslikelepirler', views.hottestdeals, name='ensicakkel'),
    path('kuponlar', views.kuponlarindeksi, name='kuponlarindeksi'),
    #path('madde/<int:pk>', views.MaddeDetailView.as_view(), name='madde_detay'),
    path('madde/<int:pk>', views.madde_detay, name='madde_detay'),
    path('profil/<int:pk>', views.profil_detay, name='profil_detay'),
    path('<int:madde_id>/upvote', views.upvote, name='upvote'),
    path('<int:madde_id>/downvote', views.downvote, name='downvote'),
    path('paylas/', views.submitdeal, name='paylas'),
    path('kpaylas/', views.submitkupon, name='kpaylas'),

    # for likes and votes
    path('like/', views.like_comment, name='like_comment'),
]
