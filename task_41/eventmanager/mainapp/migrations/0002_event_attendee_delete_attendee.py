# Generated by Django 4.2.3 on 2024-06-03 14:46

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('mainapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='attendee',
            field=models.ManyToManyField(related_name='events_attendee', to=settings.AUTH_USER_MODEL),
        ),
        migrations.DeleteModel(
            name='Attendee',
        ),
    ]