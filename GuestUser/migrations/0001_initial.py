# Generated by Django 4.1 on 2022-09-23 15:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('ExpertUser', '0010_alter_openinghours_unique_together'),
    ]

    operations = [
        migrations.CreateModel(
            name='GuestUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('long', models.DecimalField(decimal_places=6, default=1.0, max_digits=9)),
                ('lat', models.DecimalField(decimal_places=6, default=1.0, max_digits=9)),
                ('previusexpertcalls', models.ManyToManyField(to='ExpertUser.expert', verbose_name='Önceki Çağrılar')),
            ],
            options={
                'verbose_name': 'GuestUser',
                'verbose_name_plural': 'GuestUsers',
                'db_table': 'GuestUsers',
            },
        ),
    ]