# Generated by Django 2.2.6 on 2019-10-17 14:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0006_category_meta_description'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='introduction',
        ),
        migrations.RemoveField(
            model_name='category',
            name='meta_description',
        ),
        migrations.RemoveField(
            model_name='product',
            name='date_listed',
        ),
        migrations.RemoveField(
            model_name='product',
            name='gift_wrap',
        ),
        migrations.RemoveField(
            model_name='product',
            name='meta_descrption',
        ),
        migrations.RemoveField(
            model_name='product',
            name='num_fav',
        ),
        migrations.RemoveField(
            model_name='product',
            name='num_sold',
        ),
    ]
