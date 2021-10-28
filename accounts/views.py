from django.contrib.auth.models import User
from rest_framework.views import APIView
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response


class UserCreateView(APIView):
  def post(self, request):
    User.objects.create_user(request.data)

    return Response({'msg':'ok'})