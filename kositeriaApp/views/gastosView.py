from calendar import isleap
import datetime
from rest_framework import status, views, generics
from rest_framework.response import Response
from kositeriaApp.serializers.gastosSerializer import gastosSerializer
from kositeriaApp.models.gastos import gastos
import pandas as pd
from kositeriaApp.views.functions import getMonthDay, getMonthDays

"""create a gasto row"""
class gastosCreateView(views.APIView):
    def post(self, request, *args, **kwargs):

        serializer = gastosSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(request.data, status=status.HTTP_201_CREATED)

"""return a gasto row"""
class gastosDetailView(views.APIView):
    queryset = gastos.objects.all()
    serializer_class = gastosSerializer
    
    def get(self, request, *args, **kwargs):
        gasto = gastos.objects.get(id=kwargs['id'])
        response = {
            'id': gasto.id,
            'date': gasto.date,
            'type': gasto.type,
            'detail': gasto.detail,
            'amount': gasto.amount,
        }
        return Response(response, status=status.HTTP_200_OK)

"""return the rows of the week's 'Gasto'"""
class gastosDetailWeekView(generics.RetrieveAPIView):
    queryset = gastos.objects.all()
    serializer_class = gastosSerializer

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

        for gasto in gastos.objects.filter(date__gt=initDate, date__lte=finalDate).order_by('date'):
            temp = pd.Timestamp(gasto.date)
            stringResponse[format(gasto.date) + ' ' + str(gasto.id)] = {
                'id': gasto.id,
                'date': gasto.date,
                'type': gasto.type,
                'detail': gasto.detail,
                'amount': gasto.amount,
                'dayNumber': str(temp.day_of_week),
                'dayName': temp.day_name()
            }
        return Response(stringResponse, status=status.HTTP_200_OK)

"""return the rows of the week's 'Gasto' by type"""
class gastosDetailWeekTypeView(generics.RetrieveAPIView):
    queryset = gastos.objects.all()
    serializer_class = gastosSerializer

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

        for gasto in gastos.objects.filter(date__gt=initDate, date__lte=finalDate, type=kwargs['type']).order_by('date'):
            temp = pd.Timestamp(gasto.date)
            stringResponse[format(gasto.date) + ' ' + str(gasto.id)] = {
                'id': gasto.id,
                'date': gasto.date,
                'type': gasto.type,
                'detail': gasto.detail,
                'amount': gasto.amount,
                'dayNumber': str(temp.day_of_week),
                'dayName': temp.day_name()
            }
        return Response(stringResponse, status=status.HTTP_200_OK)

"""return the rows of the month's 'Gasto' """
class gastosDetailMonthView(generics.RetrieveAPIView):
    queryset = gastos.objects.all()
    serializer_class = gastosSerializer

    def get(self, request, *args, **kwargs):
        stringResponse = {}
        Date = pd.Timestamp(kwargs['date'])
        year = int(Date.strftime('%Y'))
        month = int(Date.strftime('%m'))

        initDate = getMonthDay(month,year,1)
        finalDate = getMonthDay(month,year,getMonthDays(month,year))

        for gasto in gastos.objects.filter(date__gte=initDate, date__lte=finalDate).order_by('date'):
            temp = pd.Timestamp(gasto.date)
            stringResponse[format(gasto.date) + ' ' + str(gasto.id)] = {
                'id': gasto.id,
                'date': gasto.date,
                'type': gasto.type,
                'detail': gasto.detail,
                'amount': gasto.amount,
                'dayNumber': str(temp.day_of_week),
                'dayName': temp.day_name()
            }
        return Response(stringResponse, status=status.HTTP_200_OK)

"""return the rows of the month's 'Gasto' by type"""
class gastosDetailMonthTypeView(generics.RetrieveAPIView):
    queryset = gastos.objects.all()
    serializer_class = gastosSerializer

    def get(self, request, *args, **kwargs):
        stringResponse = {}
        Date = pd.Timestamp(kwargs['date'])
        year = int(Date.strftime('%Y'))
        month = int(Date.strftime('%m'))

        initDate = getMonthDay(month,year,1)
        finalDate = getMonthDay(month,year,getMonthDays(month,year))

        for gasto in gastos.objects.filter(date__gte=initDate, date__lte=finalDate, type=kwargs['type']).order_by('date'):
            temp = pd.Timestamp(gasto.date)
            stringResponse[format(gasto.date) + ' ' + str(gasto.id)] = {
                'id': gasto.id,
                'date': gasto.date,
                'type': gasto.type,
                'detail': gasto.detail,
                'amount': gasto.amount,
                'dayNumber': str(temp.day_of_week),
                'dayName': temp.day_name()
            }
        return Response(stringResponse, status=status.HTTP_200_OK)

"""update a Gasto row"""
class gastosUpdateView(generics.UpdateAPIView):
    queryset = gastos.objects.all()
    serializer_class = gastosSerializer

    def put(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)

"""delete a Gasto row"""
class gastosDeleteView(generics.DestroyAPIView):
    queryset = gastos.objects.all()
    serializer_class = gastosSerializer

    def delete(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)