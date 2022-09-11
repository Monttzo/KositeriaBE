from kositeriaApp.models.cajas import cajas
from rest_framework import serializers

class cajasSerializer(serializers.ModelSerializer):
    class Meta:
        model = cajas
        fields = ['date', 'papeleria', 'dulces', 'cir', 'totalSold']