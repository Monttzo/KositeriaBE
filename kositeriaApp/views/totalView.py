from calendar import isleap
import datetime
from pprint import pprint
from rest_framework import status, views, generics
from rest_framework.response import Response
from kositeriaApp.serializers.cajasSerializer import cajasSerializer
from kositeriaApp.models.cajas import cajas
import pandas as pd
from kositeriaApp.views.functions import getMonthDay, getMonthDays
from django.db.models import Sum
from kositeriaApp.serializers.gastosSerializer import gastosSerializer
from kositeriaApp.models.gastos import gastos
from kositeriaApp.serializers.deudasSerializer import deudasSerializer
from kositeriaApp.models.deudas import deudas
from kositeriaApp.serializers.cjMensualSerializer import cjMensualSerializer
from kositeriaApp.models.cajaMensual import cajaMensual

class totalWeekPapeleriaView(generics.RetrieveAPIView):
    queryset = cajas.objects.all()
    serializer_class = cajasSerializer

    def get(self, request, *args, **kwargs):
        Date = pd.Timestamp(kwargs['date'])
        year = int(Date.strftime('%Y'))
        month = int(Date.strftime('%m'))
        day = int(Date.strftime('%d'))
        weekday = int(Date.strftime('%w'))

        initDay = day - weekday
        finalDay = day + (7 - weekday)

        initDate = getMonthDay(month, year, initDay)
        finalDate = getMonthDay(month, year, finalDay)

        totalCajaPapeleria = cajas.objects.filter(date__gt=initDate, date__lte=finalDate).order_by('date').aggregate(Sum('papeleria'))
        papeleria = 0 if totalCajaPapeleria['papeleria__sum'] == None else totalCajaPapeleria['papeleria__sum']

        totalGastosInventario = gastos.objects.filter(date__gt=initDate, date__lte=finalDate,type='inventario').order_by('date').aggregate(Sum('amount'))
        inventario = 0 if totalGastosInventario['amount__sum'] == None else totalGastosInventario['amount__sum']

        totalGastosVarios = gastos.objects.filter(date__gt=initDate, date__lte=finalDate,type='varios').order_by('date').aggregate(Sum('amount'))
        varios = 0 if totalGastosVarios['amount__sum'] == None else totalGastosVarios['amount__sum']

        papeleriaWithoutGastos = papeleria - inventario - varios

        initialDate = pd.Timestamp(initDate)
        initialyear = int(initialDate.strftime('%Y'))
        initialmonth = int(initialDate.strftime('%m'))
        initialday = int(initialDate.strftime('%d')) + 1
        
        initialDate = getMonthDay(initialmonth, initialyear, initialday)

        stringResponse = {
            'papeleria': papeleria,
            'inventario': inventario,
            'varios': varios,
            'papeleriaWithoutgastos': papeleriaWithoutGastos,
            'initialDate': initialDate,
            'finalDate': finalDate
        }
        return Response(stringResponse, status=status.HTTP_200_OK)

class totalWeekDulcesView(generics.RetrieveAPIView):
    queryset = cajas.objects.all()
    serializer_class = cajasSerializer

    def get(self, request, *args, **kwargs):
        Date = pd.Timestamp(kwargs['date'])
        year = int(Date.strftime('%Y'))
        month = int(Date.strftime('%m'))
        day = int(Date.strftime('%d'))
        weekday = int(Date.strftime('%w'))

        initDay = day - weekday
        finalDay = day + (7 - weekday)

        initDate = getMonthDay(month, year, initDay)
        finalDate = getMonthDay(month, year, finalDay)

        totalCajaDulces = cajas.objects.filter(date__gt=initDate, date__lte=finalDate).order_by('date').aggregate(Sum('dulces'))
        dulces = 0 if totalCajaDulces['dulces__sum'] == None else totalCajaDulces['dulces__sum']

        totalGastosDulces = gastos.objects.filter(date__gt=initDate, date__lte=finalDate,type='dulces').order_by('date').aggregate(Sum('amount'))
        Gdulces = 0 if totalGastosDulces['amount__sum'] == None else totalGastosDulces['amount__sum']

        dulcesWithoutGastos = dulces - Gdulces

        initialDate = pd.Timestamp(initDate)
        initialyear = int(initialDate.strftime('%Y'))
        initialmonth = int(initialDate.strftime('%m'))
        initialday = int(initialDate.strftime('%d')) + 1
        
        initialDate = getMonthDay(initialmonth, initialyear, initialday)

        stringResponse = {
            'dulces': dulces,
            'Gdulces': Gdulces,
            'dulcesWithoutgastos': dulcesWithoutGastos,
            'initialDate': initialDate,
            'finalDate': finalDate
        }
        return Response(stringResponse, status=status.HTTP_200_OK)

