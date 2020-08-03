from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('madde/<int:pk>', views.MaddeDetailView.as_view(), name='madde_detay'),
    path('<int:madde_id>/upvote', views.upvote, name='upvote'),
    path('<int:madde_id>/downvote', views.upvote, name='downvote'),
    path('paylas/', views.submitdeal, name='paylas'),

]
