# Generated by Django 4.2.14 on 2024-08-02 12:23

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blog', '0012_remove_event_likes'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='likes',
            field=models.ManyToManyField(blank=True, related_name='event_like', to=settings.AUTH_USER_MODEL),
        ),
    ]