class totalWeekCirView(generics.RetrieveAPIView):
    queryset = cajas.objects.all()
    serializer_class = cajasSerializer

    def get(self, request, *args, **kwargs):
        Date = pd.Timestamp(kwargs['date'])
        year = int(Date.strftime('%Y'))
        month = int(Date.strftime('%m'))
        day = int(Date.strftime('%d'))
        weekday = int(Date.strftime('%w'))

        initDay = day - weekday
        finalDay = day + (7 - weekday)

        initDate = getMonthDay(month, year, initDay)
        finalDate = getMonthDay(month, year, finalDay)

        totalCajaCir = cajas.objects.filter(date__gt=initDate, date__lte=finalDate).order_by('date').aggregate(Sum('cir'))
        cir = 0 if totalCajaCir['cir__sum'] == None else totalCajaCir['cir__sum']

        totalGastosPlataforma = gastos.objects.filter(date__gt=initDate, date__lte=finalDate,type='plataforma').order_by('date').aggregate(Sum('amount'))
        plataforma = 0 if totalGastosPlataforma['amount__sum'] == None else totalGastosPlataforma['amount__sum']

        cirWithoutGastos = cir - plataforma

        initialDate = pd.Timestamp(initDate)
        initialyear = int(initialDate.strftime('%Y'))
        initialmonth = int(initialDate.strftime('%m'))
        initialday = int(initialDate.strftime('%d')) + 1
        
        initialDate = getMonthDay(initialmonth, initialyear, initialday)

        stringResponse = {
            'cir': cir,
            'plataforma': plataforma,
            'cirWithoutgastos': cirWithoutGastos,
            'initialDate': initialDate,
            'finalDate': finalDate
        }
        return Response(stringResponse, status=status.HTTP_200_OK)

class totalWeekView(generics.RetrieveAPIView):
    queryset = cajas.objects.all()
    serializer_class = cajasSerializer

    def get(self, request, *args, **kwargs):
        Date = pd.Timestamp(kwargs['date'])
        year = int(Date.strftime('%Y'))
        month = int(Date.strftime('%m'))
        day = int(Date.strftime('%d'))
        weekday = int(Date.strftime('%w'))

        initDay = day - weekday
        finalDay = day + (7 - weekday)

        initDate = getMonthDay(month, year, initDay)
        finalDate = getMonthDay(month, year, finalDay)

        totalCajaPapeleria = cajas.objects.filter(date__gt=initDate, date__lte=finalDate).order_by('date').aggregate(Sum('papeleria'))
        papeleria = 0 if totalCajaPapeleria['papeleria__sum'] == None else totalCajaPapeleria['papeleria__sum']

        totalCajaDulces = cajas.objects.filter(date__gt=initDate, date__lte=finalDate).order_by('date').aggregate(Sum('dulces'))
        dulces = 0 if totalCajaDulces['dulces__sum'] == None else totalCajaDulces['dulces__sum']

        totalCajaCir = cajas.objects.filter(date__gt=initDate, date__lte=finalDate).order_by('date').aggregate(Sum('cir'))
        cir = 0 if totalCajaCir['cir__sum'] == None else totalCajaCir['cir__sum']

        totalGastosInventario = gastos.objects.filter(date__gt=initDate, date__lte=finalDate,type='inventario').order_by('date').aggregate(Sum('amount'))
        inventario = 0 if totalGastosInventario['amount__sum'] == None else totalGastosInventario['amount__sum']

        totalGastosPlataforma = gastos.objects.filter(date__gt=initDate, date__lte=finalDate,type='plataforma').order_by('date').aggregate(Sum('amount'))
        plataforma = 0 if totalGastosPlataforma['amount__sum'] == None else totalGastosPlataforma['amount__sum']
        
        totalGastosDulces = gastos.objects.filter(date__gt=initDate, date__lte=finalDate,type='dulces').order_by('date').aggregate(Sum('amount'))
        Gdulces = 0 if totalGastosDulces['amount__sum'] == None else totalGastosDulces['amount__sum']

        totalGastosVarios = gastos.objects.filter(date__gt=initDate, date__lte=finalDate,type='varios').order_by('date').aggregate(Sum('amount'))
        varios = 0 if totalGastosVarios['amount__sum'] == None else totalGastosVarios['amount__sum']

        papeleriaWithoutGastos = papeleria - inventario - varios
        dulcesWithoutGastos = dulces - Gdulces
        cirWithoutGastos = cir - plataforma

        totalSold = papeleria + dulces + cir
        totalGastos = inventario + plataforma + Gdulces + varios
        totalWithoutGastos = totalSold - totalGastos

        initialDate = pd.Timestamp(initDate)
        initialyear = int(initialDate.strftime('%Y'))
        initialmonth = int(initialDate.strftime('%m'))
        initialday = int(initialDate.strftime('%d')) + 1
        
        initialDate = getMonthDay(initialmonth, initialyear, initialday)

        stringResponse = {
            'papeleria': papeleria,
            'dulces': dulces,
            'cir': cir,
            'inventario': inventario,
            'plataforma': plataforma,
            'Gdulces': Gdulces,
            'varios': varios,
            'papeleriaWithoutgastos': papeleriaWithoutGastos,
            'dulcesWithoutgastos': dulcesWithoutGastos,
            'cirWithoutgastos': cirWithoutGastos,
            'totalSold': totalSold,
            'totalGastos': totalGastos,
            'totalWithoutGastos': totalWithoutGastos,
            'initialDate': initialDate,
            'finalDate': finalDate
        }
        return Response(stringResponse, status=status.HTTP_200_OK)

