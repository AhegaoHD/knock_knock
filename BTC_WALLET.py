import time

from hdwallet import BIP44HDWallet
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'settings')
import django
django.setup()
from db.models import All_Wallet, Win_Wallet
import requests

def check_mnemonic(MNEMONIC:str):
    if All_Wallet.objects.filter(mnemonic = MNEMONIC).exists():
        print("уже есть")
        return
    All_Wallet.objects.create(mnemonic = MNEMONIC)

    for i in range(1):
        addresses = generate_address(MNEMONIC, i)
        for t in addresses:
            time.sleep(0.3)
            balance, totalbalance = check_adr(addresses[t])
            if balance or totalbalance:
                Win_Wallet.objects.create(mnemonic = MNEMONIC,
                                    account = i,
                                    address = addresses[t],
                                    type = t,
                                    balance = balance,
                                    totalbalance=totalbalance)


def generate_address(MNEMONIC:str, account:int) -> dict:
    bip44_hdwallet: BIP44HDWallet = BIP44HDWallet(symbol="BTC", account=account)
    bip44_hdwallet.from_mnemonic(mnemonic=MNEMONIC, language="english")
    return {"p2wpkh":bip44_hdwallet.p2wpkh_address(),"p2pkh":bip44_hdwallet.p2pkh_address(),"p2sh":bip44_hdwallet.p2sh_address()}


def check_adr(adr:str):
    print("Check:",adr)
    response = requests.get("https://blockchain.info/address/%s?format=json" % adr)
    if response.status_code == 200:
        respJSON = response.json()
        return respJSON["final_balance"], respJSON["total_received"]
    else:
        print("BAN")
        time.sleep(60)
        return check_adr(adr)
