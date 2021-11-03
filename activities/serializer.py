from rest_framework import serializers


class SubmissionsSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    grade = serializers.IntegerField()
    repo = serializers.CharField()
    user_id = serializers.IntegerField()
    activity_id = serializers.IntegerField()


class ActiviesSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    title = serializers.CharField()
    points = serializers.IntegerField()
    submissions = SubmissionsSerializer(many=True)
