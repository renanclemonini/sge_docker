from rest_framework import serializers
from . import models


class InflowsSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Inflow
        fields = '__all__'
