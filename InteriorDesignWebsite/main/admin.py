from django.contrib import admin
from .models import Service, Project, TeamMember

# Register your models here.
admin.site.register(Service)
admin.site.register(Project)
admin.site.register(TeamMember)

# Admin username and password - username: Admin; password: Test@123