# Generated by Django 3.1.5 on 2021-02-28 14:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('manager', '0010_auto_20210102_1446'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='set',
            name='exercises',
        ),
    ]
