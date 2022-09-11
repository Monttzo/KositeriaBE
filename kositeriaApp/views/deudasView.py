from calendar import isleap
import datetime
from rest_framework import status, views, generics
from rest_framework.response import Response
from kositeriaApp.serializers.deudasSerializer import deudasSerializer
from kositeriaApp.models.deudas import deudas
import pandas as pd
from kositeriaApp.views.functions import getMonthDay, getMonthDays



"""create a deuda row"""
class deudasCreateView(views.APIView):
    def post(self, request, *args, **kwargs):

        serializer = deudasSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(request.data, status=status.HTTP_201_CREATED)

"""return a Deuda row"""
class deudasDetailView(views.APIView):
    queryset = deudas.objects.all()
    serializer_class = deudasSerializer
    
    def get(self, request, *args, **kwargs):
        deuda = deudas.objects.get(id=kwargs['id'])
        response = {
            'id': deuda.id,
            'date': deuda.date,
            'detail': deuda.detail,
            'amount': deuda.amount
        }
        return Response(response, status=status.HTTP_200_OK)

"""return the rows of the week's 'Deuda'"""
class deudasDetailWeekView(generics.RetrieveAPIView):
    queryset = deudas.objects.all()
    serializer_class = deudasSerializer

    def get(self, request, *args, **kwargs):
        stringResponse = {}
        Date = pd.Timestamp(kwargs['date'])
        year = int(Date.strftime('%Y'))
        month = int(Date.strftime('%m'))
        day = int(Date.strftime('%d'))
        weekday = int(Date.strftime('%w'))

        initDay = day - weekday
        finalDay = day + (7 - weekday)

        initDate = getMonthDay(month, year, initDay)
        finalDate = getMonthDay(month, year, finalDay)
        for deuda in deudas.objects.filter(date__gt=initDate, date__lte=finalDate).order_by('date'):
            temp = pd.Timestamp(deuda.date)
            stringResponse[format(deuda.date) + ' ' + str(deuda.id)] = {
                'id': deuda.id,
                'date': deuda.date,
                'detail': deuda.detail,
                'amount': deuda.amount,
                'dayNumber': str(temp.day_of_week),
                'dayName': temp.day_name()
            }
        return Response(stringResponse, status=status.HTTP_200_OK)

"""return the rows of the month's 'Deuda' """
class deudasDetailMonthView(generics.RetrieveAPIView):
    queryset = deudas.objects.all()
    serializer_class = deudasSerializer

    def get(self, request, *args, **kwargs):
        stringResponse = {}
        Date = pd.Timestamp(kwargs['date'])
        year = int(Date.strftime('%Y'))
        month = int(Date.strftime('%m'))

        initDate = getMonthDay(month,year,1)
        finalDate = getMonthDay(month,year,getMonthDays(month,year))
        for deuda in deudas.objects.filter(date__gte=initDate, date__lte=finalDate).order_by('date'):
            temp = pd.Timestamp(deuda.date)
            stringResponse[format(deuda.date) + ' ' + str(deuda.id)] = {
                'id': deuda.id,
                'date': deuda.date,
                'detail': deuda.detail,
                'amount': deuda.amount,
                'dayNumber': str(temp.day_of_week),
                'dayName': temp.day_name()
            }
        return Response(stringResponse, status=status.HTTP_200_OK)
        
"""update a Deuda row"""
class deudasUpdateView(generics.UpdateAPIView):
    queryset = deudas.objects.all()
    serializer_class = deudasSerializer

    def put(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)

"""delete a Deuda row"""
class deudasDeleteView(generics.DestroyAPIView):
    queryset = deudas.objects.all()
    serializer_class = deudasSerializer

    def delete(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)