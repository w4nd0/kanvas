from rest_framework import serializers
from accounts.serializer import UserSerializer

class CoursesSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    name = serializers.CharField()
    users = UserSerializer(many=True)