# Generated by Django 4.0.1 on 2022-04-06 18:37

import ckeditor.fields
import colorful.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Collection',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('image', models.ImageField(upload_to='images')),
            ],
            options={
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='Colors',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('color', colorful.fields.RGBColorField()),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('item_number', models.CharField(max_length=100)),
                ('price', models.PositiveIntegerField(blank=True)),
                ('old_price', models.PositiveIntegerField(blank=True, null=True)),
                ('discount', models.IntegerField(blank=True, default=0)),
                ('description', ckeditor.fields.RichTextField(max_length=1000)),
                ('size', models.CharField(max_length=50)),
                ('material_composition', models.CharField(max_length=100)),
                ('quantity_line', models.PositiveSmallIntegerField(default=0)),
                ('material', models.CharField(max_length=100)),
                ('favorites', models.BooleanField(default=False)),
                ('bestseller', models.BooleanField(default=False)),
                ('new', models.BooleanField(default=True)),
                ('collection', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='main.collection')),
                ('colors', models.ManyToManyField(related_name='product', to='main.Colors')),
            ],
        ),
        migrations.CreateModel(
            name='ImageProduct',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='images')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='images', to='main.product')),
            ],
        ),
    ]
