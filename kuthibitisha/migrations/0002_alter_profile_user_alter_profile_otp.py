# Generated by Django 4.0.6 on 2022-09-08 09:42

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('kuthibitisha', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='User',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='profile', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='profile',
            name='otp',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
