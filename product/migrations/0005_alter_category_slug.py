# Generated by Django 4.1.3 on 2023-11-18 11:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0004_category_level_category_lft_category_rght_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='slug',
            field=models.SlugField(unique=True),
        ),
    ]