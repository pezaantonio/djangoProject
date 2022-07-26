# Generated by Django 3.1 on 2022-10-09 04:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_auto_20220724_1936'),
    ]

    operations = [
        migrations.AddField(
            model_name='workoutentry',
            name='exerciseDate',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='workoutentry',
            name='exerciseReps',
            field=models.IntegerField(default='0', max_length=4),
        ),
        migrations.AlterField(
            model_name='workoutentry',
            name='exerciseSets',
            field=models.IntegerField(default='0', max_length=4),
        ),
    ]
