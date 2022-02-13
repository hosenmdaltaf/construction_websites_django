from django.contrib import admin

# Register your models here.
from .models import Consultancy,Project_management,Design_engineering


class Consultancylist(admin.ModelAdmin):
    list_display = ('title','icon','details')
   
admin.site.register(Consultancy,Consultancylist)

class Project_managementlist(admin.ModelAdmin):
    list_display = ('title','icon','details')
   
admin.site.register(Project_management,Project_managementlist)


class Design_engineeringlist(admin.ModelAdmin):
    list_display = ('title','icon','details')
   
admin.site.register(Design_engineering,Design_engineeringlist)

