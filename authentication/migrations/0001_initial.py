# Generated by Django 4.1.2 on 2022-11-20 22:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fullname', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=50)),
                ('address', models.TextField()),
                ('mobile_number', models.CharField(max_length=50)),
                ('password', models.CharField(max_length=6)),
            ],
        ),
    ]
