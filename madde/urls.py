from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('madde/<int:pk>', views.MaddeDetailView.as_view(), name='madde_detay'),
]
