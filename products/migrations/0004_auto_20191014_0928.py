# Generated by Django 2.2.6 on 2019-10-14 07:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_remove_product_shipping_profile'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='meta_descrption',
            field=models.CharField(default='', max_length=160),
        ),
        migrations.AddField(
            model_name='product',
            name='title_tag',
            field=models.CharField(default='', max_length=60),
        ),
    ]
