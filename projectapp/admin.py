from django.contrib import admin

# Register your models here.

from .models import Project,Scope,ProjectImages


class CaseFileAdmin(admin.StackedInline):
    model = ProjectImages

class Projectlist(admin.ModelAdmin):
    list_display = ('title','category','image_tag','location','contractors','developer')
    inlines = [CaseFileAdmin]
   
admin.site.register(Project,Projectlist)

class Scopelist(admin.ModelAdmin):
    list_display = ('title','short_description')
   
admin.site.register(Scope,Scopelist)


