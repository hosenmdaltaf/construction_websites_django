
from django.db import models
from django.urls import reverse

from ckeditor_uploader.fields import RichTextUploadingField
from django.utils.html import mark_safe
from django.conf import settings


# CATEGORY_CHOICES = (
# ("LN", "Landmark"),
# ("RN", "Running"),
# ("UP", "Upcoming"),
# ("CO", "Complated"),)
         
# # Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return str(self.name) 
    
    def get_absolute_url(self):
        return reverse('homeapp:categorypage', kwargs={'pk':self.pk})
    

class Project(models.Model):
    title = models.CharField(max_length=255,help_text='title must be in 255 character')
    categories = models.ForeignKey(Category,on_delete=models.CASCADE,null=True,blank=True)
    thumnail_image =models.ImageField(upload_to="project_imgs",help_text='upload thumnail image for project')
    details = RichTextUploadingField(null=True,blank=True,help_text="write details about your project")
    services = RichTextUploadingField(null=True,blank=True,help_text="write service of your project as a list")
    location = models.TextField(null=True,blank=True,help_text="write loaction about your project")
    contractors = models.TextField(null=True,blank=True,help_text="write contractors about your project")
    developer = models.TextField(null=True,blank=True,help_text="write developer about your project")

    def __str__(self):
        return str(self.title) 

    def image_tag(self):
        if self.thumnail_image != '':
            return mark_safe('<img src="%s%s" width="50" height="50" />' % (f'{settings.MEDIA_URL}', self.thumnail_image))


class ProjectImages(models.Model):
    case = models.ForeignKey(Project,on_delete=models.CASCADE,null=True,blank=True)
    images = models.ImageField(upload_to="file_upload", null = True, blank = True,help_text='upload images for project')



class Scope(models.Model):
    title =  models.CharField(max_length=255,help_text='title must be in 255 character')
    icon =models.FileField(upload_to="Scope_images",null=True,blank=True,help_text='please upload svg icon')
    short_description = models.TextField(null=True,blank=True,help_text="write a very short details about your project")
    long_text = RichTextUploadingField(null=True,blank=True,help_text="write long details about your project")

    def __str__(self):
        return str(self.title) 

    def image_tag(self):
        if self.icon != '':
            return mark_safe('<img src="%s%s" width="50" height="50" />' % (f'{settings.MEDIA_URL}', self.icon))
 