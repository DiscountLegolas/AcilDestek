# Generated by Django 4.1 on 2022-09-04 18:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('BaseUser', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='baseuser',
            name='username',
        ),
    ]
