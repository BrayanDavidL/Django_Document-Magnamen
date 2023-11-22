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
    name = models.CharField(max_length=255)
    path = models.FileField(upload_to=document_path, default='')  # Proporciona un valor predeterminado
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    unique_code = models.CharField(max_length=50, unique=True)
    loading_date = models.DateTimeField(auto_now_add=True)
    auth_user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
