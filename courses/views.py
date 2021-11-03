from accounts.models import User
from accounts.permission import SpecificInstrutor
from django.core.exceptions import ObjectDoesNotExist, PermissionDenied
from django.db import IntegrityError
from rest_framework import status
from rest_framework.authentication import TokenAuthentication
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Courses
from .serializer import CoursesSerializer


class CourseView(APIView):
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
            return Response(
                {"error": "Course with this name already exists"},
                status=status.HTTP_409_CONFLICT,
            )

        except KeyError:
            return Response(
                {"error": "Invalid key"},
                status=status.HTTP_400_BAD_REQUEST,
            )


class CourseRetriveView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [SpecificInstrutor]

    def get(self, request, course_id):
        course = Courses.objects.get(id=course_id)

        serializer = CoursesSerializer(course)

        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, course_id):
        try:
            Courses.objects.filter(id=course_id).update(name=request.data["name"])

            course = Courses.objects.get(id=course_id)

            serializer = CoursesSerializer(course)

            return Response(serializer.data, status=status.HTTP_200_OK)

        except IntegrityError:
            return Response(
                {"error": "Course with this name already exists"},
                status=status.HTTP_409_CONFLICT,
            )

        except ObjectDoesNotExist:
            return Response(
                {"error": "Course not found"},
                status=status.HTTP_404_NOT_FOUND,
            )

        except KeyError:
            return Response(
                {"error": "Invalid key"},
                status=status.HTTP_400_BAD_REQUEST,
            )

    def delete(self, request, course_id):
        try:
            course = Courses.objects.filter(id=course_id)

            if bool(course):
                course.delete()

            else:
                raise ObjectDoesNotExist

            return Response(status=status.HTTP_204_NO_CONTENT)

        except ObjectDoesNotExist:
            return Response(
                {"error": "Course not found"},
                status=status.HTTP_404_NOT_FOUND,
            )


class CourseRegistrationsView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [SpecificInstrutor]

    def put(self, request, course_id):
        try:
            if type(request.data["user_ids"]) != list:
                raise ValueError("Wrong request format.")

            for user_id in request.data["user_ids"]:
                user = User.objects.filter(id=user_id).first()
                if bool(user.is_staff) or bool(user.is_superuser):
                    raise PermissionDenied

            Courses.objects.get(id=course_id).users.clear()

            for user_id in request.data["user_ids"]:
                User.objects.filter(id=user_id).update(course_id=course_id)

            course = Courses.objects.get(id=course_id)

            serializer = CoursesSerializer(course)

            return Response(serializer.data, status=status.HTTP_200_OK)

        except ObjectDoesNotExist:
            return Response(
                {"error": "invalid course_id."},
                status=status.HTTP_404_NOT_FOUND,
            )

        except KeyError as e:
            print(e)
            return Response(
                {"error": "invalid key."},
                status=status.HTTP_400_BAD_REQUEST,
            )

        except ValueError as e:
            return Response(
                {"error": str(e)},
                status=status.HTTP_400_BAD_REQUEST,
            )

        except PermissionDenied:
            return Response(
                {"errors": "Only students can be enrolled in the course."},
                status=status.HTTP_400_BAD_REQUEST,
            )
