# Generated by Django 4.2.5 on 2023-09-06 11:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('db', '0004_win_wallet_totalbalance'),
    ]

    operations = [
        migrations.CreateModel(
            name='p2pkh',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.CharField(max_length=34)),
            ],
        ),
        migrations.CreateModel(
            name='p2sh',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.CharField(max_length=34)),
            ],
        ),
        migrations.CreateModel(
            name='p2wpkh',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.CharField(max_length=42)),
            ],
        ),
        migrations.CreateModel(
            name='p2wsh',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.CharField(max_length=62)),
            ],
        ),
    ]
