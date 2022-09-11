from calendar import isleap
import datetime
from rest_framework import status, views, generics
from rest_framework.response import Response
from kositeriaApp.serializers.cajasSerializer import cajasSerializer
from kositeriaApp.models.cajas import cajas
import pandas as pd
from kositeriaApp.views.functions import getMonthDay, getMonthDays



"""create a caja row"""
class cajasCreateView(views.APIView):
    def post(self, request, *args, **kwargs):

        serializer = cajasSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(request.data, status=status.HTTP_201_CREATED)

"""return a Caja row"""
class cajasDetailView(views.APIView):
    queryset = cajas.objects.all()
    serializer_class = cajasSerializer
    
    def get(self, request, *args, **kwargs):
        caja = cajas.objects.get(id=kwargs['id'])
        response = {
            'id': caja.id,
            'date': caja.date,
            'papeleria': caja.papeleria,
            'dulces': caja.dulces,
            'cir': caja.cir,
            'totalSold': caja.totalSold
        }
        return Response(response, status=status.HTTP_200_OK)

"""return the rows of the week's 'Caja'"""
class cajasDetailWeekView(generics.RetrieveAPIView):
    queryset = cajas.objects.all()
    serializer_class = cajasSerializer

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

        for caja in cajas.objects.filter(date__gt=initDate, date__lte=finalDate).order_by('date'):
            temp = pd.Timestamp(caja.date)
            stringResponse[format(caja.date) + ' ' + str(caja.id)] = {
                'id': caja.id,
                'date': caja.date,
                'papeleria': caja.papeleria,
                'dulces': caja.dulces,
                'cir': caja.cir,
                'totalSold': caja.totalSold,
                'dayNumber': str(temp.day_of_week),
                'dayName': temp.day_name()
            }
        return Response(stringResponse, status=status.HTTP_200_OK)

"""return the rows of the month's 'Caja' """
class cajasDetailMonthView(generics.RetrieveAPIView):
    queryset = cajas.objects.all()
    serializer_class = cajasSerializer

    def get(self, request, *args, **kwargs):
        stringResponse = {}
        Date = pd.Timestamp(kwargs['date'])
        year = int(Date.strftime('%Y'))
        month = int(Date.strftime('%m'))

        initDate = getMonthDay(month,year,1)
        finalDate = getMonthDay(month,year,getMonthDays(month,year))

        for caja in cajas.objects.filter(date__gte=initDate, date__lte=finalDate).order_by('date'):
            temp = pd.Timestamp(caja.date)
            stringResponse[format(caja.date) + ' ' + str(caja.id)] = {
                'id': caja.id,
                'date': caja.date,
                'papeleria': caja.papeleria,
                'dulces': caja.dulces,
                'cir': caja.cir,
                'totalSold': caja.totalSold,
                'dayNumber': str(temp.day_of_week),
                'dayName': temp.day_name()
            }
        return Response(stringResponse, status=status.HTTP_200_OK)
        
"""update a Caja row"""
class cajasUpdateView(generics.UpdateAPIView):
    queryset = cajas.objects.all()
    serializer_class = cajasSerializer

    def put(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)

"""delete a Caja row"""
class cajasDeleteView(generics.DestroyAPIView):
    queryset = cajas.objects.all()
    serializer_class = cajasSerializer

    def delete(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)