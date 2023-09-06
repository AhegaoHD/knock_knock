import os

import config

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'settings')
import django
django.setup()
import time

import requests
from db.models import p2pkh, p2sh, p2wsh, p2wpkh, idk, last


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

def check_block(height):
    print(f"Check:{height}")
    try:
        response = requests.get("https://blockchain.info/block-height/%s?format=json" % height)
    except:
        print("err")
        return check_block(height)
    if response.status_code == 200:
        respJSON = response.json()
        return respJSON["blocks"][0]['tx']
    else:
        print("BAN")
        time.sleep(60)
        return check_block(height)

def get_address_from_txs(txs):
    addresses = set()
    for tx in txs:
        for ou in tx['out']:
            if 'addr' in ou:
                addresses.add(ou['addr'])
    return addresses

def save_addresses(adresses):
    P2PKH = p2pkh.objects.all()
    P2SH = p2sh.objects.all()
    P2WPKH = p2wpkh.objects.all()
    P2WSH = p2wsh.objects.all()
    IDK = idk.objects.all()
    P2PKH_list = []
    P2SH_list = []
    P2WPKH_list = []
    P2WSH_list = []
    IDK_list = []

    for address in adresses:
        type_address = check_address(address=address)
        if type_address == 'p2pkh':
            if not P2PKH.filter(address=address).exists():
                P2PKH_list.append(p2pkh(address=address))


        elif type_address == 'p2sh':
            if not P2SH.filter(address=address).exists():
                P2SH_list.append(p2sh(address=address))


        elif type_address == 'p2wpkh':
            if not P2WPKH.filter(address=address).exists():
                P2WPKH_list.append(p2wpkh(address=address))


        elif type_address == 'p2wsh':
            if not P2WSH.filter(address=address).exists():
                P2WSH_list.append(p2wsh(address=address))


        else:
            if not IDK.filter(address=address).exists():
                IDK_list.append(idk(address=address))
        try:
            p2pkh.objects.bulk_create(P2PKH_list)
            p2sh.objects.bulk_create(P2SH_list)
            p2wpkh.objects.bulk_create(P2WPKH_list)
            p2wsh.objects.bulk_create(P2WSH_list)
            idk.objects.bulk_create(IDK_list)
        except:
            print("err bulk")
            save_addresses(adresses)

while True:
    block = last.objects.get(crypto='BTC', ms=int(config.MS))
    # time.sleep(0.5)
    save_addresses(get_address_from_txs(check_block(block.height+1)))
    block.height += 1
    block.save()
    if block.height >= block.end_height:
        print("END")
        break

# save_addresses(get_address_from_txs(check_block(200020)))