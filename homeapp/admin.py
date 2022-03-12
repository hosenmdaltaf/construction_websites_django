from django.contrib import admin

# Register your models here.
from .models import Consultancy,Design_engineering,Product


class Consultancylist(admin.ModelAdmin):
    list_display = ('title','icon','details')
   
admin.site.register(Consultancy,Consultancylist)

# class Project_managementlist(admin.ModelAdmin):
#     list_display = ('title','icon','details')
   
# admin.site.register(Project_management,Project_managementlist)

class Productlist(admin.ModelAdmin):
    list_display = ('name','image','details')

admin.site.register(Product,Productlist)

class Design_engineeringlist(admin.ModelAdmin):
    list_display = ('title','icon','details')
   
admin.site.register(Design_engineering,Design_engineeringlist)

