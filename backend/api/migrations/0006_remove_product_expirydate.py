# Generated by Django 4.2.4 on 2023-08-12 06:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_alter_product_deliveryoptions_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='expirydate',
        ),
    ]
