from rest_framework import serializers

from .models import Data


class DataSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        """Serializer fields.

        Defines the fields to show when the serializer is used.
        """
        model = Data
        fields = ['id', 'name', 'data']

    data = serializers.JSONField()
