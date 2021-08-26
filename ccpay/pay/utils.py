from Crypto.Cipher import AES
import hashlib
from binascii import hexlify, unhexlify
import base64, re
from Crypto.Cipher import AES
from Crypto import Random
from django.conf import settings

def pad(data):

    """
    ccavenue method to pad data.
    :param data: plain text
    :return: padded data.
    """

    length = 16 - (len(data) % 16)
    data += chr(length)*length
    return data


def unpad(data):

    """
    ccavenue method to unpad data.
    :param data: encrypted data
    :return: plain data
    """
    
    return data[0:-data[-1]]

def encrypt(raw, key):
    raw = pad(raw)
    iv = Random.new().read(AES.block_size)
    cipher = AES.new(bytes(key.encode()), AES.MODE_CBC, iv)
    return base64.b64encode(iv + cipher.encrypt(raw.encode()))

def decrypt(cipher_text, working_key):

    """
    Method decrypt cc-avenue response.
    :param cipher_text: encrypted data
    :param working_key: working data
    :return: list
    """
    cipher_text = base64.b64decode(cipher_text)
    iv = cipher_text[:AES.block_size]
    cipher = AES.new(bytes(working_key.encode()), AES.MODE_CBC, iv)

    plain_data = unpad(cipher.decrypt(cipher_text[AES.block_size:])).decode('utf-8')
    print(plain_data)
    plain_data_list = plain_data.split('&')

    final_pay_list = []
    for data in plain_data_list:

        final_pay_dict = {}
        final_pay_dict[data.split('=')[0]] = data.split('=')[1]

        final_pay_list.append(final_pay_dict)

    return final_pay_list