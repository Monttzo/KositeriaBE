from django.contrib import admin
from .models.user import user
from .models.cajas import cajas
from .models.gastos import gastos
from .models.deudas import deudas


admin.site.register(user)
admin.site.register(cajas)
admin.site.register(gastos)
admin.site.register(deudas)
# Register your models here.
