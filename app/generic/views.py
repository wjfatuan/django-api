from django.shortcuts import render

# Create your views here.
from django.urls import path, include
from rest_framework import routers, serializers, viewsets

from .models import Data
from .serializers import DataSerializer

# ViewSets define the view behavior.
class DataViewSet(viewsets.ModelViewSet):
    queryset = Data.objects.all()
    serializer_class = DataSerializer
