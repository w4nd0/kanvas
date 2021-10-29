from django.urls import path
from .views import CourseView, CourseRetriveView, CourseRegistrationsView

urlpatterns = [
    path('courses/', CourseView.as_view()),
    path('courses/<int:course_id>/', CourseRetriveView.as_view()),
    path('courses/<int:course_id>/registrations/', CourseRegistrationsView.as_view())
]