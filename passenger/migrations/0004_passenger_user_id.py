# Generated by Django 4.1.7 on 2023-03-29 11:20

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('passenger', '0003_remove_passenger_user_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='passenger',
            name='user_id',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
