# Generated by Django 4.1.2 on 2022-11-25 10:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('authentication', '0003_delete_customer'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=50)),
                ('address', models.TextField()),
                ('mobile_number', models.CharField(max_length=50)),
                ('password', models.CharField(max_length=6)),
            ],
        ),
    ]
