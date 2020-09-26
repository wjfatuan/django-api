from rest_framework import serializers

from .models import Data


class DataSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        
        """
        Serializer fields."""

        model = Data
        fields = ['id', 'name', 'data']

    data = serializers.JSONField()
