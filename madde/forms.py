from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from hesaplar.models import Kullanici
from django import forms
from .models import Maddeler, Katagoriler, Kuponlar
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Row, Column, Div, HTML, Field, ButtonHolder
from crispy_forms.bootstrap import PrependedText, InlineRadios
from ckeditor.widgets import CKEditorWidget


class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['email', 'username', 'first_name', 'last_name', 'password1', 'password2']

class UserEditForm(forms.ModelForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'readonly':'readonly'}))
    email = forms.CharField(widget=forms.TextInput(attrs={'readonly':'readonly'}))
    class Meta:
        model = User
        fields = ['email', 'username', 'first_name', 'last_name']

class ProfileEditForm(forms.ModelForm):
    class Meta:
        model = Kullanici
        exclude = ('kullanici','paylasimlar', 'yorumlar','ensicak','takipciler',)

KATEGORI_SECIMLERI=(
    ('Elektronik','Elektronik'), ('Moda ve aksesuarlar', 'Moda ve aksesuarlar'), ('Bahçe ve DIY','Bahçe ve DIY'),('Kültür ve boş zaman','Kültür ve boş zaman'), ('bakkal alışveriş','bakkal alışveriş'), ('Oyun','Oyun'),
    )

KUPON_CESIT = (('YE','% İndirim'),('Tİ','✂️ İndirimi'),('BK','Bedava Kargo'))

SEHIRLER = (("---","---"),("Adana","Adana"), ("Adıyaman","Adıyaman"), ("Afyonkarahisar","Afyonkarahisar"), ("Ağrı","Ağrı"), ("Aksaray","Aksaray"), ("Amasya","Amasya"), ("Ankara","Ankara"), ("Antalya","Antalya"), ("Ardahan","Ardahan"),
("Artvin","Artvin"), ("Aydın","Aydın"), ("Balıkesir","Balıkesir"), ("Bartın","Bartın"), ("Batman","Batman"), ("Bayburt","Bayburt"), ("Bilecik","Bilecik"), ("Bingöl","Bingöl"), ("Bitlis","Bitlis"), ("Bolu","Bolu"),
("Burdur","Burdur"), ("Bursa","Bursa"), ("Çanakkale","Çanakkale"), ("Çankırı","Çankırı"), ("Çorum","Çorum"), ("Denizli","Denizli"), ("Diyarbakır","Diyarbakır"), ("Düzce","Düzce"), ("Edirne","Edirne"), ("Elazığ","Elazığ"),
("Erzincan","Erzincan"), ("Erzurum","Erzurum"), ("Eskişehir","Eskişehir"), ("Gaziantep","Gaziantep"), ("Giresun","Giresun"), ("Gümüşhane","Gümüşhane"), ("Hakkâri","Hakkâri"), ("Hatay","Hatay"), ("Iğdır","Iğdır"),
("Isparta","Isparta"), ("İstanbul","İstanbul"), ("İzmir","İzmir"), ("Kahramanmaraş","Kahramanmaraş"), ("Karabük","Karabük"), ("Karaman","Karaman"), ("Kars","Kars"), ("Kastamonu","Kastamonu"), ("Kayseri","Kayseri"),
("Kilis","Kilis"), ("Kırıkkale","Kırıkkale"), ("Kırklareli","Kırklareli"), ("Kırşehir","Kırşehir"), ("KKTC - Girne","KKTC - Girne"), ("KKTC - Güzelyurt","KKTC - Güzelyurt"), ("KKTC - İskele","KKTC - İskele"),
("KKTC - Lefkoşa","KKTC - Lefkoşa"), ("KKTC - Mağusa","KKTC - Mağusa"), ("Kocaeli","Kocaeli"), ("Konya","Konya"), ("Kütahya","Kütahya"), ("Malatya","Malatya"), ("Manisa","Manisa"), ("Mardin","Mardin"), ("Mersin","Mersin"),
("Muğla","Muğla"), ("Muş","Muş"), ("Nevşehir","Nevşehir"), ("Niğde","Niğde"), ("Ordu","Ordu"), ("Osmaniye","Osmaniye"), ("Rize","Rize"), ("Sakarya","Sakarya"), ("Samsun","Samsun"), ("Şanlıurfa","Şanlıurfa"),
("Siirt","Siirt"), ("Sinop","Sinop"), ("Şırnak","Şırnak"), ("Sivas","Sivas"), ("Tekirdağ","Tekirdağ"), ("Tokat","Tokat"), ("Trabzon","Trabzon"), ("Tunceli","Tunceli"), ("Uşak","Uşak"), ("Van","Van"),
("Yalova","Yalova"), ("Yozgat","Yozgat"), ("Zonguldak","Zonguldak"))

class KuponForm(forms.ModelForm):
    kuponCesiti = forms.ChoiceField(choices=KUPON_CESIT)
    class Meta:
        model = Kuponlar
        fields = ['baslik', 'ayrintilar', 'url', 'satici', 'kuponCesiti', 'kupon', 'bas_tarih','son_tarih']
        widgets = {
            'bas_tarih': forms.DateInput(format=('%d/%m/%Y'), attrs={'class':'form-control', 'placeholder':'Tarih seçin', 'type':'date'}),
            'son_tarih': forms.DateInput(format=('%d/%m/%Y'), attrs={'class':'form-control', 'placeholder':'Tarih seçin', 'type':'date'}),
        }

class DealForm(forms.ModelForm):
    katagori = forms.ModelChoiceField(queryset=Katagoriler.objects.all(), initial=0)
    diyar = forms.ChoiceField(required=False, choices=SEHIRLER)
    class Meta:
        model = Maddeler
        fields = ['url', 'satici', 'fiyat', 'orjinalFiyat', 'kargo', 'kupon', 'baslik', 'ayrintilar', 'goruntu', 'katagori', 'bas_tarih',
                    'son_tarih', 'online', 'diyar', 'w3w']
        widgets = {
            'bas_tarih': forms.DateInput(format=('%d/%m/%Y'), attrs={'class':'form-control', 'placeholder':'Tarih seçin', 'type':'date'}),
            'son_tarih': forms.DateInput(format=('%d/%m/%Y'), attrs={'class':'form-control', 'placeholder':'Tarih seçin', 'type':'date'}),
        }
