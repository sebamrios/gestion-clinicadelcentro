from django.shortcuts import render
from django.views.generic import View
from django.shortcuts import render
from myApps.contacto.models import Consulta
from myApps.contacto.forms import ConsultaForm
from django.views.generic import FormView

# https://docs.djangoproject.com/es/3.2/topics/class-based-views/generic-editing/

# utilizando clases para las vistas 
class Contacto(FormView):

    template_name = "contacto/contacto.html"
    form_class = ConsultaForm
    success_url = "mensaje_enviado"

    def form_valid(self, form):
      
        form.save()
        form.send_email()
        return super().form_valid(form)

# utilizando clases para las vistas 
class MensajeEnviado(View):

    template = "contacto/mensaje_enviado.html"

    def get(self, request):
        form = ConsultaForm()
        params = {}
        params["form"] = form
        return render(request, self.template, params)
