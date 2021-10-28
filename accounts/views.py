from django.contrib.auth.models import User
from rest_framework.views import APIView
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

class UserCreateView(APIView):
  def post(self, request):
    print(request.data)
    # User.objects.create_user(
    #   username=request.data['username'],
    #   password=request.data['password'])

    return '',200