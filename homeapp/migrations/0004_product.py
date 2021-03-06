# Generated by Django 3.2 on 2022-03-12 10:55

import ckeditor_uploader.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homeapp', '0003_auto_20220308_1716'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='title must be in 255 character', max_length=255)),
                ('product_url', models.URLField(blank=True, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='product_image')),
                ('details', ckeditor_uploader.fields.RichTextUploadingField(blank=True, help_text='try not to put very large text', null=True)),
            ],
        ),
    ]
