from django.contrib import admin

from roadmap.models import Step, RoadMap, Project


class StepAdmin(admin.ModelAdmin):
    pass

class RoadMapAdmin(admin.ModelAdmin):
    pass

class ProjectAdmin(admin.ModelAdmin):
    pass

admin.site.register(Step, StepAdmin)
admin.site.register(RoadMap, RoadMapAdmin)
admin.site.register(Project, ProjectAdmin)