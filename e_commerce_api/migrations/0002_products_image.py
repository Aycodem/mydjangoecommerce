# Generated by Django 4.1.2 on 2022-12-06 17:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('e_commerce_api', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='products',
            name='image',
            field=models.ImageField(default='default.jpg', upload_to='content'),
        ),
    ]