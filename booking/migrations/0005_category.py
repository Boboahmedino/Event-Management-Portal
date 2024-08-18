# Generated by Django 4.1.2 on 2022-11-21 18:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0004_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=300)),
            ],
            options={
                'verbose_name_plural': 'Categories',
            },
        ),
    ]
