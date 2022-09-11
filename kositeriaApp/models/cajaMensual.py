from django.db import models

class cajaMensual(models.Model):
    id = models.AutoField(primary_key=True)
    date = models.DateField('date')
    month = models.BigIntegerField('month')
    totalSold = models.BigIntegerField('totalSold')
    year = models.BigIntegerField('year', default=2022)