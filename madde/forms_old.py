from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from hesaplar.models import Kullanici
from django import forms
from .models import Maddeler, Katagoriler
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


class KuponForm(forms.Form):
    baslik = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Örnek... Bayan elbise %30 indirimli'}))
    ayrintilar = forms.CharField(widget=CKEditorWidget())
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

'''
class DealForm(forms.Form):
    class Meta:
        model = Maddeler
        fields = ['url', 'satici', 'fiyat', 'orjinalFiyat', 'kargo', 'kupon', 'baslik', 'ayrintilar', 'goruntu', 'katagori', 'bas_tarih',
                    'son_tarih', 'online', 'diyar', 'w3w']

    url = forms.URLField(required=False, widget=forms.TextInput(attrs={'placeholder': 'http://www.....'}))
    satici = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Örnek... HepsiBurada'}))
    fiyat = forms.DecimalField(widget=forms.NumberInput(attrs={'placeholder': '99.00'}), min_value=0)
    orjinalFiyat = forms.DecimalField(min_value=0, required=False, widget=forms.NumberInput(attrs={'placeholder': '200.00'}))
    kargo = forms.BooleanField(required=False)
    kupon = forms.CharField(required=False)
    baslik = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Örnek... Bayan elbise %30 indirimli'}))
    ayrintilar = forms.CharField(widget=CKEditorWidget())
    goruntu = forms.ImageField(required=False)
    katagori = forms.ModelChoiceField(
        queryset=Katagoriler.objects.all().order_by('kategori'),
        widget=forms.RadioSelect,
        required=True)
    bas_tarih = forms.DateField(widget=forms.TextInput(attrs={'type': 'date'}),required=False)
    son_tarih = forms.DateField(required=False, widget=forms.TextInput(attrs={'type': 'date'}))
    online = forms.BooleanField(required=False)
    diyar =forms.ChoiceField(choices=SEHIRLER, required=False)
    w3w = forms.CharField(required=False, widget=forms.TextInput(attrs={'placeholder': '///sultan.hurma.hisar'}))


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
            Row(
                InlineRadios('katagori', css_class="custom-control-input")),
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
'''


class DealForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(DealForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.form_class = 'form-horizontal'
        # NEW:
        self.helper.label_class = 'col-sm-2'
        self.helper.field_class = 'col-sm-10'

        self.helper.layout = Layout(
                'baslik',
                'ayrintilar',
                PrependedText('url', '<span class="fas fa-globe"></span>'),
                PrependedText('satici', '<span class="fas fa-store"></span>'),
                Row(
                    Column(PrependedText('fiyat', '<span class="fas fa-lira-sign"></span>'), css_class='form-group offset-md-2 col-md-4 mb-0'),
                    Column(PrependedText('orjinalFiyat', '<span class="fas fa-lira-sign"></span>'), css_class='form-group offset-md-2 col-md-4 mb-0'),
                    css_class='form-row'
                ),
                'kargo',
                'kupon',
                'goruntu',
                'katagori',
                Row(
                    Column('bas_tarih', css_class='form-group offset-md-2 col-md-4 mb-0'),
                    Column('son_tarih', css_class='form-group offset-md-2 col-md-4 mb-0'),
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
    class Meta:
        model = Maddeler
        fields = ['url', 'satici', 'fiyat', 'orjinalFiyat', 'kargo', 'kupon', 'baslik', 'ayrintilar', 'goruntu', 'katagori', 'bas_tarih',
                    'son_tarih', 'online', 'diyar', 'w3w']
        widgets = {
            'baslik':forms.TextInput(attrs={'placeholder': 'Örnek... Bayan elbise %30 indirimli'}),
            'url':forms.URLInput(attrs={'placeholder': 'http://www.....'}),
            'satici': forms.TextInput(attrs={'placeholder': 'Örnek... HepsiBurada'}),
            'bas_tarih':forms.TextInput(attrs={'type': 'date'}),
            'son_tarih':forms.TextInput(attrs={'type': 'date'}),
            'fiyat': forms.NumberInput(attrs={'placeholder': '99.00'}),
            'orjinalFiyat': forms.NumberInput(attrs={'placeholder': '200.00'}),

        }
        '''
        widgets = {
            'baslik': forms.TextInput(
				attrs={'class': 'form-control', 'placeholder': 'Örnek... Bayan elbise %30 indirimli'}),
            'url': forms.URLInput(
				attrs={'class': 'form-control', 'placeholder': 'http://www.....'}),
            'satici': forms.TextInput(
                attrs={'class': 'form-control','placeholder': 'Örnek... HepsiBurada'}),
            'fiyat': forms.NumberInput(attrs={'class': 'form-control','placeholder': '99.00'}),
            'orjinalFiyat': forms.NumberInput(attrs={'class': 'form-control','placeholder': '200.00'}),
            'kargo':forms.BooleanField(),
			}


        url = forms.URLField(required=False, widget=forms.TextInput(attrs={'placeholder': 'http://www.....'}))
        satici = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Örnek... HepsiBurada'}))
        fiyat = forms.IntegerField(widget=forms.NumberInput(attrs={'placeholder': '99.00'}),min_value=0)
        orjinalFiyat = forms.IntegerField(min_value=0, required=False, widget=forms.NumberInput(attrs={'placeholder': '200.00'}))
        kargo = forms.BooleanField(required=False)
        kupon = forms.CharField(required=False)
        baslik = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Örnek... Bayan elbise %30 indirimli'}))
        ayrintilar = forms.CharField(widget=CKEditorWidget())
        goruntu = forms.ImageField(required=False)
        katagori = forms.ModelMultipleChoiceField(
            queryset=Katagoriler.objects,
            widget=forms.CheckboxSelectMultiple,
            required=True)
        bas_tarih = forms.DateField(required=False, widget=forms.TextInput(attrs={'type': 'date'}))
        son_tarih = forms.DateField(required=False, widget=forms.TextInput(attrs={'type': 'date'}))
        online = forms.BooleanField(required=False)
        diyar =forms.ChoiceField(choices=SEHIRLER, required=False)
        w3w = forms.CharField(required=False, widget=forms.TextInput(attrs={'placeholder': '///sultan.hurma.hisar'}))


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
            '''
