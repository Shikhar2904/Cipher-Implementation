from aes import aes_decrypt_block, aes_encrypt_block
from padding import pad, unpad
import os
def ecb_encrypt(plaintext,key):
    key=list(bytes.fromhex(key))
    plaintext=pad(plaintext)
    ciphertext=[]
    for i in range(0,len(plaintext),16):
        block=plaintext[i:i+16]
        ciphertext.extend(aes_encrypt_block(block,key))
    return bytes(ciphertext).hex()

def ecb_decrypt(ciphertext, key):
    key=list(bytes.fromhex(key))
    ciphertext=list(bytes.fromhex(ciphertext))
    if len(ciphertext) == 0:
        raise ValueError("Ciphertext cannot be empty")
    if len(ciphertext) % 16 != 0:
        raise ValueError("Ciphertext length must be a multiple of 16 bytes")
    plaintext = []
    for i in range(0, len(ciphertext), 16):
        block = ciphertext[i:i + 16]
        decrypted_block = aes_decrypt_block(block, key)
        plaintext.extend(decrypted_block)
    plaintext = unpad(plaintext)
    return plaintext

def cbc_encrypt(plaintext, key):
    key = list(bytes.fromhex(key))
    iv=list(os.urandom(16))
    if len(iv) != 16:
        raise ValueError("IV must be exactly 16 bytes")
    plaintext = pad(plaintext)
    ciphertext = []
    previous_block = iv
    for i in range(0, len(plaintext), 16):
        block = plaintext[i:i + 16]
        xored_block = [
            block[j] ^ previous_block[j]
            for j in range(16)
        ]
        encrypted_block = aes_encrypt_block(xored_block, key)
        ciphertext.extend(encrypted_block)
        previous_block = encrypted_block
    return bytes(iv).hex(),bytes(ciphertext).hex()

def cbc_decrypt(ciphertext, key, iv):
    key = list(bytes.fromhex(key))
    iv = list(bytes.fromhex(iv))
    ciphertext = list(bytes.fromhex(ciphertext))
    if len(iv) != 16:
        raise ValueError("IV must be exactly 16 bytes")
    if len(ciphertext) == 0:
        raise ValueError("Ciphertext cannot be empty")
    if len(ciphertext) % 16 != 0:
        raise ValueError("Ciphertext length must be a multiple of 16 bytes")
    plaintext = []
    previous_block = iv
    for i in range(0, len(ciphertext), 16):
        block = ciphertext[i:i + 16]
        decrypted_block = aes_decrypt_block(block, key)
        plaintext_block = [
            decrypted_block[j] ^ previous_block[j]
            for j in range(16)
        ]
        plaintext.extend(plaintext_block)
        previous_block = block
    return unpad(plaintext)
