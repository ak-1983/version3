# Generated by Django 3.2.6 on 2025-01-01 05:29

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0025_auto_20241230_1413'),
    ]

    operations = [
        migrations.AddField(
            model_name='exam',
            name='total_students',
            field=models.IntegerField(default=0, help_text='Total number of students in the batch'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='peerevaluation',
            name='deadline',
            field=models.DateTimeField(default=datetime.datetime(2025, 1, 8, 10, 59, 32, 193631)),
        ),
    ]
