# Generated by Django 4.1 on 2022-09-24 17:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Category', '0003_remove_servicecategory_parent'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='servicecategory',
            name='level',
        ),
        migrations.RemoveField(
            model_name='servicecategory',
            name='lft',
        ),
        migrations.RemoveField(
            model_name='servicecategory',
            name='rght',
        ),
        migrations.RemoveField(
            model_name='servicecategory',
            name='tree_id',
        ),
    ]
