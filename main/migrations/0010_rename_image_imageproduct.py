# Generated by Django 4.0.1 on 2022-04-04 05:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0009_rename_trend_product_new'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Image',
            new_name='ImageProduct',
        ),
    ]
