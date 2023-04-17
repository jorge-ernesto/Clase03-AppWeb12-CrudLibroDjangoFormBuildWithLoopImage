from django import forms
from .models import Libro

# El formulario hereda las validaciones definidas en el modelo.
class LibroForm(forms.ModelForm):
    class Meta:
        model=Libro
        fields="__all__"
