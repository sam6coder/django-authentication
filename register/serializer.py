from rest_framework import serializers
from .models import CustomUser

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=CustomUser
        fields=['email','password','is_verified']
        
class VerifyAccountSerializer(serializers.Serializer):
    email=serializers.EmailField()
    otp=serializers.CharField()
    
class LoginSerializer(serializers.Serializer):
    email=serializers.EmailField()
    password=serializers.CharField()