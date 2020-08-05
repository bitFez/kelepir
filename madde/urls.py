from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('kuponlar', views.kuponlarindeksi, name='kuponlarindeksi'),
    path('madde/<int:pk>', views.MaddeDetailView.as_view(), name='madde_detay'),
    path('<int:madde_id>/upvote', views.upvote, name='upvote'),
    path('<int:madde_id>/downvote', views.downvote, name='downvote'),
    path('paylas/', views.submitdeal, name='paylas'),
    path('kpaylas/', views.submitkupon, name='kpaylas'),

]
