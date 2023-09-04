############################################################################
## Django ORM Standalone Python Template
############################################################################
""" Here we'll import the parts of Django we need. It's recommended to leave
these settings as is, and skip to START OF APPLICATION section below """

# Turn off bytecode generation
import sys

from hdwallet.utils import generate_mnemonic

import BTC_WALLET

sys.dont_write_bytecode = True

# Django specific settings
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'settings')
import django
django.setup()
# Import your models for use in your script


############################################################################
## START OF APPLICATION
############################################################################
""" Replace the code below with your own """


print("GOGO!")
while True:
    mnemonic = generate_mnemonic()
    BTC_WALLET.check_mnemonic(mnemonic)



