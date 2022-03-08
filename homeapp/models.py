
from django.db import models

from ckeditor_uploader.fields import RichTextUploadingField
from django.utils.html import mark_safe
from django.conf import settings

# Create your models here. 
class Consultancy(models.Model): 
    title = models.CharField(max_length=255,help_text='title must be in 255 character')
    icon =models.FileField(upload_to="consultancy_imgs",null=True,blank=True,help_text='please upload svg icon')
    details = RichTextUploadingField(null=True,blank=True,help_text="try not to put very large text")
 
    def __str__(self):
        return str(self.title) 

    def image_tag(self):
        if self.icon != '':
            return mark_safe('<img src="%s%s" width="50" height="50" />' % (f'{settings.MEDIA_URL}', self.icon))

class Design_engineering(models.Model):
    title = models.CharField(max_length=255,help_text='title must be in 255 character')
    icon =models.FileField(upload_to="design_engineering",null=True,blank=True,help_text='please upload svg icon')
    details = RichTextUploadingField(null=True,blank=True,help_text="try not to put very large text")
 
    def __str__(self):
        return str(self.title) 

    def image_tag(self):
        if self.icon != '':
            return mark_safe('<img src="%s%s" width="50" height="50" />' % (f'{settings.MEDIA_URL}', self.icon))

class Project_management(models.Model):
    title = models.CharField(max_length=255,help_text='title must be in 255 character')
    icon =models.FileField(upload_to="project_management",null=True,blank=True,help_text='please upload svg icon')
    details = RichTextUploadingField(null=True,blank=True,help_text="try not to put very large text")
 
    def __str__(self):
        return str(self.title) 

    def image_tag(self):
        if self.icon != '':
            return mark_safe('<img src="%s%s" width="50" height="50" />' % (f'{settings.MEDIA_URL}', self.icon))
