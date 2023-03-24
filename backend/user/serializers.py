from core.models import User
from django.contrib.auth import get_user_model, authenticate
from rest_framework import serializers
from django.utils.translation import gettext_lazy as _
from core.models import Accounts, User


class UserSerializer(serializers.ModelSerializer):
    """ serializer for the users objects """

    class Meta:
        model = get_user_model()
        fields = ('email', 'password', 'first_name', 'last_name', 'id')
        extra_kwargs = {'password': {'write_only': True , 'min_length': 5}}

    
    def create(self, validated_data):
        """ creates a new user with password and return it """
        newUser = get_user_model().objects.create_user(**validated_data)
        return newUser


class AuthTokenSeriliazer(serializers.Serializer):
    """ Serializer for the user authentification object """
    email = serializers.CharField()
    password = serializers.CharField(style={'input_type': 'password'}, trim_whitespace=False)

    def validate(self, attrs):
        """ Validate and authentificate the user """
        email = attrs.get('email')
        password = attrs.get('password')
        user = authenticate(
            request = self.context.get('request'),
            username = email, 
            password = password
        )
        if not user:
            msg = ('The credentials provided are not OK')
            raise serializers.ValidationError(msg, code='authentication')
        attrs['user'] = user
        return attrs

class AccountSerializer(serializers.ModelSerializer):
    """ Seriliazer for the account object """
    class Meta:
        model = User
        fields = ('id', 'first_name', 'email', 'last_name')
        read_only_fields = ('id',)