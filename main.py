
import os
import random

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
from hdwallet import BIP44HDWallet
from hdwallet.utils import generate_mnemonic, _unhexlify

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

letters = '1234567890abcdf'
def generate_random_pk():
    rand_pk = ''.join(random.choice(letters) for i in range(64))
    return rand_pk

def check_mnemonic_PK(my_pk:str, awm):
    addresses = pk_generate_address(my_pk)
    for address in addresses:
        if awm.filter(address=address).exists():
            print(my_pk)
            Win_Wallet.objects.create(mnemonic=my_pk,
                                      account=0,
                                      address=address,
                                      type=check_address(address),
                                        )
def gogoPK(i,awm):
    print("зашел1")
    chek = 0
    while True:
        print(f"proc{i}={chek}")
        chek+=1
        my_pk = generate_random_pk()
        check_mnemonic_PK(my_pk, awm)



# if __name__ == "__main__":
#     pool = multiprocessing.Pool(4)
#     results = pool.map(gogoPK)
#     pool.close()
#     pool.join()
#     # freeze_support()
#     # set_start_method('fork')
#     # p0 = Process(target=gogoPK())
#     # p1 = Process(target=gogoPK())
#     # p2 = Process(target=gogoPK())
#     # p3 = Process(target=gogoPK())
#     # p4 = Process(target=gogoPK())
#     # p5 = Process(target=gogoPK())
#     # p6 = Process(target=gogoPK())
#     # p7 = Process(target=gogoPK())
#     # p8 = Process(target=gogoPK())
#     # p9 = Process(target=gogoPK())
#     # p0.start()
#     # p1.start()
#     # p2.start()
#     # p3.start()
#     # p4.start()
#     # p5.start()
#     # p6.start()
#     # p7.start()
#     # p8.start()
#     # p9.start()
#     #
#     # p0.join()
#     # p1.join()
#     # p2.join()
#     # p3.join()
#     # p4.join()
#     # p5.join()
#     # p6.join()
#     # p7.join()
#     # p8.join()
#     # p9.join()

from multiprocessing import Process

def test_multiprocessing(count_proc, my_awm):
    print("зашел")
    for i in range(count_proc):
        p_func1 = Process(target=gogoPK, args=(i,my_awm))
        p_func1.start()

    print('done')

class SimpleClass(object):
    def __init__(self):
        self.count = 0

    def plusplus(self):
        self.count += 1

    def get(self):
        return self.count

if __name__ == '__main__':
    my_awm = address_with_money.objects.all()
    test_multiprocessing(1, my_awm)




