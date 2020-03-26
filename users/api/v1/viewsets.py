from rest_framework import authentication
from users.models import Phone
from .serializers import PhoneSerializer
from rest_framework import viewsets


class PhoneViewSet(viewsets.ModelViewSet):
    serializer_class = PhoneSerializer
    authentication_classes = (
        authentication.SessionAuthentication,
        authentication.TokenAuthentication,
    )
    queryset = Phone.objects.all()
