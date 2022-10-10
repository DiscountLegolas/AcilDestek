# Generated by Django 4.1 on 2022-10-10 18:48

import django.contrib.postgres.indexes
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Category', '0004_remove_servicecategory_level_and_more'),
        ('ExpertUser', '0011_remove_expert_category_expert_categories_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='expert',
            name='categories',
            field=models.ManyToManyField(blank=True, null=True, to='Category.servicecategory', verbose_name='Kategorisi'),
        ),
        migrations.AddIndex(
            model_name='expert',
            index=django.contrib.postgres.indexes.GinIndex(fields=['companyname'], name='bas_expert_ln_gin_idx', opclasses=['gin_trgm_ops']),
        ),
    ]
