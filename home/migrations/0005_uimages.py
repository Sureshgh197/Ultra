# Generated by Django 3.2 on 2021-07-11 12:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_auto_20210711_0912'),
    ]

    operations = [
        migrations.CreateModel(
            name='UImages',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('imag', models.ImageField(upload_to='pics/')),
            ],
        ),
    ]
