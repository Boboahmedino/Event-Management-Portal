# Generated by Django 4.1.2 on 2022-11-21 11:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='customer',
            old_name='fullname',
            new_name='username',
        ),
    ]
