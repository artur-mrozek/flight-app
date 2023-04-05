# Generated by Django 4.1.7 on 2023-04-05 12:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flight', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='flight',
            name='price_business_class',
            field=models.FloatField(default=10.0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='flight',
            name='price_economy_class',
            field=models.FloatField(default=10.0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='flight',
            name='price_first_class',
            field=models.FloatField(default=10.0),
            preserve_default=False,
        ),
    ]