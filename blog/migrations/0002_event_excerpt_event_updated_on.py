# Generated by Django 4.2.13 on 2024-07-09 10:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='excerpt',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='event',
            name='updated_on',
            field=models.DateTimeField(auto_now=True),
        ),
    ]