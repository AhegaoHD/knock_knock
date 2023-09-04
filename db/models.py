import sys

try:
    from django.db import models
except Exception:
    print('Exception: Django Not Found, please install it with "pip install django".')
    sys.exit()



# class MNEMONIC(models.Model):
#     MNEMONIC = models.CharField(max_length=512)
class All_Wallet(models.Model):
    mnemonic = models.CharField(max_length=512)
    # balance = models.DecimalField(max_digits=64, decimal_places=8)

class Win_Wallet(models.Model):
    mnemonic = models.CharField(max_length=512)
    account = models.PositiveIntegerField()
    address = models.CharField(max_length=512)
    type = models.CharField(max_length=8)
    balance = models.DecimalField(max_digits=128, decimal_places=8)
    totalbalance = models.DecimalField(max_digits=128, decimal_places=8)
