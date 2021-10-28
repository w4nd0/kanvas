from rest_framework.permissions import BasePermission

class SpecificFacilitador(BasePermission):
    def has_permission(self, request, view):
        ...

class SpecificInstrutor(BasePermission):
    def has_permission(self, request, view):
        ...