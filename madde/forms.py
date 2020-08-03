from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import Maddeler

class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['email', 'username', 'first_name', 'last_name', 'password1', 'password2']

class DealForm(ModelForm):
    class Meta:
        model = Maddeler
        #bas_tarih = forms.DateTimeField(input_formats=['%d/%m/%Y'])
        #son_tarih = forms.DateTimeField(input_formats=['%d/%m/%Y'])
        #bas_tarih = forms.DateField(widget=forms.TextInput(attrs={'type': 'date'}))
        #son_tarih = forms.DateField(widget=forms.TextInput(attrs={'type': 'date'}))
        fields = ('url','satici','fiyat','orjinalFiyat','kargo','kupon','baslik','ayrintilar','goruntu','katagori','bas_tarih','son_tarih','online','diyar','w3w')
        exclude = ('paylasan', 'derece', 'duyurmaTarihi', 'kaynamavakti', 'aktif', 'oylar')

        widgets = {
            'url': forms.TextInput(attrs={'placeholder': 'http://www.'}),
            'satici':forms.TextInput(attrs={'placeholder':'Örnek... HepsiBurada'}),
            'fiyat': forms.TextInput(attrs={'placeholder': '99.00'}),
            'baslik': forms.TextInput(attrs={'placeholder': 'Örnek... Bayan elbise %30 indirimli'}),
            'ayrintilar': forms.TextInput(attrs={'placeholder': 'Kelepiri kendi sözlerinizle anlatın ve neden kaçılmaz fırsat olduğunu başkalarına açıklayın.'}),
            'bas_tarih': forms.DateField(widget=forms.TextInput(attrs={'type': 'date'})),
            'son_tarih': forms.DateField(widget=forms.TextInput(attrs={'type': 'date'})),
            'w3w': forms.TextInput(attrs={'placeholder': '///susma.hurma.eşyalı'}),
        }
