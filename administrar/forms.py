from django import forms
#modelos que necesitan validacion
from .models import Tarea

class TareaForm(forms.ModelForm):
  class Meta:
    model = Tarea
    exclude = []
