from calendar import isleap
import datetime
from rest_framework import status, views, generics
from rest_framework.response import Response
from kositeriaApp.models.user import user
from kositeriaApp.serializers.userSerializer import userSerializer

from kositeriaApp.views.functions import getMonthDay, getMonthDays

class appModeDetailView(views.APIView):
    queryset = user.objects.all()
    serializer_class = userSerializer
    
    def get(self, request, *args, **kwargs):
        User = user.objects.get(username=kwargs['username'])
        response = {
            'appMode': User.appMode
        }
        return Response(response, status=status.HTTP_200_OK)
