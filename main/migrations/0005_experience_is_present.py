# Generated by Django 3.1 on 2021-05-09 09:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_education'),
    ]

    operations = [
        migrations.AddField(
            model_name='experience',
            name='is_present',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
    ]