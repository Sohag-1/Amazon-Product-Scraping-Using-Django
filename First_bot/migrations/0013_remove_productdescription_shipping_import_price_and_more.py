# Generated by Django 4.2.1 on 2023-05-08 03:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('First_bot', '0012_productdescription_total_rating'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='productdescription',
            name='shipping_import_price',
        ),
        migrations.AddField(
            model_name='productdescription',
            name='shipping_import_details',
            field=models.CharField(default='', max_length=100),
        ),
    ]
