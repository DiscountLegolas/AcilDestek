# Generated by Django 4.1 on 2022-09-04 12:11

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('ExpertUser', '0001_initial'),
        ('PersonalUser', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ExpertReview',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rate', models.FloatField(validators=[django.core.validators.MinValueValidator(0.0), django.core.validators.MaxValueValidator(5.0)])),
                ('expert', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ExpertUser.expert')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='PersonalUser.personalaccount')),
            ],
        ),
        migrations.AddConstraint(
            model_name='expertreview',
            constraint=models.CheckConstraint(check=models.Q(('rate__range', (0, 5))), name='valid_rate'),
        ),
        migrations.AddConstraint(
            model_name='expertreview',
            constraint=models.UniqueConstraint(fields=('user', 'expert'), name='rating_once'),
        ),
    ]
