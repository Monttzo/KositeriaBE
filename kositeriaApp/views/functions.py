"""return the number of days of the month"""
from calendar import isleap
import datetime
from kositeriaApp.serializers.cajasSerializer import cajasSerializer
from kositeriaApp.models.cajas import cajas
import pandas as pd
from django.db.models import Sum
from kositeriaApp.serializers.gastosSerializer import gastosSerializer
from kositeriaApp.models.gastos import gastos
from kositeriaApp.serializers.deudasSerializer import deudasSerializer
from kositeriaApp.models.deudas import deudas
from kositeriaApp.serializers.cjMensualSerializer import cjMensualSerializer
from kositeriaApp.models.cajaMensual import cajaMensual

def getMonthDays(month:int, year:int) -> int:
        if int(month) in [4, 6, 9, 11]:
            return 30
        if int(month) == 2:
            if isleap(int(year)):
                return 29
            else:
                return 28
        else:
            return 31

"""return the day of the month evaluating if the initial 
day in negative or exceeds the days of the month"""
def getMonthDay(month:int, year:int, day:int) -> datetime:
    monthDays = getMonthDays(month, year)
    if(day <= 0):
        month -= 1
        monthDays = getMonthDays(month, year)
        day = monthDays + day
        return datetime.date(year, month, day)
        
    if(day > monthDays):
        diferenceDays = day - monthDays
        month += 1
        return datetime.date(year, month, diferenceDays)
    
    return datetime.date(year, month, day)