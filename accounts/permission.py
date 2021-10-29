from rest_framework.permissions import BasePermission

class SpecificInstrutor(BasePermission):
    def has_permission(self, request, view):
        request_method = view.request._request.__dict__['environ']['REQUEST_METHOD']

        route = view.request._request.get_full_path_info()

        return bool(request.user.is_superuser or (request_method == 'GET' and route == '/api/courses/'))

class SpecificFacilitador(BasePermission):
    def has_permission(self, request, view):
        return bool(request.user.is_staff)

class SpecificEstudante(BasePermission):
    def has_permission(self, request, view):
        return bool(not request.user.is_staff)