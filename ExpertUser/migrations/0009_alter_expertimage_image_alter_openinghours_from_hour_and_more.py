# Generated by Django 4.1 on 2022-09-21 21:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ExpertUser', '0008_expertimage'),
    ]

    operations = [
        migrations.AlterField(
            model_name='expertimage',
            name='image',
            field=models.ImageField(upload_to='', verbose_name='Expert Image'),
        ),
        migrations.AlterField(
            model_name='openinghours',
            name='from_hour',
            field=models.TimeField(blank=True, null=True, verbose_name='Opening'),
        ),
        migrations.AlterField(
            model_name='openinghours',
            name='to_hour',
            field=models.TimeField(blank=True, null=True, verbose_name='Closing'),
        ),
    ]