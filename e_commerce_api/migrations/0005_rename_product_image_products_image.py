# Generated by Django 4.1.2 on 2022-12-06 17:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('e_commerce_api', '0004_rename_image_products_product_image'),
    ]

    operations = [
        migrations.RenameField(
            model_name='products',
            old_name='product_image',
            new_name='image',
        ),
    ]
