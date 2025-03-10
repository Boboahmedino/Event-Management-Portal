# Generated by Django 4.1.2 on 2022-11-27 10:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0013_user_alter_booking_owner'),
    ]

    operations = [
        migrations.CreateModel(
            name='Owner',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='booking.user')),
            ],
        ),
        migrations.AlterField(
            model_name='booking',
            name='owner',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='booking.owner'),
        ),
    ]
