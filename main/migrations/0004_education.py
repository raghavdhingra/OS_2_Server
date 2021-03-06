# Generated by Django 3.1 on 2021-05-09 08:56

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_auto_20210509_0853'),
    ]

    operations = [
        migrations.CreateModel(
            name='Education',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('institute_name', models.CharField(blank=True, default='', max_length=200, null=True)),
                ('from_date', models.DateField(blank=True, default=datetime.date.today, null=True)),
                ('to_date', models.DateField(blank=True, default=datetime.date.today, null=True)),
                ('description', models.TextField(blank=True, default='', null=True)),
                ('gpa', models.IntegerField(blank=True, default=0, null=True)),
            ],
        ),
    ]
