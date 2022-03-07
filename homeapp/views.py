from django.shortcuts import render
from projectapp.models import Scope,Project
from .models import Consultancy,Project_management,Design_engineering

def home(request):
    scopes = Scope.objects.all()[:6]
    projects = Project.objects.all()[:6]

    consultancys = Consultancy.objects.all()[:6]
    design_engineerings = Design_engineering.objects.all()[:6]
    project_managements = Project_management.objects.all()[:6]

    context={
        'scopes':scopes,
        'projects':projects,
        'consultancys':consultancys,
        'project_managements':project_managements,
        'design_engineerings':design_engineerings
    }
    return render(request,'homeapp/homepage.html',context)

def who_we_are(request):
    return render(request,'homeapp/who_we_are.html') 

def who_we_are_for(request):
    return render(request,'homeapp/who_we_are_for.html')


