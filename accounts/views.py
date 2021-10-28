from django.contrib.auth.models import User
from rest_framework.views import APIView
from rest_framework.authtoken.models import Token
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth import authenticate
from rest_framework import status
from rest_framework.response import Response

class UserCreateView(APIView):
  def post(self, request):
    username = request.data['username']
    password = request.data['password']
    
    User.objects.create_user(username=username, password=password)

    return Response({'msg':'ok'})

class LoginView(APIView):
  def post(self, request):

    username = request.data['username']
    password = request.data['password']

    user = authenticate(username=username, password=password)
    print(user)
    if user:
        token = Token.objects.get_or_create(user=user)[0]

        return Response({'token': token.key})
    
    return Response({'error':'user not found'}, status=status.HTTP_401_UNAUTHORIZED)