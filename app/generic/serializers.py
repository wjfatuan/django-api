from django.urls import path, include
from rest_framework import routers, serializers, viewsets

from .models import Data

# Serializers define the API representation.
class DataSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Data
        fields = ['id','name', 'data']
