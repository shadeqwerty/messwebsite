# Generated by Django 4.2.11 on 2024-05-10 17:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('messwebsite', '0007_alter_menuitem_options'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='review',
            name='food_item',
        ),
        migrations.DeleteModel(
            name='FoodItem',
        ),
    ]