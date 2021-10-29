from accounts.permission import SpecificInstrutor
from django.core.exceptions import ObjectDoesNotExist
from rest_framework import status
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Courses
from .serializer import CoursesSerializer


class CourseView(APIView):    
    def get(self, request):
    #TODO tem que colocar busca por id tb
        ...


class CreateCourseView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated, SpecificInstrutor]

    def post(self, request):
        ...

class CourseRetriveView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated, SpecificInstrutor]
    
    def put(self, request):
        ...

    def delete(self, request):
        ...

class CourseRegistrationsView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated, SpecificInstrutor]

    def put(self, request):
        ...
