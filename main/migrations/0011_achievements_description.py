# Generated by Django 3.1 on 2021-05-11 11:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0010_achievements'),
    ]

    operations = [
        migrations.AddField(
            model_name='achievements',
            name='description',
            field=models.TextField(blank=True, default='', null=True),
        ),
    ]