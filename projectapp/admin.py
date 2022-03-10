from django.contrib import admin

# Register your models here.

from .models import Project,Scope,ProjectImages,Category


class CaseFileAdmin(admin.StackedInline):
    model = ProjectImages

class Projectlist(admin.ModelAdmin):
    list_display = ('title','categories','image_tag','location','contractors','developer')
    inlines = [CaseFileAdmin]
   
admin.site.register(Project,Projectlist)

   
admin.site.register(Category)

class Scopelist(admin.ModelAdmin):
    list_display = ('title','short_description')
   
admin.site.register(Scope,Scopelist)


