# Generated by Django 3.2 on 2021-07-11 03:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_alter_appusers_phone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appusers',
            name='DOB',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='appusers',
            name='first_name',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='appusers',
            name='last_name',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='appusers',
            name='profile_picture',
            field=models.ImageField(null=True, upload_to='profile_pichurs/'),
        ),
        migrations.AlterField(
            model_name='appusers',
            name='username',
            field=models.CharField(max_length=255, null=True),
        ),
    ]
