# from users.models import CustomUser
# from rest_auth.registration.serializers import RegisterSerializer
# from rest_framework import serializers


# class CustomRegisterSerializer(RegisterSerializer):

#     email = serializers.EmailField(required=True)
#     password1 = serializers.CharField(write_only=True)
#     username = serializers.CharField(required=True)
#     profile_photo = serializers.ImageField(required=False)

#     def get_cleaned_data(self):
#         super(CustomRegisterSerializer, self).get_cleaned_data()

#         return {
#             'password1': self.validated_data.get('password1', ''),
#             'email': self.validated_data.get('email', ''),
#             'username': self.validated_data.get('username', ''),
#             'profile_photo': self.validated_data.get('profile_photo', ''),
#         }

# class CustomUserDetailsSerializer(serializers.HyperlinkedModelSerializer):

#     class Meta:
#         model = CustomUser
#         fields = ('email','username','profile_photo')
#         read_only_fields = ('email',)