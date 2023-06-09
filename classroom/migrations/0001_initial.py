# Generated by Django 4.1.6 on 2023-04-06 16:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='classes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('code', models.CharField(max_length=10)),
                ('year', models.IntegerField()),
                ('sem', models.CharField(choices=[('even', 'even'), ('odd', 'odd')], max_length=5)),
                ('teacher_name', models.CharField(max_length=50)),
                ('description', models.TextField()),
                ('created_time', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
