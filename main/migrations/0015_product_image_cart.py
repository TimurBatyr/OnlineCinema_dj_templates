# Generated by Django 4.0.1 on 2022-04-18 08:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0014_alter_cartitem_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='image_cart',
            field=models.ImageField(blank=True, upload_to='images'),
        ),
    ]
