# Generated by Django 3.2 on 2021-07-11 03:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_remove_appusers_is_active'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appusers',
            name='phone',
            field=models.BigIntegerField(null=True),
        ),
    ]
