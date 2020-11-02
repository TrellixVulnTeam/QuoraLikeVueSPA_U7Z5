# Generated by Django 3.1.2 on 2020-10-05 12:51

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('questions', '0003_remove_answers_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='voters',
            field=models.ManyToManyField(related_name='q_voters', to=settings.AUTH_USER_MODEL),
        ),
    ]