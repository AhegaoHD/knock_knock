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
thread5 = Thread(target=gogo)
thread6 = Thread(target=gogo)
thread7 = Thread(target=gogo)
thread8 = Thread(target=gogo)
thread9 = Thread(target=gogo)
thread10 = Thread(target=gogo)
thread11 = Thread(target=gogo)
thread12 = Thread(target=gogo)
thread13 = Thread(target=gogo)
thread14 = Thread(target=gogo)
thread15 = Thread(target=gogo)
thread16 = Thread(target=gogo)
thread17 = Thread(target=gogo)
thread18 = Thread(target=gogo)
thread19 = Thread(target=gogo)
thread20 = Thread(target=gogo)
thread21 = Thread(target=gogo)
thread22 = Thread(target=gogo)
thread23 = Thread(target=gogo)
thread24 = Thread(target=gogo)
thread25 = Thread(target=gogo)
thread26 = Thread(target=gogo)
thread27 = Thread(target=gogo)
thread28 = Thread(target=gogo)
thread29 = Thread(target=gogo)
print(my_checked_mnemonic.objects.all().count())

thread0.start()
thread1.start()
thread2.start()
thread3.start()
thread4.start()
thread5.start()
thread6.start()
thread7.start()
thread8.start()
thread9.start()
thread10.start()
thread11.start()
thread12.start()
thread13.start()
thread14.start()
thread15.start()
thread16.start()
thread17.start()
thread18.start()
thread19.start()
thread20.start()
thread21.start()
thread22.start()
thread23.start()
thread24.start()
thread25.start()
thread26.start()
thread27.start()
thread28.start()
thread29.start()