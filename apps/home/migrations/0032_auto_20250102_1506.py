# Generated by Django 3.2.6 on 2025-01-02 09:36

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0031_auto_20250102_0927'),
    ]

    operations = [
        migrations.AlterField(
            model_name='documents',
            name='document',
            field=models.FileField(upload_to='static/documents/'),
        ),
        migrations.AlterField(
            model_name='peerevaluation',
            name='deadline',
            field=models.DateTimeField(default=datetime.datetime(2025, 1, 9, 15, 6, 29, 827119)),
        ),
    ]
