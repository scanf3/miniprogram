# Generated by Django 3.2.8 on 2024-03-19 01:01

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AuthUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('open_id', models.CharField(default='', max_length=60)),
                ('createdAt', models.DateTimeField(default=datetime.datetime(2024, 3, 19, 1, 1, 58, 379227))),
            ],
        )
    ]