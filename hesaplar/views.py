from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
# from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required

# Create your views here.

from . models import Kullanici
from madde.models import Maddeler, Katagoriler

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

product_categories = [
    {"kategori":"Moda ve Aksesuarlar", "ikon":"fa-solid fa-shirt"},
    {"kategori":"Elektronik", "ikon":"fa-solid fa-plug"},
    {"kategori":"Bahçe ve DIY", "ikon":"fa-solid fa-screwdriver-wrench"},
    {"kategori":"Eğlence", "ikon":"fa-solid fa-masks-theater"},
    {"kategori":"Bakkal Alışveriş", "ikon":"fa-solid fa-basket-shopping"},
    {"kategori":"Oyun", "ikon":"fa-solid fa-gamepad"},
]

products = [
    {"baslik":"Red Dead Redemption PS4","url":"http://google.com", "satici":"Amazon", "fiyat":30, 
    "orjinalFiyat":45,"kargo":"True","kupon":"","goruntu":"https://m.media-amazon.com/images/I/71SyRObF2yL._AC_SL1000_.jpg",
    "ayrintilar":"America, 1899. The end of the Wild West era has begun as lawmen hunt down the last remaining outlaw gangs. Those who will not surrender or succumb are killed.", 
    "kategori":6,"online":"True", "derece":256,
    },
    {"baslik":"Marvel Studios Captain America 4K Ultra-HD Blu-ray Trilogy £27.20 @ Amazon","url":"http://google.com", "satici":"Amazon", "fiyat":27.20, 
    "orjinalFiyat":40,"kargo":"True","kupon":"","goruntu":"https://m.media-amazon.com/images/I/8133x-bYjfL._SL1500_.jpg",
    "ayrintilar":"The First Avenger: Captain America leads the fight for freedom in the action-packed blockbuster starring Chris Evans as the ultimate weapon against evil! When a terrifying force threatens everyone across the globe, the world’s greatest soldier wages war on the evil HYDRA organization, led by the villainous Red Skull (Hugo Weaving, The Matrix).", 
    "kategori":4,"online":"True", "derece":127,
    },
    {"baslik":"Keter Manor Outdoor Garden Storage Shed, Grey, 4 x 3 ft £195.99","url":"http://google.com", "satici":"Amazon", "fiyat":195, 
    "orjinalFiyat":260,"kargo":"True","kupon":"","goruntu":"https://m.media-amazon.com/images/I/91idKRZ3AOL._AC_SL1500_.jpg",
    "ayrintilar":"Keter Manor Outdoor Garden Storage Shed, Grey, 4 x 3 ft for £195.99. Free scheduled delivery. Next best price based on Very", 
    "kategori":3,"online":"True", "derece":165,
    },
    {"baslik":"Grey, Navy & Teal Bicycle Ankle Socks 5 Pack","url":"http://google.com", "satici":"Amazon", "fiyat":4.99, 
    "orjinalFiyat":9,"kargo":"True","kupon":"","goruntu":"https://m.media-amazon.com/images/I/81XzH-XIlKL._AC_UX679_.jpg",
    "ayrintilar":"Bargain Socks here now just £4.50 reduced from £9", 
    "kategori":1,"online":"True", "derece":111,
    },
    {"baslik":"Berghaus Men's Cornice III Interactive Gore-Tex Waterproof Shell Jacket, Durable, Breathable Rain Coat","url":"http://google.com", "satici":"Amazon", "fiyat":30, 
    "orjinalFiyat":45,"kargo":"True","kupon":"","goruntu":"https://m.media-amazon.com/images/I/71ieeK135EL._AC_UX522_.jpg",
    "ayrintilar":"ALL-DAY COMFORT: Come wind, rain, or shine, this has been the jacket of choice for walkers since 1993 Packed full of features for comfort, performance, and extra warmth, you can zip in one of our compatible mid layers, thanks to the interactive zip.", 
    "kategori":1,"online":"True", "derece":250,
    },
    {"baslik":"Fairywill Sonic USB Rechargeable Electric Toothbrush 2 pack with 8 heads for £17.59","url":"http://google.com", "satici":"Amazon", "fiyat":17.59, 
    "orjinalFiyat":30,"kargo":"True","kupon":"","goruntu":"https://m.media-amazon.com/images/I/71-CJK+dmTL._AC_SL1500_.jpg",
    "ayrintilar":"Safe to use in the bath or shower as the toothbrush is rated IPX7 waterproof.", 
    "kategori":5,"online":"True", "derece":183,
    },
]

@staff_member_required
def update_categories(request):
    for i in product_categories:
        Katagoriler.objects.update_or_create(
           kategori = i["kategori"],
           ikon = i["ikon"]
        )

    url = reverse('admin:index')
    return HttpResponseRedirect(url)


@staff_member_required
def add_fake_accounts(request):
    for i in fake_users:
        Kullanici.objects.update_or_create(
            email = i["email"],
            user_name=i["user_name"],
            first_name=i["first_name"],
            password=i["password"]
        )
    
    for i in range(0,len(products)):
        category = Katagoriler.objects.get(id=products[i]["kategori"])
        print(category)
        obj = Maddeler.objects.update_or_create(
            paylasan = Kullanici.objects.order_by('?')[i],
            satici = products[i]["satici"],
            # goruntu = products[i]["goruntu"],
            fiyat = products[i]["fiyat"],
            orjinalFiyat = products[i]["orjinalFiyat"],
            kargo = products[i]["kargo"],
            kupon = products[i]["kupon"],
            baslik = products[i]["baslik"],
            ayrintilar = products[i]["ayrintilar"],
            online = products[i]["online"],
            derece = products[i]["derece"]
        )[0]
        obj.katagori.add(category)
        obj.save()
    url = reverse('admin:index')
    return HttpResponseRedirect(url)

@staff_member_required
def remove_fake_accounts(request):
    for i in fake_users:
        Kullanici.objects.filter(user_name=i["user_name"]).delete()
    
    url = reverse('admin:index')
    return HttpResponseRedirect(url)