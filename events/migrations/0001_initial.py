# Generated by Django 4.1.6 on 2023-03-14 09:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('subname', models.CharField(max_length=50)),
                ('image', models.ImageField(upload_to='')),
                ('description', models.TextField(max_length=2000)),
                ('startDateTime', models.DateTimeField()),
                ('endDateTime', models.DateTimeField()),
            ],
        ),
    ]
