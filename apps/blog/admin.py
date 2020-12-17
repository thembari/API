from django.contrib import admin
from .models import BlogPost, Category

models = [BlogPost, Category]
admin.site.register(models)
