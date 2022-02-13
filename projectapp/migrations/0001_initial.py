# Generated by Django 3.2 on 2022-02-12 09:51

import ckeditor_uploader.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(help_text='title must be in 255 character', max_length=255)),
                ('thumnail_image', models.ImageField(help_text='upload thumnail image for project', upload_to='project_imgs')),
                ('details', ckeditor_uploader.fields.RichTextUploadingField(blank=True, help_text='write details about your project', null=True)),
                ('services', ckeditor_uploader.fields.RichTextUploadingField(blank=True, help_text='write service of your project as a list', null=True)),
                ('location', models.TextField(blank=True, help_text='write loaction about your project', null=True)),
                ('contractors', models.TextField(blank=True, help_text='write contractors about your project', null=True)),
                ('developer', models.TextField(blank=True, help_text='write developer about your project', null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Scope',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(help_text='title must be in 255 character', max_length=255)),
                ('short_description', models.TextField(blank=True, help_text='write a very short details about your project', null=True)),
                ('long_text', ckeditor_uploader.fields.RichTextUploadingField(blank=True, help_text='write long details about your project', null=True)),
            ],
        ),
        migrations.CreateModel(
            name='ProjectImages',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('images', models.ImageField(blank=True, help_text='upload images for project', null=True, upload_to='file_upload')),
                ('case', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='projectapp.project')),
            ],
        ),
    ]