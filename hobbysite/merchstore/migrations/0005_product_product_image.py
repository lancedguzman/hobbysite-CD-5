# Generated by Django 5.1.7 on 2025-03-13 09:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('merchstore', '0004_remove_product_product_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='product_image',
            field=models.CharField(default='images/.jpg', max_length=255),
            preserve_default=False,
        ),
    ]
