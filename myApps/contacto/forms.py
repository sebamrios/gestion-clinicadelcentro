from django import forms
from django.forms import ModelForm
from myApps.contacto.models import Consulta
from django import forms
from captcha.fields import CaptchaField


class ConsultaForm(ModelForm):
    # atributo de captcha por medio de app instalada django-simple-captcha
    captcha = CaptchaField() 

    #atributos heredados del modelo Consulta
    class Meta:
        model = Consulta
        fields = [
            "nombre",
            "descripcion",
            "mail",
            "telefono",
            "estado_respuesta",
            "fecha"
        ]
    # widget para poder estilizar en el html con el form.atributo
        widgets = {
            "nombre": forms.TextInput(attrs={"class": "form-control"}),
            "descripcion": forms.Textarea(attrs={"class": "form-control", "rows": 4}),
            "mail": forms.EmailInput(attrs={"class": "form-control"}),
            "telefono": forms.TextInput(attrs={"class": "form-control"}),
            "estado_respuesta": forms.Select(attrs={"class": "form-control"}),
            "fecha": forms.DateInput(attrs={"class": "form-control", "type": "date"}),
        }

    # Aplicar estilo Bootstrap solo al campo de texto del captcha
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["captcha"].widget.attrs.update({"class": "form-control"})

    #metodo para enviar informacion una vez accedida desde el view
    def send_email(self):
        
        nombre = self.cleaned_data["nombre"]
        descripcion = self.cleaned_data["descripcion"]
        mail = self.cleaned_data["mail"]
        estado_respuesta = self.cleaned_data["estado_respuesta"]
        telefono = self.cleaned_data["telefono"]
        fecha = self.cleaned_data["fecha"]

        #print("enviando datos")
        #print(nombre, descripcion, mail, estado_respuesta, telefono, fecha)