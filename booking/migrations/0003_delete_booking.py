# Generated by Django 4.1.2 on 2022-11-18 18:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0002_remove_booking_contact_address_remove_booking_email_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Booking',
        ),
    ]
