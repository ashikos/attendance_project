# Generated by Django 4.0.4 on 2022-05-13 09:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('attendance_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='attendance',
            name='days_absents',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='attendance',
            name='days_present',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]