from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializer import *
from .emails import *
# Create your views here.


class RegisterAPI(APIView):
    def post(self,request):
        try:
            data=request.data
            serializer=UserSerializer(data=data)
            if serializer.is_valid():    
                serializer.save()
                send_otp_via_email(serializer.data['email'])
            
                return Response({
                    'status':200,
                    'message':'registeration successfull. Check email',
                    'data':serializer.data
                })
            return Response({
                'status':400,
                'message':'something went wrong',
                'data':serializer.errors
            })
            
        except Exception as e:
            print(e)
            
            
class VerifyOTP(APIView):
    def post(self,request):
        try:
            data=request.data
            serializer=VerifyAccountSerializer(data=data)
            if serializer.is_valid():    
                email=serializer.data['email']
                otp=serializer.data['otp']
                user= CustomUser.objects.filter(email=email)
                print(user[0])
                if not user.exists():
                    return Response({
                    'status':400,
                    'message':'something went wrong',
                    'data':'Invalid Email'
                })
                    
                if not user[0].otp==otp :
                    return Response({
                        'status':200,
                        'message':'something went wrong',
                        'data':'wrong otp'
                    })
                user[0].is_verified=True
                user[0].save()
            return Response({
                        'status':200,
                        'message':'account verified',
                        'data':serializer.data
                    })
            
        except Exception as e:
            print(e)
            
class LoginAPI(APIView):
    def post(self,request):
        try:
            data=request.data
            serializers=LoginSerializer(data=data)
            if serializers.is_valid():
                email=serializers.data['email']
                password=serializers.data['password']
                user=CustomUser.objects.filter(email=email)
                if user.exists():
                    return Response({
                        'status':400,
                        'message':'Logged In Successfully',
                        'data':serializers.data
                    })
                else:
                    return Response({
                        'status':400,
                        'message':'Invalid email or password'
                    })
            else:
                return Response({
                    'status':400,
                    'message':'Validation Error',
                    'data':serializers.error
                })
        except Exception as e:
            return Response({
                'status':500,
                'message':'Internal Server error',
                'error':str(e)
            })
           