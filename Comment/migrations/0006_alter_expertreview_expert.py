# Generated by Django 4.1.4 on 2022-12-27 20:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ExpertUser', '0014_alter_expert_user'),
        ('Comment', '0005_expertreview_isanonymous'),
    ]

    operations = [
        migrations.AlterField(
            model_name='expertreview',
            name='expert',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reviews', to='ExpertUser.expert', verbose_name='Yorum Yapılan Usta'),
        ),
    ]
