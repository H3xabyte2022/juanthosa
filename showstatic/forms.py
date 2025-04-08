from django import forms
import re
from django.core.validators import EmailValidator
CHOICES =(
    
    ("solicitudes@juanthosa.com", "Solicitud"),
    ("pqrsf@juanthosa.com", "PQRS"),
    ("cotizaciones@juanthosa.com", "Cotizacion"),
  
)

TIPOTRANS =(
     ("Transporte_fluvial", "Transporte Fluvial"),
    ("Transporte_terrestre", "Transporte Terrestre"),
    ("Transporte_aereo", "Transporte Aereo"),
     ("Transporte_combinado", "Transporte Combinado"),
      ("Ninguno", "Ninguno")
   
  
)

class MyEmailValidator(EmailValidator):
    user_regex = re.compile(
    r"(^[-!#$%&'*+/=?^_`{}|~0-9A-Z]+(\.[-!#$%&'*+/=?^_`{}|~0-9A-Z]+)*$"  # dot-atom
    r'|^"([\001-\010\013\014\016-\037!#-\[\]-\177]|\\[\001-\011\013\014\016-\177])*"$)',  # quoted-string
    re.IGNORECASE)


class EmailForm(forms.Form):
    nombre = forms.CharField(max_length=100, label='Nombre completo')
    telefono = forms.CharField(max_length=100, label='Teléfono')
    lugar_destino = forms.CharField(max_length=100, label='Destino', required = False)
    lugar_recogida = forms.CharField(max_length=100, label='Lugar de salida', required = False)
    empresa = forms.CharField(max_length=100, label='Empresa')
    tipo_peticion = forms.ChoiceField(choices = CHOICES, label='Seleccione Tipo de requerimiento', widget=forms.HiddenInput())
    tipo_transporte = forms.ChoiceField(choices = TIPOTRANS, label='Seleccione Tipo de transporte')
    fecha_servicio = forms.DateTimeField(required = False, widget=forms.NumberInput(attrs={'type': 'datetime-local'}))
    cantidad_pasajeros = forms.IntegerField(required = False) 
    peso = forms.IntegerField(label='Peso(Kg)', required = False)
    email = forms.EmailField(label='Correo', validators=[MyEmailValidator()])
    subject = forms.CharField(max_length=100, label='Asunto')
    attach = forms.FileField(widget=forms.ClearableFileInput(attrs={'multiple': True}), label='Adjunto', required = False)
    message = forms.CharField(label='Mensaje', widget=forms.Textarea(attrs={'style': "width:100%;"}))
    