class totalMonthView(generics.RetrieveAPIView):
    queryset = cajas.objects.all()
    serializer_class = cajasSerializer

    def get(self, request, *args, **kwargs):
        Date = pd.Timestamp(kwargs['date'])
        year = int(Date.strftime('%Y'))
        month = int(Date.strftime('%m'))

        initDate = getMonthDay(month,year,1)
        finalDate = getMonthDay(month,year,getMonthDays(month,year))
        
        totalCajaPapeleria = cajas.objects.filter(date__gte=initDate, date__lte=finalDate).order_by('date').aggregate(Sum('papeleria'))
        papeleria = 0 if totalCajaPapeleria['papeleria__sum'] == None else totalCajaPapeleria['papeleria__sum']

        totalCajaDulces = cajas.objects.filter(date__gte=initDate, date__lte=finalDate).order_by('date').aggregate(Sum('dulces'))
        dulces = 0 if totalCajaDulces['dulces__sum'] == None else totalCajaDulces['dulces__sum']

        totalCajaCir = cajas.objects.filter(date__gte=initDate, date__lte=finalDate).order_by('date').aggregate(Sum('cir'))
        cir = 0 if totalCajaCir['cir__sum'] == None else totalCajaCir['cir__sum']

        totalGastosInventario = gastos.objects.filter(date__gte=initDate, date__lte=finalDate,type='inventario').order_by('date').aggregate(Sum('amount'))
        inventario = 0 if totalGastosInventario['amount__sum'] == None else totalGastosInventario['amount__sum']

        totalGastosPlataforma = gastos.objects.filter(date__gte=initDate, date__lte=finalDate,type='plataforma').order_by('date').aggregate(Sum('amount'))
        plataforma = 0 if totalGastosPlataforma['amount__sum'] == None else totalGastosPlataforma['amount__sum']
        
        totalGastosDulces = gastos.objects.filter(date__gte=initDate, date__lte=finalDate,type='dulces').order_by('date').aggregate(Sum('amount'))
        Gdulces = 0 if totalGastosDulces['amount__sum'] == None else totalGastosDulces['amount__sum']

        totalGastosVarios = gastos.objects.filter(date__gte=initDate, date__lte=finalDate,type='varios').order_by('date').aggregate(Sum('amount'))
        varios = 0 if totalGastosVarios['amount__sum'] == None else totalGastosVarios['amount__sum']

        papeleriaWithGastos = papeleria - inventario - varios
        dulcesWithGastos = dulces - Gdulces
        cirWithGastos = cir - plataforma

        totalSold = papeleria + dulces + cir
        totalGastos = inventario + plataforma + Gdulces + varios
        totalWithGastos = totalSold - totalGastos

        totalDeudas = deudas.objects.filter(date__gte=initDate, date__lte=finalDate).order_by('date').aggregate(Sum('amount'))
        Deudas = 0 if totalDeudas['amount__sum'] == None else totalDeudas['amount__sum']
        newDate = pd.Timestamp(initDate)
        Year = int(newDate.strftime('%Y'))
        Month = int(newDate.strftime('%m')) - 1
        if(month == 0):
            Year -= 1
            Month = 12
        totalPreviousMonth = cajaMensual.objects.filter(month=Month).aggregate(Sum('totalSold'))
        PreviousMonth = 0 if totalPreviousMonth['totalSold__sum'] == None else totalPreviousMonth['totalSold__sum']
        totalMonthWithGastosWithPrevious = totalWithGastos + PreviousMonth
        totalMonthWithDeudas = totalMonthWithGastosWithPrevious - Deudas
        
        stringResponse = {
            'papeleria': papeleria,
            'dulces': dulces,
            'cir': cir,
            'inventario': inventario,
            'plataforma': plataforma,
            'Gdulces': Gdulces,
            'varios': varios,
            'papeleriaWithgastos': papeleriaWithGastos,
            'dulcesWithgastos': dulcesWithGastos,
            'cirWithgastos': cirWithGastos,
            'totalSold': totalSold,
            'totalGastos': totalGastos,
            'totalWithGastos': totalWithGastos,
            'totalWithPreviousMonth': totalMonthWithGastosWithPrevious,
            'totalMonthWithDeudas': totalMonthWithDeudas
        }
        return Response(stringResponse, status=status.HTTP_200_OK)

