from rest_framework.permissions import BasePermission

class SpecificInstrutor(BasePermission):
    def has_permission(self, request, view):
        return request.user.is_superuser

class SpecificFacilitador(BasePermission):
    def has_permission(self, request, view):
        return request.user.is_staff

class SpecificEstudante(BasePermission):
    def has_permission(self, request, view):
        return not request.user.is_staff