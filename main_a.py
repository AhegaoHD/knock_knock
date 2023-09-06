import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'settings')
import django
django.setup()
from db.models import address_with_money


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

i=0
addresses = list()
with open("E:\\adress\\Bitcoin_addresses_LATEST.txt", "r") as file:
    while line := file.readline():
        print(i)
        address = line.rstrip()
        addresses.append(address_with_money(address=address))
        i+=1
        if i % 1000 == 0:
            print("add")
            address_with_money.objects.bulk_create(addresses)
            addresses = list()
address_with_money.objects.bulk_create(addresses)