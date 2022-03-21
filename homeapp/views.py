from django.shortcuts import render
from projectapp.models import Scope,Project,Category
from .models import Consultancy,Design_engineering,Product

def home(request):
    scopes = Scope.objects.all().order_by('-id')[:6]
    projects = Project.objects.all()[:6]

    consultancys = Consultancy.objects.all()[:6]
    design_engineerings = Design_engineering.objects.all()[:6]
    # project_managements = Project_management.objects.all()[:6]

    context={
        'scopes':scopes,
        'projects':projects,
        'consultancys':consultancys,
        # 'project_managements':project_managements,
        'design_engineerings':design_engineerings
    }
    return render(request,'homeapp/homepage.html',context)

def category_filter(request,pk):
    category = Project.objects.filter(categories=pk)
    cat_name =Category.objects.filter(pk=pk).first()
    context={
        'category': category,
        'cat_name':cat_name
    }
    return render(request,'homeapp/category.html',context )


def product(request):
    products =Product.objects.all()
    projects = Project.objects.all()[:6]
    context={
        'products': products,
        'projects':projects
    }
    return render(request,'homeapp/product.html',context) 

def who_we_are(request):
    return render(request,'homeapp/who_we_are.html') 

def who_we_are_for(request):
    return render(request,'homeapp/who_we_are_for.html')




