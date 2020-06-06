from django.shortcuts import render
from .models import Service, Project, TeamMember
from .filters import ProjectFilter

# Create your views here.

def index(request):

    services = Service.objects.all()
    team_members = TeamMember.objects.all()
    context = {'services': services, 'team_members': team_members}

    return render(request, 'index.html', context)

def get_projects(request):

    projects = Project.objects.all()
    project_filter = ProjectFilter(request.GET, queryset=projects)
    filtered_projects = project_filter.qs
    context = {'projects': filtered_projects, 'project_filter': project_filter}

    return render(request, 'projects.html', context)
