# from django.contrib.auth.models import User
from django.contrib.auth import authenticate, get_user_model
from django.db import IntegrityError
from rest_framework import status
from rest_framework.authentication import TokenAuthentication
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializer import UserSerializer

User = get_user_model()

class UserCreateView(APIView):
  def post(self, request):
    try:
      user = User.objects.create_user(**request.data)

      serializer = UserSerializer(user)

      return Response(serializer.data, status=status.HTTP_201_CREATED)
    
    except IntegrityError:
        return Response({'error':'already registered user'}, status=status.HTTP_409_CONFLICT)
        
class LoginView(APIView):
  def post(self, request):

    user = authenticate(**request.data)

    if user:
        token = Token.objects.get_or_create(user=user)[0]

        return Response({'token': token.key})
    
    return Response({'error':'user not found'}, status=status.HTTP_401_UNAUTHORIZED)
