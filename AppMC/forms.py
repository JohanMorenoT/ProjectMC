from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Post, Profile

class SearchForm(forms.Form):
    search = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control text-success' , 'placeholder':'search'}))

class UserRegisterForm(UserCreationForm):
	email = forms.EmailField()
	password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput)
	password2 = forms.CharField(label='Confirma Contraseña', widget=forms.PasswordInput)

	class Meta:
		model = User
		fields = ['username', 'email', 'password1', 'password2']
		help_texts = {k:"" for k in fields }
  
class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['nombres', 'apellidos', 'telefono', 'direccion']
	
class ProfileImageForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image']
        labels = {
            'image': 'Imagen de perfil'
        }
        widgets = {
            'image': forms.ClearableFileInput(attrs={'class': 'form-control-file'})
        }
 
class PostForm(forms.ModelForm):
	description = forms.CharField(label='', widget=forms.Textarea(attrs={'rows':2, 'placeholder': 'Haz una descripción del producto.'}), required=True)

	class Meta:
		model = Post
		fields = ['name','description', 'price', 'image']