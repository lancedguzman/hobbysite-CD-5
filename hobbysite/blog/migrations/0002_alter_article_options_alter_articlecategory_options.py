# Generated by Django 5.1.7 on 2025-03-13 04:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='article',
            options={'ordering': ['-created_on']},
        ),
        migrations.AlterModelOptions(
            name='articlecategory',
            options={'ordering': ['name']},
        ),
    ]
