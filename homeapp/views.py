from django.shortcuts import render
from projectapp.models import Scope,Project,Category
from .models import Consultancy,Design_engineering,Product,Contact

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

def product_details(request,pk):
    object = Product.objects.get(pk=pk)
    all = Product.objects.all()
    context ={
        'object':object,
        'all':all
    }
    return render(request,'homeapp/product_details.html',context)

def who_we_are(request):
    return render(request,'homeapp/who_we_are.html') 

def who_we_are_for(request):
    return render(request,'homeapp/who_we_are_for.html')

def career(request):
    # if request.method =="POST" and request.FILES['file']:
    if request.method == 'POST' and request.FILES.get('file', False):
        name = request.POST.get('name')
        phone =request.POST.get('phone')
        email = request.POST.get('email')
        message = request.POST.get('message')
        position = request.POST.get('position')
        file = request.FILES['file']
        Contact.objects.create(name=name,email=email,message=message,phone=phone,position=position,file=file)
        return render(request,'global/thankyou.html')
    
    return render(request,'global/career.html')





