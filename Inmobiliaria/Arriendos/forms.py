from django import forms
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth import password_validation 
from django.core.exceptions import ValidationError

from .models import User

class RegisterModelForm(UserCreationForm):
    username = forms.CharField(
    label='Nombre de usuario',
    widget=forms.TextInput(attrs={'placeholder': 'Ingrese su nombre de usuario'}),
)
    password1 = forms.CharField(
        label='Contraseña',
        strip=False,
        widget=forms.PasswordInput(attrs={'placeholder': 'Ingrese su contraseña'}),
        help_text=password_validation.password_validators_help_text_html(),
    )
    password2 = forms.CharField(
        label='Confirmar contraseña',
        widget=forms.PasswordInput(attrs={'placeholder': 'Confirme su contraseña'}),
        strip=False,
        help_text='Ingrese la misma contraseña que antes, para su verificación.',
    )
    tipo_usuario = forms.ChoiceField(
        label='Tipo de usuario',
        choices=[('arrendatario', 'Arrendatario'), ('arrendador', 'Arrendador')],
        widget=forms.Select(attrs={'placeholder': 'Seleccione su tipo de usuario'}),
    )
    
    rut = forms.CharField(
        label='Rut',
        widget=forms.TextInput(attrs={'placeholder': 'Ingrese su rut'}),
    )
    nombres = forms.CharField(
        label='Nombres',
        widget=forms.TextInput(attrs={'placeholder': 'Ingrese sus nombres'}),
    )
    apellidos = forms.CharField(
        label='Apellidos',
        widget=forms.TextInput(attrs={'placeholder': 'Ingrese sus apellidos'}),
    )
    direccion = forms.CharField(
        label='Direccion',
        widget=forms.TextInput(attrs={'placeholder': 'Ingrese su domicilio'}),
    )
    telefono_personal = forms.CharField(
        label='Telefono personal',
        widget=forms.TextInput(attrs={'placeholder': 'Ingrese su telefono personal'}),
    )
    correo_electronico = forms.EmailField(
        label='Correo electronico',
        widget=forms.EmailInput(attrs={'placeholder': 'Ingrese su correo electronico'}),
    )
    
    class Meta:
        model = User
        fields = ['username','password1', 'password2','tipo_usuario', 'rut', 'nombres', 'apellidos', 'direccion', 'telefono_personal', 'correo_electronico' ]
    def clean_rut(self):
        rut = self.cleaned_data.get('rut')
        if User.objects.filter(rut=rut).exists():
            raise ValidationError("Rut already exists")
        return rut

    def clean_correo_electronico(self):
        correo_electronico = self.cleaned_data.get('correo_electronico')
        if User.objects.filter(correo_electronico=correo_electronico).exists():
            raise ValidationError("Email already exists")
        return correo_electronico

    def save(self, commit=True):
        user = super().save(commit=False)
        user.username = self.cleaned_data['username']
        user.tipo_usuario = self.cleaned_data['tipo_usuario']
        user.rut = self.cleaned_data['rut']
        user.nombres = self.cleaned_data['nombres']
        user.apellidos = self.cleaned_data['apellidos']
        user.direccion = self.cleaned_data['direccion']
        user.telefono_personal = self.cleaned_data['telefono_personal']
        user.correo_electronico = self.cleaned_data['correo_electronico']
        if commit:
            user.save()
        return user
        
class CustomAuthenticationForm(AuthenticationForm):
    username = forms.CharField(
        label='',
        widget=forms.TextInput(attrs={'placeholder': 'Nombre de usuario'}),
)
    password = forms.CharField(
        label='',
        widget=forms.PasswordInput(attrs={'placeholder': 'Ingrese su contraseña'}),
    )
class UserUpdateForm(forms.ModelForm):
    tipo_usuario = forms.ChoiceField(
        label='Tipo de usuario',
        choices=[('arrendatario', 'Arrendatario'), ('arrendador', 'Arrendador')],
        widget=forms.Select(attrs={'placeholder': 'Seleccione su tipo de usuario'}),
    )
    
    rut = forms.CharField(
        label='Rut',
        widget=forms.TextInput(attrs={'placeholder': 'Ingrese su rut'}),
    )
    nombres = forms.CharField(
        label='Nombres',
        widget=forms.TextInput(attrs={'placeholder': 'Ingrese sus nombres'}),
    )
    apellidos = forms.CharField(
        label='Apellidos',
        widget=forms.TextInput(attrs={'placeholder': 'Ingrese sus apellidos'}),
    )
    direccion = forms.CharField(
        label='Direccion',
        widget=forms.TextInput(attrs={'placeholder': 'Ingrese su domicilio'}),
    )
    telefono_personal = forms.CharField(
        label='Telefono personal',
        widget=forms.TextInput(attrs={'placeholder': 'Ingrese su telefono personal'}),
    )
    correo_electronico = forms.EmailField(
        label='Correo electronico',
        widget=forms.EmailInput(attrs={'placeholder': 'Ingrese su correo electronico'}),
    )
    
    class Meta:
        model = User
        fields = ['tipo_usuario', 'rut', 'nombres', 'apellidos', 'direccion', 'telefono_personal', 'correo_electronico']
