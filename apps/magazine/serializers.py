from rest_framework import serializers
from .models import *


class IssueModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Issue
        fields = '__all__'

class ContentModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Content
        fields = '__all__'
