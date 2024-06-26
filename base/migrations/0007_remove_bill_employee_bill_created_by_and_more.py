# Generated by Django 4.2.11 on 2024-04-07 15:54

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0006_bill_employee'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bill',
            name='employee',
        ),
        migrations.AddField(
            model_name='bill',
            name='created_by',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='created_bills', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='bill',
            name='generated_at',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
