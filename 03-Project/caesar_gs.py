#!/usr/bin/python3

# caesar_gs
# "Caesar" comes from the Caesar Cipher
# "GS" comes from the surnames of Önder Görmez and Enes Doğan Şanlı


@staticmethod
def caesar_encryption_hex(plaintext_hex_string, shift):
    """Encrypt plaintext using Caesar Cipher"""
    ciphertext_hex_string = ""
    for i in range(0, len(plaintext_hex_string), 2):
        hex_value = plaintext_hex_string[i:i + 2]
        int_value = int(hex_value, 16)
        shifted_int_value = (int_value + shift) % 256
        ciphertext_hex_string += format(shifted_int_value, '02X')

    return ciphertext_hex_string


@staticmethod
def caesar_decryption_hex(ciphertext_hex_string, shift):
    """Decrypt ciphertext using Caesar Cipher"""
    plaintext_hex_string = ""
    for i in range(0, len(ciphertext_hex_string), 2):
        hex_value = ciphertext_hex_string[i:i + 2]
        int_value = int(hex_value, 16)
        shifted_int_value = (int_value - shift) % 256
        plaintext_hex_string += format(shifted_int_value, '02X')

    return plaintext_hex_string
