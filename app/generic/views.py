from rest_framework import viewsets

from .models import Data
from .serializers import DataSerializer

# ViewSets define the view behavior.
class DataViewSet(viewsets.ModelViewSet):
    queryset = Data.objects.all()
    serializer_class = DataSerializer
