# Generated by Django 3.1.2 on 2020-10-03 21:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('questions', '0002_auto_20201003_1629'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='answers',
            name='slug',
        ),
    ]
