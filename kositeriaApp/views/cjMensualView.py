from calendar import isleap
import datetime
from rest_framework import status, views, generics
from rest_framework.response import Response
from kositeriaApp.serializers.cjMensualSerializer import cjMensualSerializer
from kositeriaApp.models.cajaMensual import cajaMensual
import pandas as pd
from kositeriaApp.views.functions import getMonthDay, getMonthDays



"""create a cjMensual row"""
class cjMensualCreateView(views.APIView):
    def post(self, request, *args, **kwargs):

        serializer = cjMensualSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(request.data, status=status.HTTP_201_CREATED)

"""return a Caja row"""
class cjMensuakDetailView(views.APIView):
    queryset = cajaMensual.objects.all()
    serializer_class = cjMensualSerializer
    
    def get(self, request, *args, **kwargs):
        cajaMensual = cajaMensual.objects.get(id=kwargs['id'])
        response = {
            'id': cajaMensual.id,
            'date': cajaMensual.date,
            'month': cajaMensual.month,
            'year': cajaMensual.year,
            'totalSold': cajaMensual.totalSold
        }
        return Response(response, status=status.HTTP_200_OK)

"""return the rows of 'cajaMensual' by month and year"""
class cjMensualMonthView(generics.RetrieveAPIView):
    queryset = cajaMensual.objects.all()
    serializer_class = cjMensualSerializer

    def get(self, request, *args, **kwargs):
        stringResponse = {}
        month = kwargs['month']
        year = kwargs['year']

        cajaM = cajaMensual.objects.get(month=month, year=year)
        stringResponse = {
            'id': cajaM.id,
            'date': cajaM.date,
            'month': cajaM.papeleria,
            'year': cajaM.dulces,
            'totalSold': cajaM.totalSold,
        }
        return Response(stringResponse, status=status.HTTP_200_OK)

"""return the rows of the month's 'Caja' """
class cjMensualYearView(generics.RetrieveAPIView):
    queryset = cajaMensual.objects.all()
    serializer_class = cjMensualSerializer

    def get(self, request, *args, **kwargs):
        stringResponse = {}
        year = kwargs['year']

        for cajaM in cajaMensual.objects.filter(month__gte=1, month__lte=12, year=year).order_by('month'):
            stringResponse[str(cajaM.month)] = {
                'id': cajaM.id,
                'date': cajaM.date,
                'month': cajaM.month,
                'year': cajaM.year,
                'totalSold': cajaM.totalSold
            }
        return Response(stringResponse, status=status.HTTP_200_OK)
        
"""update a cajaMensual row"""
class cjMensualUpdateView(generics.UpdateAPIView):
    queryset = cajaMensual.objects.all()
    serializer_class = cjMensualSerializer

    def put(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)

"""delete a cajaMensual row"""
class cjMensualDeleteView(generics.DestroyAPIView):
    queryset = cajaMensual.objects.all()
    serializer_class = cjMensualSerializer

    def delete(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)