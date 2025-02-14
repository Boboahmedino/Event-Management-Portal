# Generated by Django 4.1.2 on 2023-04-09 19:15

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('dashboard', '0007_alter_reservation_confirmation'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='reservation',
            name='client',
        ),
        migrations.AddField(
            model_name='reservation',
            name='customer',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]
