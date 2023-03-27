from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
# from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import user_passes_test
# Create your views here.

from . models import Kullanici, CustomAccountManager

fake_users = [
    {"email":"oliver@aol.com", "user_name":"OllieOllieOllie", "first_name":"oliver", "password":"table130"},
    {"email":"loulou@gmail.com", "user_name":"chopsticks", "first_name":"Lou", "password":"table130"},
    {"email":"george@aol.com", "user_name":"George3000", "first_name":"George", "password":"table130"},
    {"email":"ali_khan@aol.com", "user_name":"AliKhan", "first_name":"Ali", "password":"table130"},
    {"email":"smithy@hotmail.com", "user_name":"johnsmith123", "first_name":"John", "password":"table130"},
    {"email":"priyesh@hotmail.com", "user_name":"priyesh_offers", "first_name":"Priyesh", "password":"table130"},
    {"email":"ramonrazor@aol.com", "user_name":"ramonrazor", "first_name":"Ramon", "password":"table130"},
    {"email":"marvels@marvel.com", "user_name":"marvels", "first_name":"Carol", "password":"table130"},
    {"email":"hacksawjimdougan@aol.com", "user_name":"hacksawjimdougan", "first_name":"Jim", "password":"table130"},
    {"email":"machomanrandysavagerip@aol.com", "user_name":"machomanrandysavagerip", "first_name":"Randy", "password":"table130"},
]

@user_passes_test(lambda u: u.is_superuser)
def add_fake_accounts(request):
    for i in fake_users:
        Kullanici.objects.update_or_create(
            email = i["email"],
            user_name=i["user_name"],
            first_name=i["first_name"],
            password=i["password"]
        )
        
    url = reverse('admin:index')
    return HttpResponseRedirect(url)

@user_passes_test(lambda u: u.is_superuser)
def remove_fake_accounts(request):
    for i in fake_users:
        Kullanici.objects.filter(user_name=i["user_name"]).delete()
    
    url = reverse('admin:index')
    return HttpResponseRedirect(url)