from django.urls import path
from .views import CourseCreateView, CourseUpdateView, CourseRegistrationsView

urlpatterns = [
    path('courses/', CourseCreateView.as_view()),
    path('courses/<int:course_id>/', CourseUpdateView.as_view()),
    path('courses/<int:course_id>/registrations/', CourseRegistrationsView.as_view())
]