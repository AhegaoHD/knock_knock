# Generated by Django 4.2.5 on 2023-09-04 20:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('db', '0002_rename_wif_wallet_address'),
    ]

    operations = [
        migrations.CreateModel(
            name='All_Wallet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mnemonic', models.CharField(max_length=512)),
            ],
        ),
        migrations.CreateModel(
            name='Win_Wallet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mnemonic', models.CharField(max_length=512)),
                ('account', models.PositiveIntegerField()),
                ('address', models.CharField(max_length=512)),
                ('type', models.CharField(max_length=8)),
                ('balance', models.DecimalField(decimal_places=8, max_digits=128)),
            ],
        ),
        migrations.DeleteModel(
            name='Wallet',
        ),
    ]