from django.contrib import admin
from .models import *

models = [Issue, Content]
admin.site.register(models)
