from django import forms
from .models import Persona
from django.core.exceptions import ValidationError
from django.contrib import auth

class PersonaModelForm(forms.ModelForm):
	password = forms.CharField(min_length=8, widget=forms.PasswordInput())
	confirmarPassword = forms.CharField(min_length=8, widget=forms.PasswordInput())

	class Meta:
		model = Persona
		fields = '__all__'
		labels = {
            'tipoDocumento':'Tipo de Documento',
            'fechaNacimiento':'Fecha de Nacimiento',
            'lugarResidencia':'Lugar de Residencia',
        }

	def clean_nombres(self):
		nombres = self.cleaned_data.get('nombres')
		if len(nombres) > 25:
			raise ValidationError('El nombre no debe exceder los 25 caracteres')
		return nombres

	def clean_apellidos(self):
		apellidos = self.cleaned_data.get('apellidos')
		if len(apellidos) > 25:
			raise ValidationError('Los apellidos no deben exceder los 25 caracteres')
		return apellidos

	def clean_email(self):
		email = self.cleaned_data.get('email')
		if len(email) > 120:
			raise ValidationError('El email no debe exceder los 120 caracteres')
		return email

	def clean_usuario(self):
		usuario = self.cleaned_data.get('usuario')
		if len(usuario) > 10:
			raise ValidationError('El usuario no debe exceder los 10 caracteres')
		return usuario

	def clean(self):
		if self.cleaned_data.get('password') != self.cleaned_data.get('confirmarPassword'):
			raise ValidationError('Las contraseñas no coinciden')
		return self.cleaned_data