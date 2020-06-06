from django.contrib import admin
from .models import Service, TeamMember

# Register your models here.
admin.site.register(Service)
admin.site.register(TeamMember)

# Admin username and password - username: Admin; password: Test@123