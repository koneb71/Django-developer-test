from rest_framework import serializers

from roadmap.models import Step, RoadMap, Project, Users


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = ('username', 'email')


class StepSerializer(serializers.ModelSerializer):
    class Meta:
        model = Step
        fields = ('name', 'explanation')


class RoadMapSerializer(serializers.ModelSerializer):
    steps = StepSerializer(many=True)

    class Meta:
        model = RoadMap
        fields = ('name', 'steps')


class ProjectSerializer(serializers.ModelSerializer):
    roadmap = RoadMapSerializer()
    owner = UserSerializer()

    class Meta:
        model = Project
        fields = ('name', 'description', 'roadmap', 'owner')
