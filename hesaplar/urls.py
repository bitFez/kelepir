from django.urls import path
from .import views

app_name = 'hesaplar'

urlpatterns = [
    path('add_dummy', views.add_fake_accounts, name='add_fake_accounts'),
    path('remove_dummy', views.remove_fake_accounts, name='remove_fake_accounts'),
]