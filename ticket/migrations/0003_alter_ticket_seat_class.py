# Generated by Django 4.1.7 on 2023-04-10 14:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ticket', '0002_remove_ticket_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ticket',
            name='seat_class',
            field=models.CharField(choices=[('First', 'First'), ('Business', 'Business'), ('Economy', 'Economy')], default='economy', max_length=10),
        ),
    ]
