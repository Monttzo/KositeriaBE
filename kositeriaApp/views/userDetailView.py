from django.conf import settings
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework_simplejwt.backends import TokenBackend
from rest_framework.permissions import IsAuthenticated
from kositeriaApp.models.user import user
from kositeriaApp.serializers.userSerializer import userSerializer

class userDetailView(generics.RetrieveAPIView):
    queryset = user.objects.all()
    serializer_class = userSerializer
    permission_classes = (IsAuthenticated,)

    def get(self, request, *args, **kwargs):
        
        token = request.META.get('HTTP_AUTHORIZATION')[7:]
        tokenBackend = TokenBackend(algorithm=settings.SIMPLE_JWT['ALGORITHM'])
        valid_data = tokenBackend.decode(token,verify=False)

        if valid_data['user_id'] != kwargs['pk']:
            stringResponse = {'detail':'Unauthorized Request'}
            return Response(stringResponse, status=status.HTTP_401_UNAUTHORIZED)

        return super().get(request, *args, **kwargs)