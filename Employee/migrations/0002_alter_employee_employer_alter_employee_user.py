# Generated by Django 4.1.4 on 2022-12-27 20:54

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ExpertUser', '0014_alter_expert_user'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Employee', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='employer',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='employees', to='ExpertUser.expert'),
        ),
        migrations.AlterField(
            model_name='employee',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, related_name='emloyeeprofile', serialize=False, to=settings.AUTH_USER_MODEL),
        ),
    ]