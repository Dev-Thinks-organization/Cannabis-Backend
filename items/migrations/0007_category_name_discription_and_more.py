# Generated by Django 4.0.3 on 2022-03-30 13:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('items', '0006_alter_items_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='name_discription',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='category',
            name='parent_discription',
            field=models.TextField(blank=True, null=True),
        ),
    ]
