from rest_framework import serializers

from .models import Data


class DataSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        """
        Defining model and fields to be displayes when the serializer is 
        called.
        """
        model = Data
        fields = ['id', 'name', 'data']

    data = serializers.JSONField()
