from django import forms
from .models import Document, Category

class DocumentForm(forms.ModelForm):
    # Agrega un campo de selección para las categoríasa
    
    category = forms.ModelChoiceField(
        queryset=Category.objects.all(),
        empty_label="Selecciona una categoría",
        widget=forms.Select(attrs={'class': 'form-label form-control'})
    )
    class Meta:
        model = Document
        fields = ['name', 'path', 'category']

    # Personaliza la inicialización del formulario
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Puedes personalizar las etiquetas de los campos si lo deseas
        self.fields['name'].label = "Nombre del Documento"
        self.fields['path'].label = "Archivo"
        self.fields['category'].label = "Categoría"
