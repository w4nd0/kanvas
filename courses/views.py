from django.core.exceptions import ObjectDoesNotExist
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Courses
from .serializer import CoursesSerializer

class CourseCreateView(APIView):
    ...

class CourseUpdateView(APIView):
    ...

class CourseRegistrationsView(APIView):
    ...
