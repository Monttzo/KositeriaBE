"""KositeriaProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from rest_framework_simplejwt.views import (TokenObtainPairView, TokenRefreshView)
from kositeriaApp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', TokenObtainPairView.as_view()),
    path('refresh/', TokenRefreshView.as_view()),
    path('createUser/', views.userCreateView.as_view()),
    path('detailUser/<int:pk>/', views.userDetailView.as_view()),
    path('updateUser/<int:user>/<int:pk>/', views.userUpdateView.as_view()),
    path('deleteUser/<int:user>/<int:pk>/', views.userDeleteView.as_view()),
    path('appModeUser/<username>/', views.appModeDetailView.as_view()),
    #Cajas
    path('createCaja/', views.cajasCreateView.as_view()),
    path('detailCaja/<int:id>/', views.cajasDetailView.as_view()),
    path('detailWeekCaja/<date>/', views.cajasDetailWeekView.as_view()),
    path('detailMonthCaja/<date>/', views.cajasDetailMonthView.as_view()),
    path('updateCaja/<pk>/', views.cajasUpdateView.as_view()),
    path('deleteCaja/<int:pk>/', views.cajasDeleteView.as_view()),
    #Gastos
    path('createGasto/', views.gastosCreateView.as_view()),
    path('detailGasto/<int:id>/', views.gastosDetailView.as_view()),
    path('detailWeekGasto/<date>/', views.gastosDetailWeekView.as_view()),
    path('detailWeekTypeGasto/<date>/<type>/', views.gastosDetailWeekTypeView.as_view()),
    path('detailMonthGasto/<date>/', views.gastosDetailMonthView.as_view()),
    path('detailMonthTypeGasto/<date>/<type>/', views.gastosDetailMonthTypeView.as_view()),
    path('updateGasto/<pk>/', views.gastosUpdateView.as_view()),
    path('deleteGasto/<int:pk>/', views.gastosDeleteView.as_view()),
    #Deudas
    path('createDeuda/', views.deudasCreateView.as_view()),
    path('detailDeuda/<int:id>/', views.deudasDetailView.as_view()),
    path('detailWeekDeuda/<date>/', views.deudasDetailWeekView.as_view()),
    path('detailMonthDeuda/<date>/', views.deudasDetailMonthView.as_view()),
    path('updateDeuda/<pk>/', views.deudasUpdateView.as_view()),
    path('deleteDeuda/<int:pk>/', views.deudasDeleteView.as_view()),
    #Total
    path('detailTotalWeek/<date>/', views.totalWeekView.as_view()),
    path('detailTotalWeekPapeleria/<date>/', views.totalWeekPapeleriaView.as_view()),
    path('detailTotalWeekDulces/<date>/', views.totalWeekDulcesView.as_view()),
    path('detailTotalWeekCir/<date>/', views.totalWeekCirView.as_view()),
    path('detailTotalMonthPapeleria/<date>/', views.totalMonthPapeleriaView.as_view()),
    path('detailTotalMonthDulces/<date>/', views.totalMonthDulcesView.as_view()),
    path('detailTotalMonthCir/<date>/', views.totalMonthCirView.as_view()),
    path('detailTotalMonth/<date>/', views.totalMonthView.as_view()),
    #cajaMensual
    path('createCajaMensual/', views.cjMensualCreateView.as_view()),
    path('detailCajaMensual/<int:id>/', views.cjMensuakDetailView.as_view()),
    path('detailMonthCajaMensual/<month>/<year>/', views.cjMensualMonthView.as_view()),
    path('detailYearCajaMensual/<year>/', views.cjMensualYearView.as_view()),
    path('updateCajaMensual/<pk>/', views.cjMensualUpdateView.as_view()),
    path('deleteCajaMensual/<int:pk>/', views.cjMensualDeleteView.as_view()),
]
