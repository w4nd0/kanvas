from django.core.exceptions import ObjectDoesNotExist
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Courses
from .serializer import CoursesSerializer

class CourseView(APIView):
    def get(self, request):
        ...

class CreateCourseView(APIView):
    def post(self, request):
        ...

class CourseRetriveView(APIView):
    def put(self, request):
        ...

    def delete(self, request):
        ...

class CourseRegistrationsView(APIView):
    def put(self, request):
        ...
