# Generated by Django 4.1.6 on 2023-03-14 10:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='venue',
            field=models.TextField(default='MMM', max_length=200),
        ),
    ]