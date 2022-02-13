from multiprocessing import context
from django.shortcuts import render

from projectapp.models import Scope,Project

# Create your views here.


def project_details(request,pk):
    object = Project.objects.get(pk=pk)
    all = Project.objects.all()
    context ={
        'object':object,
        'all':all
    }
    return render(request,'projectapp/project_details.html',context)

def scope_details(request,pk): 
    object = Scope.objects.get(pk=pk)
    context ={
        'object':object
    }
    return render(request,'projectapp/scope_details.html',context)

