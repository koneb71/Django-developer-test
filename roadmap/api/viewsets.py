from rest_framework import viewsets

from roadmap.api.serializers import StepSerializer, RoadMapSerializer, ProjectSerializer
from roadmap.models import Step, RoadMap, Project


class StepViewSet(viewsets.ModelViewSet):
    queryset = Step.objects.all()
    serializer_class = StepSerializer


class RoadMapViewSet(viewsets.ModelViewSet):
    queryset = RoadMap.objects.all()
    serializer_class = RoadMapSerializer


class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer