# Generated by Django 3.2.9 on 2021-12-11 14:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('taskApp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='task2',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('taskname', models.CharField(max_length=30)),
                ('taskdesc', models.TextField()),
                ('slug', models.CharField(max_length=30)),
                ('time', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]