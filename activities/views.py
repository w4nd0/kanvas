from django.core.exceptions import ObjectDoesNotExist
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView


class ActivitiesView(APIView):
    def post(self, request):
        ...
    
    def get(self, request):
        ...
    
class ActivitiesRetriveView(APIView):
    def put(self, request, activity_id):
        ...

class ActivitiesSubmitView(APIView):
    def post(self, request,activity_id):
        ...
    
class SubmissionNoteView(APIView):
    def put(self, request, submission_id):
        ...

class SubmissionView(APIView):
    def get(self, request, submission_id):
        ...
