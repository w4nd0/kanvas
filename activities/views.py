from accounts.permission import SpecificFacilitador, SpecificEstudante
from django.core.exceptions import ObjectDoesNotExist
from rest_framework import status
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView


class ActivitiesView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated, SpecificFacilitador]

    def post(self, request):
        ...
    
    def get(self, request):
        ...
    
class ActivitiesUpdateView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated, SpecificFacilitador]

    def put(self, request, activity_id):
        ...

class SubmissionNoteView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated, SpecificFacilitador]

    def put(self, request, submission_id):
        ...

class ActivitiesSubmitView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated, SpecificEstudante]

    def post(self, request,activity_id):
        ...
    
class SubmissionView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated, SpecificEstudante]

    def get(self, request):
        ...
