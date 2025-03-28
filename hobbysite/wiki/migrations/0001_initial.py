# Generated by Django 5.1.6 on 2025-03-13 08:11

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article_Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('description_field', models.TextField()),
                ('created_on', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'Article Category',
                'verbose_name_plural': 'Article Categories',
                'ordering': ['created_on'],
            },
        ),
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('entry_field', models.TextField()),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('updated_on', models.DateTimeField(auto_now=True)),
                ('article_category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='wiki.article_category')),
            ],
            options={
                'verbose_name': 'Article',
                'verbose_name_plural': 'Articles',
                'ordering': ['-created_on'],
            },
        ),
    ]
