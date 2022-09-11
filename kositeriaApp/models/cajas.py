from django.db import models

class cajas(models.Model):
    id = models.AutoField(primary_key=True)
    date = models.DateField('date')
    papeleria = models.BigIntegerField('papeleria')
    dulces = models.BigIntegerField('dulces')
    cir = models.BigIntegerField('cir')
    totalSold = models.BigIntegerField('totalSold')