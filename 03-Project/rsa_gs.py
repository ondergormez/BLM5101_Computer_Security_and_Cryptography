#!/usr/bin/python3

# RSA_GS
# "RSA" comes from the surnames of Ron Rivest, Adi Shamir and Leonard Adleman
# "GS" comes from the surnames of Önder Görmez and Enes Doğan Şanlı

# Source: http://www.cs.sjsu.edu/~stamp/CS265/SecurityEngineering/chapter5_SE/RSAmath.html#:~:text=In%20RSA%2C%20we%20have%20two,the%20private%20key%20is%20d.
# In RSA, we have two large primes p and q, a modulus N = pq, an encryption exponent e and a decryption exponent d that satisfy ed = 1 mod (p - 1)(q - 1).
# The public key is the pair (N,e) and the private key is d.

import math
import random
import caesar_gs


class RSA_GS:
    """RSA_GS class"""

    @staticmethod
    def is_prime(n):
        """Check if a number is prime"""
        if n == 2 or n == 3:
            return True
        if n < 2 or n % 2 == 0:
            return False
        if n < 9:
            return True
        if n % 3 == 0:
            return False
        r = int(math.sqrt(n))
        f = 5
        while f <= r:
            if n % f == 0:
                return False
            if n % (f + 2) == 0:
                return False
            f += 6
        return True

    @staticmethod
    def generate_large_prime(bit_length):
        """Generate a large prime number with bit_length bits"""
        while True:
            number = random.getrandbits(bit_length)
            if RSA_GS.is_prime(number):
                print("Generated prime number: ", number)
                return number

    # Modulus represented as N = p * q
    @staticmethod
    def calculate_modulus(p, q):
        """Calculate n = p * q"""
        modulus = p * q
        print("Modulus (N): ", modulus)
        return modulus

    # EBOB: En Büyük Ortak Bölen
    # GCD: Greatest Common Divisor
    # r0: 84, r1: 30
    # r0: 30 * 2 + 24 ve , r0: 30, r1: 24
    # r0: 24 * 1 + 6, ve r0: 24, r1: 6
    # r0: 6 * 4 + 0, ve r0: 6, r1: 0
    # r0: 6, r1: 0
    @staticmethod
    def gcd(r0, r1):
        """Calculate the greatest common divisor of two numbers"""
        while r1 != 0:
            r0, r1 = r1, r0 % r1

        print("Greatest common divisor: ", r0)
        return r0

    @staticmethod
    def is_coprime(n1, n2):
        """Check if two numbers are coprime"""
        return RSA_GS.gcd(n1, n2) == 1

    @staticmethod
    def compute_phi(p, q):
        """Compute Euler's totient function"""

        phi = (p - 1) * (q - 1)
        print("phi: ", phi)
        return phi

    # TODO: Maybe we can the public exponent (e) as 65537 by default
    # e: Public Exponent
    @staticmethod
    def generate_public_exponent(phi):
        """Generate Public Exponent (e)"""
        while True:
            e = random.randrange(2, phi)
            if RSA_GS.is_coprime(e, phi):
                print("Public Exponent (e): ", e)
                return e

    # d: Private Exponent
    @staticmethod
    def generate_private_exponent(public_exponent, phi):
        """Generate Private Exponent (d)"""
        d = 0
        while True:
            d = random.randrange(2, phi)

            # TODO: Check if this is necessary
            if public_exponent == d:
                continue

            if ((d * public_exponent) % phi) == 1:
                print("Private Exponent (d): ", d)
                return d

    @staticmethod
    def generate_key_pair(bit_length, public_exponent=65537):
        """Generate public and private key pair"""
        p = RSA_GS.generate_large_prime(bit_length)
        q = RSA_GS.generate_large_prime(bit_length)

        modulus = RSA_GS.calculate_modulus(p, q)
        phi = RSA_GS.compute_phi(p, q)

        private_exponent = RSA_GS.generate_private_exponent(
            public_exponent, phi)

        return (public_exponent, modulus), (private_exponent, modulus)

    @staticmethod
    def encrypt(public_key, shift, plaintext):
        """Encrypt plaintext using public key"""
        public_exponent, modulus = public_key

        print("Plaintext: ", plaintext)
        plaintext_hex_string = RSA_GS.convert_to_hex_string(plaintext)
        print("Plaintext hex string: ", plaintext_hex_string)

        plaintext_int_array = RSA_GS.convert_to_int_array(plaintext)

        ciphertext_int_array = [0] * len(plaintext_int_array)
        for i in range(0, len(plaintext_int_array)):
            ciphertext_int_array[i] = (plaintext_int_array[i]**
                                       public_exponent) % modulus

        ciphertext_string = RSA_GS.convert_to_string(ciphertext_int_array)
        print("Ciphertext: ", ciphertext_string)
        ciphertext_hex_string = RSA_GS.convert_to_hex_string(ciphertext_string)
        print("Ciphertext hex string: ", ciphertext_hex_string)

        caesar_ciphertext_hex_string = caesar_gs.caesar_encryption_hex(
            ciphertext_hex_string, shift)

        return ciphertext_string, ciphertext_hex_string, plaintext_hex_string, caesar_ciphertext_hex_string

    @staticmethod
    def decrypt(private_key, ciphertext, shift):
        """Decrypt ciphertext using private key"""
        private_exponent, modulus = private_key

        de_ciphertext = caesar_gs.caesar_decryption_hex(ciphertext, shift)

        ciphertext_text = RSA_GS.convert_to_text(de_ciphertext)

        ciphertext_int_array = RSA_GS.convert_to_int_array(ciphertext_text)

        plaintext_int_array = [0] * len(ciphertext_int_array)
        for i in range(0, len(ciphertext_int_array)):
            plaintext_int_array[i] = (ciphertext_int_array[i]**
                                      private_exponent) % modulus

        plaintext_string = RSA_GS.convert_to_string(plaintext_int_array)
        print("Plaintext: ", plaintext_string)
        plaintext_hex_string = RSA_GS.convert_to_hex_string(plaintext_string)
        print("Plaintext hex string: ", plaintext_hex_string)

        return plaintext_string, plaintext_hex_string

    @staticmethod
    def convert_to_hex_string(text):
        """Convert text to hex string"""
        return text.encode("utf-8").hex().upper()

    @staticmethod
    def convert_to_int_array(text):
        """Convert text to int array"""
        return [ord(c) for c in text]

    @staticmethod
    def convert_to_string(int_array):
        """Convert int array to string"""
        return ''.join(chr(i) for i in int_array)

    @staticmethod
    def convert_to_text(hex_string):
        """Convert hex string to text"""
        return bytes.fromhex(hex_string).decode('utf-8')
