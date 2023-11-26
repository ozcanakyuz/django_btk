# Generated by Django 4.1.3 on 2023-11-12 12:52

import ckeditor_uploader.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='ContactFormMessage',
        ),
        migrations.AddField(
            model_name='setting',
            name='aboutus',
            field=ckeditor_uploader.fields.RichTextUploadingField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='setting',
            name='contact',
            field=ckeditor_uploader.fields.RichTextUploadingField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='setting',
            name='references',
            field=ckeditor_uploader.fields.RichTextUploadingField(default=0),
            preserve_default=False,
        ),
    ]