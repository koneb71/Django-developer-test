from django.conf.urls import include, url
from django.contrib import admin
from roadmap.api.urls import router as roadmap_api


urlpatterns = [
    url(r'^', include('roadmap.urls', namespace='roadmap')),
    url(r'^api/', include(roadmap_api.urls)),
    url(r'^admin/', include(admin.site.urls)),
]
