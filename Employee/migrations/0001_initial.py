# Generated by Django 4.1.4 on 2022-12-20 12:49

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('ExpertUser', '0012_alter_expert_categories_expert_bas_expert_ln_gin_idx'),
        ('BaseUser', '0005_baseuser_is_employee'),
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('employer', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='ExpertUser.expert')),
            ],
            options={
                'verbose_name': 'Employee',
                'verbose_name_plural': 'Employees',
                'db_table': 'Employees',
            },
        ),
    ]
