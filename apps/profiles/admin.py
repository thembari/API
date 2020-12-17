from django.contrib import admin
from .models import Contributor_Profile, Reader_Profile

models = [Contributor_Profile, Reader_Profile]
admin.site.register(models)
