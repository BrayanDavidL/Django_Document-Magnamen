from django.contrib import admin
from .models import Category
from .models import Document
# Register your models here.
admin.site.register(Document)
admin.site.register(Category)
