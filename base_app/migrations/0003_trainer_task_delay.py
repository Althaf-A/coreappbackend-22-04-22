# Generated by Django 4.0.3 on 2022-04-21 03:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base_app', '0002_create_team_enddate_create_team_startdate'),
    ]

    operations = [
        migrations.AddField(
            model_name='trainer_task',
            name='delay',
            field=models.IntegerField(default=0),
        ),
    ]
