from django.urls import path
from .views import UserCreateView

urlpatterns = [
    path('accounts/', UserCreateView.as_view())
]