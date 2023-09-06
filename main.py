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
    for address in adresses:
        type_address = check_address(address=address)
        if type_address == 'p2pkh':
                try:
                    p2pkh.objects.create(address=address)
                except:
                    pass
        elif type_address == 'p2sh':
            try:
                p2sh.objects.create(address=address)
            except:
                pass
        elif type_address == 'p2wpkh':
            try:
                p2wpkh.objects.create(address=address)
            except:
                pass
        elif type_address == 'p2wsh':
            try:
                p2wsh.objects.create(address=address)
            except:
                pass
        else:
            try:
                idk.objects.create(address=address)
            except:
                pass

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