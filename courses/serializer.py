from rest_framework import serializers


class CoursesSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    name = serializers.CharField()
    # users = UsersSerializer(many=True)