# Generated by Django 4.1 on 2022-09-20 17:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ExpertUser', '0006_remove_expert_closingtime_remove_expert_openingtime'),
    ]

    operations = [
        migrations.AddField(
            model_name='openinghours',
            name='is_closed',
            field=models.BooleanField(default=True),
        ),
    ]