# users/serializers.py
from rest_framework import serializers
from rest_auth.registration.serializers import RegisterSerializer
from rest_auth.serializers import LoginSerializer
from allauth.utils import email_address_exists
from allauth.account.adapter import get_adapter
from allauth.account.utils import setup_user_email
from django.contrib.auth import authenticate, get_user_model
from django.utils.translation import ugettext as _
from django_countries.serializers import CountryFieldMixin
from django_countries.serializer_fields import CountryField
from rest_auth.models import TokenModel
from . import models

User = get_user_model()

class CustomTokenSerializer(serializers.ModelSerializer):
    token = serializers.CharField(source='key')

    class Meta:
        model = TokenModel
        fields = ('token',)

class CustomLoginSerializer(LoginSerializer):
    username = serializers.CharField(required=False, allow_blank=True)
    email = serializers.EmailField(required=True)
    password = serializers.CharField(
        required=True, style={'input_type': 'password'})

########################## USER SERIALIZER ###################################


class UserSerializer(CountryFieldMixin, serializers.ModelSerializer):
    class Meta:
        model = models.CustomUser
        fields = ('id', 'email', 'username', 'profile_photo', 'country')


###################### REGISTRATION SERIALIZER ##########################################

class CustomRegisterSerializer(CountryFieldMixin, RegisterSerializer):
    """
    Registration serializer
    """
    email = serializers.EmailField(required=True, write_only=True)
    password1 = serializers.CharField(required=True, write_only=True, style={
                                      'input_type': 'password'})
    password2 = serializers.CharField(required=True, write_only=True, style={
                                      'input_type': 'password'})
    username = serializers.CharField(
        required=True, min_length=1, max_length=30,  write_only=True)
    profile_photo = serializers.ImageField(required=False,  write_only=True)
    country = CountryField(required=True, write_only=True)

    def validate_country(self, data):
        return data

    def validate_email(self, email):
        email = get_adapter().clean_email(email)
        if email and email_address_exists(email):
            raise serializers.ValidationError(
                _("A user is already registered with this e-mail address."))
        return email

    def validate_password1(self, password):
        return get_adapter().clean_password(password)

    def validate(self, data):
        if data['password1'] != data['password2']:
            raise serializers.ValidationError(
                _("The two password fields didn't match."))
        return data

    def get_cleaned_data(self):
        return {
            'password1': self.validated_data.get('password1', ''),
            'email': self.validated_data.get('email', ''),
            'username': self.validated_data.get('username', ''),
            'profile_photo': self.validated_data.get('profile_photo', ''),
            'country': self.validated_data.get('country', '')
        }

    def save(self, request):
        adapter = get_adapter()
        user = adapter.new_user(request)
        self.cleaned_data = self.get_cleaned_data()
        adapter.save_user(request, user, self)
        setup_user_email(request, user, [])

        ## User extra data assignation
        user.profile_photo = request.data['profile_photo']
        user.country = self.cleaned_data['country']

        user.save()
        return user
