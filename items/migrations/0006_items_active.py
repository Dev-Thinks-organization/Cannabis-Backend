# Generated by Django 4.0.3 on 2022-05-28 06:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('items', '0005_alter_items_popular_ind'),
    ]

    operations = [
        migrations.AddField(
            model_name='items',
            name='active',
            field=models.BooleanField(default=False),
        ),
    ]