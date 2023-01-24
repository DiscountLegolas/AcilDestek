# Generated by Django 4.1.4 on 2022-12-27 20:54

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('PersonalUser', '0007_personalaccount_previusexpertcalls_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='personalaccount',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, related_name='customerprofile', serialize=False, to=settings.AUTH_USER_MODEL),
        ),
    ]