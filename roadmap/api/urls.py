from rest_framework import routers
from roadmap.api import viewsets as views

router = routers.DefaultRouter()

router.register('steps', views.StepViewSet)
router.register('roadmaps', views.RoadMapViewSet)
router.register('projects', views.ProjectViewSet)