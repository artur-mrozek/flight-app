# Generated by Django 4.1.7 on 2023-03-29 11:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('passenger', '0002_passenger_user_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='passenger',
            name='user_id',
        ),
    ]
