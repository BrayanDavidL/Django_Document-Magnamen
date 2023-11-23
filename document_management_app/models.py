# models.py

from django.db import models
from django.contrib.auth.models import User

def document_path(instance, filename):
    return f'documents/{filename}'

class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Document(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255, verbose_name='Nombre')
    path = models.FileField(upload_to=document_path, default='',verbose_name='Documento')  # Proporciona un valor predeterminado
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='Categoria')
    unique_code = models.CharField(max_length=50, unique=True,verbose_name='Codigo')
    loading_date = models.DateTimeField(auto_now_add=True,verbose_name='Fecha')
    auth_user = models.ForeignKey(User, on_delete=models.CASCADE,verbose_name='Usuario')

    def __str__(self):
        return self.name
