# Generated by Django 3.2.6 on 2025-01-02 11:08

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0032_auto_20250102_1506'),
    ]

    operations = [
        migrations.AddField(
            model_name='peerevaluation',
            name='ticket',
            field=models.IntegerField(default=0, help_text='Ticket for the evaluation'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='documents',
            name='document',
            field=models.FileField(upload_to='apps/static/documents/'),
        ),
        migrations.AlterField(
            model_name='peerevaluation',
            name='deadline',
            field=models.DateTimeField(default=datetime.datetime(2025, 1, 9, 16, 38, 7, 230249)),
        ),
    ]
