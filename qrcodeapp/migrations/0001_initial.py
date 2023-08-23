# Generated by Django 4.2.3 on 2023-08-23 06:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='LinkCode',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('link', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='SocialCode',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=40)),
            ],
        ),
        migrations.CreateModel(
            name='WifiCode',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('wifi_name', models.CharField(max_length=100)),
                ('encryiption', models.TextField()),
                ('password', models.CharField(max_length=30)),
            ],
        ),
    ]