# Generated by Django 4.0.3 on 2022-05-28 06:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('items', '0004_remove_items_category_items_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='items',
            name='popular_ind',
            field=models.IntegerField(blank=True, max_length=100, null=True),
        ),
    ]
