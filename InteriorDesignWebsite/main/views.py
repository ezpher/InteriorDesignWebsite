from django.shortcuts import HttpResponse, redirect, render
from .models import Service, Project, TeamMember
from .filters import ProjectFilter
from django.core.mail import send_mail

# Create your views here.

def index(request):
   
    if request.method == 'POST':
        email_subject = request.POST.get('name')
        email_message = request.POST.get('message')
        email_address = request.POST.get('email')        

        send_mail(
            email_subject,
            email_message,
            email_address,
            ['test@test.com']
        )
        
        return redirect(email_confirmation)
    else:
        services = Service.objects.all()
        team_members = TeamMember.objects.all()
        context = {'services': services, 'team_members': team_members}

        return render(request, 'index.html', context)

def email_confirmation(request):

    return render(request, 'email_confirmation.html')

def get_projects(request):

    projects = Project.objects.all()
    project_filter = ProjectFilter(request.GET, queryset=projects)
    filtered_projects = project_filter.qs
    context = {'projects': filtered_projects, 'project_filter': project_filter}

    return render(request, 'projects.html', context)
