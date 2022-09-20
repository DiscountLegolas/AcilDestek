# Generated by Django 4.1 on 2022-09-07 18:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ExpertUser', '0003_alter_expert_options_alter_expert_table'),
        ('Comment', '0003_alter_expertreview_options_alter_expertreview_table'),
    ]

    operations = [
        migrations.AlterField(
            model_name='expertreview',
            name='expert',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Expert', to='ExpertUser.expert', verbose_name='Yorum Yapılan Usta'),
        ),
    ]