# Generated by Django 4.1 on 2022-09-20 17:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('PersonalUser', '0004_remove_personalaccount_current_lat_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='personalaccount',
            options={'verbose_name': 'Custome', 'verbose_name_plural': 'Customers'},
        ),
    ]
