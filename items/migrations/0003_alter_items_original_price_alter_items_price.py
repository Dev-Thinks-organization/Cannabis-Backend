# Generated by Django 4.0.3 on 2022-04-01 10:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('items', '0002_remove_benefits_location_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='items',
            name='original_price',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True),
        ),
        migrations.AlterField(
            model_name='items',
            name='price',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True),
        ),
    ]
