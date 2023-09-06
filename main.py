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

    response = requests.get("https://blockchain.info/block-height/%s?format=json" % height)
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
            addresses.add(ou['addr'])
    return addresses

def save_addresses(adresses):
    for address in adresses:
        type_address = check_address(address=address)
        if type_address == 'p2pkh':
            if not p2pkh.objects.filter(address=address).exists():
                p2pkh.objects.create(address=address)
        elif type_address == 'p2sh':
            if not p2sh.objects.filter(address=address).exists():
                p2sh.objects.create(address=address)
        elif type_address == 'p2wpkh':
            if not p2wpkh.objects.filter(address=address).exists():
                p2wpkh.objects.create(address=address)
        elif type_address == 'p2wsh':
            if not p2wsh.objects.filter(address=address).exists():
                p2wsh.objects.create(address=address)
        else:
            if not idk.objects.filter(address=address).exists():
                idk.objects.create(address=address)

while True:
    block = last.objects.get(crypto='BTC', ms=int(config.MS))
    time.sleep(0.5)
    save_addresses(get_address_from_txs(check_block(block.height+1)))
    block.height += 1
    block.save()
    if block.height >= block.end_height:
        print("END")
        break