from django import forms
from django.forms import ModelForm 
from .models import Mascota
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class MascotaForm(ModelForm):
    class Meta:
        model = Mascota
        fields = ['nombre','sexo','color','esterilizado','cliente','imagen']
        
        
class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField()
    password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Confirma contraseña', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields =['username', 'email','password1','password2']
        help_texts = {k:"" for k in fields}

