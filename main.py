import sys

from hdwallet.utils import generate_mnemonic

import BTC_WALLET

sys.dont_write_bytecode = True

# Django specific settings
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'settings')
import django
django.setup()

############################################################################
## START OF APPLICATION
############################################################################

print("GOGO!")
while True:
    mnemonic = generate_mnemonic()
    BTC_WALLET.check_mnemonic(mnemonic)



