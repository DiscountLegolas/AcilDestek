# Generated by Django 4.1 on 2022-10-08 09:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Category', '0004_remove_servicecategory_level_and_more'),
        ('ExpertUser', '0010_alter_openinghours_unique_together'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='expert',
            name='category',
        ),
        migrations.AddField(
            model_name='expert',
            name='categories',
            field=models.ManyToManyField(to='Category.servicecategory', verbose_name='Kategorisi'),
        ),
    ]
