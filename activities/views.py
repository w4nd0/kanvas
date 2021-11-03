from accounts.permission import SpecificFacilitador, SpecificEstudante
from django.core.exceptions import ObjectDoesNotExist
from django.db import IntegrityError
from rest_framework import status
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Activities, Submissions
from .serializer import ActiviesSerializer, SubmissionsSerializer


class ActivitiesView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [SpecificFacilitador]

    def post(self, request):
        try:
            activity = Activities.objects.create(**request.data)

            serializer = ActiviesSerializer(activity)

            return Response(serializer.data, status=status.HTTP_201_CREATED)

        except IntegrityError:
            return Response(
                {"error": "Activity with this name already exists"},
                status=status.HTTP_409_CONFLICT,
            )

        except KeyError:
            return Response(
                {"error": "Invalid key"},
                status=status.HTTP_400_BAD_REQUEST,
            )

    def get(self, request):
        activities = Activities.objects.all()

        serializer = ActiviesSerializer(activities, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)


class ActivitiesUpdateView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [SpecificFacilitador]

    def put(self, request, activity_id):
        try:
            Activities.objects.filter(id=activity_id).update(**request.data)

            activities = Activities.objects.get(id=activity_id)

            serializer = ActiviesSerializer(activities)

            return Response(serializer.data, status=status.HTTP_200_OK)

        except IntegrityError:
            return Response(
                {"error": "Activity with this name already exists"},
                status=status.HTTP_409_CONFLICT,
            )

        except ObjectDoesNotExist:
            return Response(
                {"error": "Activity not found"},
                status=status.HTTP_404_NOT_FOUND,
            )

        except KeyError:
            return Response(
                {"error": "Invalid key"},
                status=status.HTTP_400_BAD_REQUEST,
            )


class ActivitiesSubmitView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [SpecificEstudante]

    def post(self, request, activity_id):
        try:
            new_submission = {
                "repo": request.data["repo"],
                "user_id": request.user.id,
                "activity_id": activity_id,
            }

            submission = Submissions.objects.create(**new_submission)

            serializer = SubmissionsSerializer(submission)

            return Response(serializer.data, status=status.HTTP_201_CREATED)
        except:
            return Response({"msg": "ok"})


class SubmissionNoteView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [SpecificFacilitador]

    def put(self, request, submission_id):
        try:
            Submissions.objects.filter(id=submission_id).update(**request.data)

            submission = Submissions.objects.get(id=submission_id)

            serializer = SubmissionsSerializer(submission)

            return Response(serializer.data, status=status.HTTP_200_OK)

        except ObjectDoesNotExist:
            return Response(
                {"error": "Submission not found"},
                status=status.HTTP_404_NOT_FOUND,
            )

        except KeyError:
            return Response(
                {"error": "Invalid key"},
                status=status.HTTP_400_BAD_REQUEST,
            )


class SubmissionView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        if bool(request.user.is_staff):
            submissions = Submissions.objects.all()
        else:
            submissions = Submissions.objects.filter(user_id=request.user.id)

        serializer = SubmissionsSerializer(submissions, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)
