# Generated by Django 4.2.11 on 2024-04-06 20:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0003_customer_gender'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='age',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
    ]