from core.models import User
from rest_framework import generics
from user.serializers import UserSerializer, AccountSerializer
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings
from user.serializers import UserSerializer, AuthTokenSeriliazer
from rest_framework.authentication import TokenAuthentication
from rest_framework import viewsets, mixins
from rest_framework.permissions import IsAuthenticated
from core.models import Accounts
from user import serializers
from main.integrations.omnisend import Omnisend

class CreateUserView(generics.CreateAPIView):
    """ Create a new user in the system """
    serializer_class = UserSerializer

    def perform_create(self, serializer):
        GetContact = Omnisend()
        contactID = GetContact.Contact(self.request.data['email'], self.request.data['first_name'],
                                       self.request.data['last_name'])
        serializer.save(mailchimp_id=contactID)

class CreateTokenView(ObtainAuthToken):
    """ Create new auth token for the user """
    serializer_class = AuthTokenSeriliazer
    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES


class AccountsViewSet(viewsets.GenericViewSet, 
                      mixins.ListModelMixin,
                      mixins.CreateModelMixin):
    """ allow to view the accounts """
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)
    queryset = User.objects.all()
    serializer_class = serializers.AccountSerializer

    def get_queryset(self):
        """ return account for authentificated user only """
        return self.queryset.filter(email=self.request.user)

    def perform_create(self, serializer):
        """ create an accounts """
        serializer.save(user=self.request.user)