class totalMonthPapeleriaView(generics.RetrieveAPIView):
    queryset = cajas.objects.all()
    serializer_class = cajasSerializer

    def get(self, request, *args, **kwargs):
        Date = pd.Timestamp(kwargs['date'])
        year = int(Date.strftime('%Y'))
        month = int(Date.strftime('%m'))

        initDate = getMonthDay(month,year,1)
        finalDate = getMonthDay(month,year,getMonthDays(month,year))

        totalCajaPapeleria = cajas.objects.filter(date__gte=initDate, date__lte=finalDate).order_by('date').aggregate(Sum('papeleria'))
        papeleria = 0 if totalCajaPapeleria['papeleria__sum'] == None else totalCajaPapeleria['papeleria__sum']

        totalGastosInventario = gastos.objects.filter(date__gte=initDate, date__lte=finalDate,type='inventario').order_by('date').aggregate(Sum('amount'))
        inventario = 0 if totalGastosInventario['amount__sum'] == None else totalGastosInventario['amount__sum']

        totalGastosVarios = gastos.objects.filter(date__gte=initDate, date__lte=finalDate,type='varios').order_by('date').aggregate(Sum('amount'))
        varios = 0 if totalGastosVarios['amount__sum'] == None else totalGastosVarios['amount__sum']

        papeleriaWithoutGastos = papeleria - inventario - varios

        stringResponse = {
            'papeleria': papeleria,
            'inventario': inventario,
            'varios': varios,
            'papeleriaWithoutgastos': papeleriaWithoutGastos,
            'initialDate': initDate,
            'finalDate': finalDate
        }
        return Response(stringResponse, status=status.HTTP_200_OK)

class totalMonthDulcesView(generics.RetrieveAPIView):
    queryset = cajas.objects.all()
    serializer_class = cajasSerializer

    def get(self, request, *args, **kwargs):
        Date = pd.Timestamp(kwargs['date'])
        year = int(Date.strftime('%Y'))
        month = int(Date.strftime('%m'))

        initDate = getMonthDay(month,year,1)
        finalDate = getMonthDay(month,year,getMonthDays(month,year))

        totalCajaDulces = cajas.objects.filter(date__gte=initDate, date__lte=finalDate).order_by('date').aggregate(Sum('dulces'))
        dulces = 0 if totalCajaDulces['dulces__sum'] == None else totalCajaDulces['dulces__sum']

        totalGastosDulces = gastos.objects.filter(date__gte=initDate, date__lte=finalDate,type='dulces').order_by('date').aggregate(Sum('amount'))
        Gdulces = 0 if totalGastosDulces['amount__sum'] == None else totalGastosDulces['amount__sum']

        dulcesWithoutGastos = dulces - Gdulces

        stringResponse = {
            'dulces': dulces,
            'Gdulces': Gdulces,
            'dulcesWithoutgastos': dulcesWithoutGastos,
            'initialDate': initDate,
            'finalDate': finalDate
        }
        return Response(stringResponse, status=status.HTTP_200_OK)

class totalMonthCirView(generics.RetrieveAPIView):
    queryset = cajas.objects.all()
    serializer_class = cajasSerializer

    def get(self, request, *args, **kwargs):
        Date = pd.Timestamp(kwargs['date'])
        year = int(Date.strftime('%Y'))
        month = int(Date.strftime('%m'))

        initDate = getMonthDay(month,year,1)
        finalDate = getMonthDay(month,year,getMonthDays(month,year))

        totalCajaCir = cajas.objects.filter(date__gte=initDate, date__lte=finalDate).order_by('date').aggregate(Sum('cir'))
        cir = 0 if totalCajaCir['cir__sum'] == None else totalCajaCir['cir__sum']

        totalGastosPlataforma = gastos.objects.filter(date__gte=initDate, date__lte=finalDate,type='plataforma').order_by('date').aggregate(Sum('amount'))
        plataforma = 0 if totalGastosPlataforma['amount__sum'] == None else totalGastosPlataforma['amount__sum']

        cirWithoutGastos = cir - plataforma

        stringResponse = {
            'cir': cir,
            'plataforma': plataforma,
            'cirWithoutgastos': cirWithoutGastos,
            'initialDate': initDate,
            'finalDate': finalDate
        }
        return Response(stringResponse, status=status.HTTP_200_OK)