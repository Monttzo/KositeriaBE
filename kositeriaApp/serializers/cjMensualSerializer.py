from kositeriaApp.models.cajaMensual import cajaMensual
from rest_framework import serializers

class cjMensualSerializer(serializers.ModelSerializer):
    class Meta:
        model = cajaMensual
        fields = ['date', 'month', 'totalSold', 'year']