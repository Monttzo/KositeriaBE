from kositeriaApp.models.gastos import gastos
from rest_framework import serializers

class gastosSerializer(serializers.ModelSerializer):
    class Meta:
        model = gastos
        fields = ['date', 'detail', 'amount', 'type']