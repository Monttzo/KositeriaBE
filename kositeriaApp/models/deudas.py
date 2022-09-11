from django.db import models

class deudas(models.Model):
    id = models.AutoField(primary_key=True)
    date = models.DateField('date')
    detail = models.CharField('detail',max_length=100, null=True)
    amount = models.BigIntegerField('amount')
