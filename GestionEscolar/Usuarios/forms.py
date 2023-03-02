from django import forms

class FormularioRegistrarUsuario(forms.Form):
    nombre = forms.CharField(label='',widget=forms.TextInput(attrs={'class': 'sas','placeholder': 'Nombre de usuario'}))
    email = forms.EmailField(label='',widget=forms.EmailInput(attrs={'class': 'sas','placeholder': 'Correo electrónico'}))
    password = forms.CharField(label='',widget=forms.PasswordInput(attrs={'class': 'sas','placeholder': 'Contraseña'}))


class FormularioLogin(forms.Form):
    email = forms.EmailField(label='',widget=forms.EmailInput(attrs={'class': 'sas','placeholder': 'Correo electrónico'}))
    password = forms.CharField(label='',widget=forms.PasswordInput(attrs={'class': 'sas','placeholder': 'Contraseña'}))