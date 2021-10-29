from django.urls import path
from .views import ActivitiesView, ActivitiesUpdateView, ActivitiesSubmitView, SubmissionNoteView, SubmissionView

urlpatterns = [
    path('activities/', ActivitiesView.as_view()),
    path('activities/<int:activity_id>/', ActivitiesUpdateView.as_view()),
    path('activities/<int:activity_id>/submissions/', ActivitiesSubmitView.as_view()),
    path('/submissions/<int:submission_id>/', SubmissionNoteView.as_view()),
    path('/submissions/<int:submission_id>/', SubmissionView.as_view()),
   
]