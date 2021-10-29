from accounts.permission import SpecificInstrutor
from django.core.exceptions import ObjectDoesNotExist
from rest_framework import status
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from django.db import IntegrityError


from .models import Courses
from .serializer import CoursesSerializer


class CourseView(APIView):    
    #TODO tem que colocar busca por id tb
    authentication_classes = [TokenAuthentication]
    permission_classes = [SpecificInstrutor]

    def get(self, request):
        courses = Courses.objects.all()

        serializer = CoursesSerializer(courses, many=True)
        
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        try:
            course = Courses.objects.create(**request.data)

            serializer = CoursesSerializer(course)

            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        except IntegrityError:
            return Response({'error': 'Course with this name already exists'}, 
                            status=status.HTTP_409_CONFLICT)

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
