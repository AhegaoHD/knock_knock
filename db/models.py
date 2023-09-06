import sys

try:
    from django.db import models
except Exception:
    print('Exception: Django Not Found, please install it with "pip install django".')
    sys.exit()



# class MNEMONIC(models.Model):
#     MNEMONIC = models.CharField(max_length=512)
class my_checked_mnemonic(models.Model):
    mnemonic = models.CharField(max_length=512, unique=True, primary_key=True)
    # balance = models.DecimalField(max_digits=64, decimal_places=8)

class Win_Wallet(models.Model):
    mnemonic = models.CharField(max_length=512)
    account = models.PositiveIntegerField()
    address = models.CharField(max_length=512)
    type = models.CharField(max_length=8)

class p2pkh(models.Model):
    address = models.CharField(max_length=34, unique=True, primary_key=True)
class p2sh(models.Model):
    address = models.CharField(max_length=34, unique=True, primary_key=True)
class p2wpkh(models.Model):
    address = models.CharField(max_length=42, unique=True, primary_key=True)
class p2wsh(models.Model):
    address = models.CharField(max_length=62, unique=True, primary_key=True)

class idk(models.Model):
    address = models.CharField(max_length=256, unique=True, primary_key=True)

class last(models.Model):
    height = models.PositiveIntegerField()
    start_height = models.PositiveIntegerField()
    end_height = models.PositiveIntegerField()
    crypto = models.CharField(max_length=16)
    ms = models.CharField()

# class p2pkh_with_money(models.Model):
#     address = models.CharField(max_length=34, unique=True, primary_key=True)
# class p2sh_with_money(models.Model):
#     address = models.CharField(max_length=34, unique=True, primary_key=True)
# class p2wpkh_with_money(models.Model):
#     address = models.CharField(max_length=42, unique=True, primary_key=True)
# class p2wsh_with_money(models.Model):
#     address = models.CharField(max_length=62, unique=True, primary_key=True)
# class idk_with_money(models.Model):
#     address = models.CharField(max_length=256, unique=True, primary_key=True)

class address_with_money(models.Model):
    address = models.CharField(max_length=128, unique=True, primary_key=True)