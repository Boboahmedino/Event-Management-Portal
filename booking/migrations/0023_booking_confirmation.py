# Generated by Django 4.1.2 on 2023-01-29 19:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0022_delete_payment_remove_booking_pay'),
    ]

    operations = [
        migrations.AddField(
            model_name='booking',
            name='confirmation',
            field=models.CharField(default=3, max_length=3),
            preserve_default=False,
        ),
    ]
