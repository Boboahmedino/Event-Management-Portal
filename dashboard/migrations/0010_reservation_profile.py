# Generated by Django 4.1.2 on 2023-04-09 19:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0009_alter_reservation_guest'),
    ]

    operations = [
        migrations.AddField(
            model_name='reservation',
            name='profile',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='dashboard.profile'),
            preserve_default=False,
        ),
    ]
