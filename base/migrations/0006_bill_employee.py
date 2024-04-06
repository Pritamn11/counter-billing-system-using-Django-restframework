# Generated by Django 4.2.11 on 2024-04-06 21:46

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0005_bill'),
    ]

    operations = [
        migrations.AddField(
            model_name='bill',
            name='employee',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='bills', to=settings.AUTH_USER_MODEL),
        ),
    ]