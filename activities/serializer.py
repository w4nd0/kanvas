from rest_framework import serializers


class ActiviesSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    title = serializers.CharField()
    points = serializers.IntegerField()

    # users = UsersSerializer(many=True)


class SubmissionsSerializer(serializers.Serializer):
    id = serializers.IntegerField()
