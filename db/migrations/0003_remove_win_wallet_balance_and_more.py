# Generated by Django 4.2.5 on 2023-09-07 00:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('db', '0002_my_checked_mnemonic_delete_all_wallet'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='win_wallet',
            name='balance',
        ),
        migrations.RemoveField(
            model_name='win_wallet',
            name='totalbalance',
        ),
    ]
