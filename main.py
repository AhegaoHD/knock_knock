
import os
import random
import time

from binascii import unhexlify, hexlify
from hashlib import sha256

import base58
import ecdsa
from ecdsa import SECP256k1
from ecdsa.ecdsa import int_to_string
from hdwallet.cryptocurrencies import get_cryptocurrency
from hdwallet.libs.base58 import ensure_string
from hdwallet.libs.bech32 import encode
from hdwallet.libs.ripemd160 import ripemd160

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'settings')
import django
from hdwallet.utils import _unhexlify

django.setup()
from db.models import address_with_money, Win_Wallet

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
def compressed(verified_key) -> str:
        _verified_key = verified_key
        padx = (b"\0" * 32 + int_to_string(
            _verified_key.pubkey.point.x()))[-32:]
        if _verified_key.pubkey.point.y() & 1:
            ck = b"\3" + padx
        else:
            ck = b"\2" + padx
        return hexlify(ck).decode()


def pk_generate_address(private_key):
    private_key = unhexlify(private_key)
    key = ecdsa.SigningKey.from_string(private_key, curve=SECP256k1)
    verified_key = key.get_verifying_key()
    cryptocurrency = get_cryptocurrency(symbol="BTC")
    compressed_verified_key = compressed(verified_key)

    compressed_public_key_p2wsh = unhexlify("5121" + compressed_verified_key + "51ae")
    script_hash = sha256(compressed_public_key_p2wsh).digest()
    p2wsh = ensure_string(encode(cryptocurrency.SEGWIT_ADDRESS.HRP, 0, script_hash))

    compressed_public_key = unhexlify(compressed_verified_key)

    public_key_hash_p2wpkh = ripemd160(sha256(compressed_public_key).digest())
    p2wpkh = ensure_string(encode(cryptocurrency.SEGWIT_ADDRESS.HRP, 0, public_key_hash_p2wpkh))

    public_key_hash = ripemd160(sha256(compressed_public_key).digest())
    network_hash160_bytes = _unhexlify(cryptocurrency.PUBLIC_KEY_ADDRESS) + public_key_hash
    p2pkh = ensure_string(base58.b58encode_check(network_hash160_bytes))

    public_key_hash = hexlify(public_key_hash).decode("utf-8")
    public_key_hash_script = unhexlify("76a914" + public_key_hash + "88ac")
    script_hash = ripemd160(sha256(public_key_hash_script).digest())
    network_hash160_bytes = _unhexlify(cryptocurrency.SCRIPT_ADDRESS) + script_hash
    p2sh = ensure_string(base58.b58encode_check(network_hash160_bytes))

    return [p2pkh,p2sh,p2wpkh,p2wsh]


def generate_random_pk():
    rand_pk = ''.join(random.choice(letters) for i in range(64))
    return rand_pk

from multiprocessing import Process

def test_multiprocessing(count_proc):
    for i in range(count_proc):
        process = Process(target=gogoPK, args=(i,))
        process.start()
        # process.join()
    print('done')


def gogoPK(proc):
    i =0
    while True:
        i+=1
        my_pk = generate_random_pk()
        addresses = pk_generate_address(my_pk)
        for address in addresses:
            if awm.filter(address=address).exists():
                print(my_pk)
                Win_Wallet.objects.create(mnemonic=my_pk,
                                          account=0,
                                          address=address,
                                          type=check_address(address),
                                          )
        if i==1000:
            print(f"Процесс {proc} 100 за {int(time.time())%1000} сек")
            break
letters = '1234567890abcdf'
awm = address_with_money.objects.all()
# print("GOGO")
if __name__ == '__main__':
    print(int(time.time())%1000)
    test_multiprocessing(6)




