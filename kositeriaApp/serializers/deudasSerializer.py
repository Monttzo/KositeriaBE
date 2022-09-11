from kositeriaApp.models.deudas import deudas
from rest_framework import serializers

class deudasSerializer(serializers.ModelSerializer):
    class Meta:
        model = deudas
        fields = ['date', 'detail', 'amount']