from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import Maddeler, Katagoriler
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Row, Column
from crispy_forms.bootstrap import PrependedText

class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['email', 'username', 'first_name', 'last_name', 'password1', 'password2']

KATEGORI_SECIMLERI=(
    ('Elektronik','Elektronik'), ('Moda ve aksesuarlar', 'Moda ve aksesuarlar'), ('Bahçe ve DIY','Bahçe ve DIY'),('Kültür ve boş zaman','Kültür ve boş zaman'), ('bakkal alışveriş','bakkal alışveriş'), ('Oyun','Oyun'),
    )

KUPON_CESIT = (('YE','% İndirim'),('Tİ','✂️ İndirimi'),('BK','Bedava Kargo'))

SEHIRLER = (("Adana","Adana"), ("Adıyaman","Adıyaman"), ("Afyonkarahisar","Afyonkarahisar"), ("Ağrı","Ağrı"), ("Aksaray","Aksaray"), ("Amasya","Amasya"), ("Ankara","Ankara"), ("Antalya","Antalya"), ("Ardahan","Ardahan"),
("Artvin","Artvin"), ("Aydın","Aydın"), ("Balıkesir","Balıkesir"), ("Bartın","Bartın"), ("Batman","Batman"), ("Bayburt","Bayburt"), ("Bilecik","Bilecik"), ("Bingöl","Bingöl"), ("Bitlis","Bitlis"), ("Bolu","Bolu"),
("Burdur","Burdur"), ("Bursa","Bursa"), ("Çanakkale","Çanakkale"), ("Çankırı","Çankırı"), ("Çorum","Çorum"), ("Denizli","Denizli"), ("Diyarbakır","Diyarbakır"), ("Düzce","Düzce"), ("Edirne","Edirne"), ("Elazığ","Elazığ"),
("Erzincan","Erzincan"), ("Erzurum","Erzurum"), ("Eskişehir","Eskişehir"), ("Gaziantep","Gaziantep"), ("Giresun","Giresun"), ("Gümüşhane","Gümüşhane"), ("Hakkâri","Hakkâri"), ("Hatay","Hatay"), ("Iğdır","Iğdır"),
("Isparta","Isparta"), ("İstanbul","İstanbul"), ("İzmir","İzmir"), ("Kahramanmaraş","Kahramanmaraş"), ("Karabük","Karabük"), ("Karaman","Karaman"), ("Kars","Kars"), ("Kastamonu","Kastamonu"), ("Kayseri","Kayseri"),
("Kilis","Kilis"), ("Kırıkkale","Kırıkkale"), ("Kırklareli","Kırklareli"), ("Kırşehir","Kırşehir"), ("KKTC - Girne","KKTC - Girne"), ("KKTC - Güzelyurt","KKTC - Güzelyurt"), ("KKTC - İskele","KKTC - İskele"),
("KKTC - Lefkoşa","KKTC - Lefkoşa"), ("KKTC - Mağusa","KKTC - Mağusa"), ("Kocaeli","Kocaeli"), ("Konya","Konya"), ("Kütahya","Kütahya"), ("Malatya","Malatya"), ("Manisa","Manisa"), ("Mardin","Mardin"), ("Mersin","Mersin"),
("Muğla","Muğla"), ("Muş","Muş"), ("Nevşehir","Nevşehir"), ("Niğde","Niğde"), ("Ordu","Ordu"), ("Osmaniye","Osmaniye"), ("Rize","Rize"), ("Sakarya","Sakarya"), ("Samsun","Samsun"), ("Şanlıurfa","Şanlıurfa"),
("Siirt","Siirt"), ("Sinop","Sinop"), ("Şırnak","Şırnak"), ("Sivas","Sivas"), ("Tekirdağ","Tekirdağ"), ("Tokat","Tokat"), ("Trabzon","Trabzon"), ("Tunceli","Tunceli"), ("Uşak","Uşak"), ("Van","Van"),
("Yalova","Yalova"), ("Yozgat","Yozgat"), ("Zonguldak","Zonguldak"))


class KuponForm(forms.Form):
    baslik = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Örnek... Bayan elbise %30 indirimli'}))
    ayrintilar = forms.CharField(widget=forms.TextInput())
    url = forms.URLField(widget=forms.TextInput(attrs={'placeholder': 'http://www.....'}))
    satici = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Örnek... HepsiBurada'}))
    kuponCesiti = forms.ChoiceField(choices=KUPON_CESIT)
    kupon = forms.CharField(widget=forms.TextInput())
    bas_tarih = forms.DateField(widget=forms.TextInput(attrs={'type': 'date'}))
    son_tarih = forms.DateField(widget=forms.TextInput(attrs={'type': 'date'}))

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            'baslik',
            'ayrintilar',
            PrependedText('url', '<span class="fas fa-globe"></span>'),
            PrependedText('satici', '<span class="fas fa-store"></span>'),
            'kuponCesiti',
            PrependedText('kupon', '<span class="fas fa-hand-scissors></span>'),
            Row(
                Column('bas_tarih', css_class='form-group col-md-6 mb-0'),
                Column('son_tarih', css_class='form-group col-md-6 mb-0'),
                css_class='form-row'
            ),

            Submit('submit','Kuponu Paylaş')
        )


class DealForm(forms.Form):
    url = forms.URLField(widget=forms.TextInput(attrs={'placeholder': 'http://www.....'}))
    satici = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Örnek... HepsiBurada'}))
    fiyat = forms.IntegerField(widget=forms.NumberInput(attrs={'placeholder': '99.00'}),min_value=0)
    orjinalFiyat = forms.IntegerField(min_value=0, widget=forms.NumberInput(attrs={'placeholder': '200.00'}))
    kargo = forms.BooleanField(required=False)
    kupon = forms.CharField()
    baslik = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Örnek... Bayan elbise %30 indirimli'}))
    ayrintilar = forms.TextInput()
    goruntu = forms.ImageField()
    katagori = forms.ModelMultipleChoiceField(
        queryset=Katagoriler.objects,
        widget=forms.CheckboxSelectMultiple,
        required=True)
    bas_tarih = forms.DateField(widget=forms.TextInput(attrs={'type': 'date'}))
    son_tarih = forms.DateField(widget=forms.TextInput(attrs={'type': 'date'}))
    online = forms.BooleanField(required=False)
    diyar =forms.ChoiceField(choices=SEHIRLER)
    w3w = forms.CharField(widget=forms.TextInput(attrs={'placeholder': '///sultan.hurma.hisar'}))


    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            'baslik',
            'ayrintilar',
            PrependedText('url', '<span class="fas fa-globe"></span>'),
            PrependedText('satici', '<span class="fas fa-store"></span>'),
            Row(
                Column(PrependedText('fiyat', '<span class="fas fa-lira-sign"></span>'), css_class='form-group col-md-3 mb-0'),
                Column(PrependedText('orjinalFiyat', '<span class="fas fa-lira-sign"></span>'), css_class='form-group col-md-3 mb-0'),
                css_class='form-row'
            ),
            'kargo',
            'kupon',
            'goruntu',
            'katagori',
            Row(
                Column('bas_tarih', css_class='form-group col-md-6 mb-0'),
                Column('son_tarih', css_class='form-group col-md-6 mb-0'),
                css_class='form-row'
            ),
            Row(
                Column('online', css_class='form-group col-md-6 mb-0'),
                Column('diyar', css_class='form-group col-md-6 mb-0'),
                css_class='form-row'
            ),
            'w3w',
            Submit('submit','Kelepiri Paylaş')
        )
