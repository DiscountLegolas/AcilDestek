# Generated by Django 4.1.4 on 2022-12-20 12:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BaseUser', '0004_alter_baseuser_managers'),
    ]

    operations = [
        migrations.AddField(
            model_name='baseuser',
            name='is_employee',
            field=models.BooleanField(default=False),
        ),
    ]
