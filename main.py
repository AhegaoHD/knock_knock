import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'settings')
import django
from hdwallet import BIP44HDWallet
from hdwallet.utils import generate_mnemonic

django.setup()
from db.models import address_with_money, my_checked_mnemonic, Win_Wallet
awm = address_with_money.objects.all()

def check_mnemonic(mnemonic:str):
    # print(f"check: {mnemonic}")
    if my_checked_mnemonic.objects.filter(mnemonic = mnemonic).exists():
        print("уже есть")
        return
    my_checked_mnemonic.objects.create(mnemonic = mnemonic)
    addresses = generate_address(mnemonic, 0)
    for address in addresses:
        if awm.filter(address=address).exists():
            Win_Wallet.objects.create(mnemonic=mnemonic,
                                      account=0,
                                      address=address,
                                      type=check_address(address),
                                        )

def check_address(address):
    if address[0:1] == '1' and 26 <= len(address) <= 34:
        return "p2pkh"
    elif address[0:1] == '3' and len(address)==34:
        return "p2sh"
    elif address[0:4] == 'bc1q' and len(address)==42:
        return "p2wpkh"
    elif address[0:4] == 'bc1q' and len(address)==62:
        return "p2wsh"
    else:
        return "idk"
def generate_address(MNEMONIC:str, account:int):
    bip44_hdwallet: BIP44HDWallet = BIP44HDWallet(symbol="BTC", account=account)
    bip44_hdwallet.from_mnemonic(mnemonic=MNEMONIC, language="english")
    return [bip44_hdwallet.p2pkh_address(), bip44_hdwallet.p2sh_address(), bip44_hdwallet.p2wpkh_address(), bip44_hdwallet.p2wsh_address()]

print("GOGO!")
def gogo():
    while True:
        mnemonic = generate_mnemonic()
        check_mnemonic(mnemonic)

from threading import Thread
thread0 = Thread(target=gogo)
thread1 = Thread(target=gogo)
thread2 = Thread(target=gogo)
thread3 = Thread(target=gogo)
thread4 = Thread(target=gogo)


print(my_checked_mnemonic.objects.all().count())

thread0.start()
thread1.start()
thread2.start()
thread3.start()
thread4.start()


