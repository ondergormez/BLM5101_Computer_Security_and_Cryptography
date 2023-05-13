#!/usr/bin/python3

import math
import cv2 as open_cv
import random
import os
import numpy as numpy
import matplotlib.pyplot as pyplot

import bitarray

import logging
import logging.config
import yaml

with open(
        '/home/onder/Repos/BLM5101_Computer_Security_and_Cryptography/02-Homework/Homework-2/logger_config.yaml',
        'r') as file:
    config = yaml.safe_load(file.read())
    logging.config.dictConfig(config)

logger = logging.getLogger(__name__)


def hide_data_to_image(data_to_be_hidden, image_path):
    """Entry function"""
    orginal_image = open_cv.imread(image_path, open_cv.IMREAD_GRAYSCALE)
    orginal_image = open_cv.resize(orginal_image, (128, 128))

    print()
    file_name = os.path.basename(image_path)
    logger.info(
        'The \'{0}\' file was read successfully. Features;'.format(file_name))

    height, width = orginal_image.shape
    logger.info('width:  {0}'.format(width))
    logger.info('height: {0}'.format(height))
    logger.info('size:   {0}'.format(orginal_image.size))
    logger.info('')

    logger.info('Original data in ascii length: {0}'.format(
        len(data_to_be_hidden)))
    logger.info('Original data in ascii: {0}'.format(data_to_be_hidden))
    logger.info('')

    data_to_be_hidden = get_padded_length_string(
        len(data_to_be_hidden)) + data_to_be_hidden

    m_data_length_in_bits = len(data_to_be_hidden) * 8
    l_pixel_count = orginal_image.size

    data_in_bits = bitarray.bitarray()
    data_in_bits.frombytes(data_to_be_hidden.encode('utf-8'))

    logger.info('Data to be hidden in ascii length: {0}'.format(
        len(data_to_be_hidden)))
    logger.info('Data to be hidden in ascii: {0}'.format(data_to_be_hidden))
    logger.info('')

    logger.info('Data to be hidden in bits length: {0}'.format(
        data_in_bits.__len__()))
    logger.info('Data to be hidden in bits: {0}'.format(data_in_bits))
    logger.info('')

    p_prime_number = select_prime_number_between(m_data_length_in_bits,
                                                 l_pixel_count)

    a_prime_root = select_prime_root(p_prime_number)

    data_hidden_image = orginal_image.copy()

    for i in range(0, m_data_length_in_bits):
        # yi = a_prime_root^i % p_prime_number
        yi_index = a_prime_root**i % p_prime_number
        logger.info('y{0}: {1}^{2} mod {3} = {4}'.format(
            i, a_prime_root, i, p_prime_number, yi_index))
        data_hidden_image = write_bit_to_image(data_hidden_image, width,
                                               yi_index, data_in_bits[i])

    return p_prime_number, data_hidden_image


# m: Gizlenecek metin uzunluğu
# l: Veri gizlenecek resimdeki piksel sayısı (512 x 512 ise 262144)
# p: Çok büyük bir asal sayı
# Öyleki p; m < p < l şartını sağlasın.
def select_prime_number_between(m, l):
    """Select a prime number between m and l"""

    logger.info('Selecting prime number between {0} and {1}...'.format(m, l))

    while True:
        p = random.randint(m + 1, l - 1)
        if is_prime(p):
            logger.info("Selected prime number: {0}".format(p))
            logger.info('')
            return p


# TODO: Fonksiyon ismi yaptığı işi temsil etmiyor olabilir. Düzeltilecek.
# a değeri üstel şekilde yazıldığında 1'den p - 1'e kadar olan tüm sayıları verebilmelidir.
def select_prime_root(p):
    """Select a prime root for p"""

    coprime_numbers = get_all_coprime_numbers_up_to_number(p - 1)

    logger.info(
        'Finding the divisor that gives the whole set from 1 to {0}...'.format(
            p - 1))
    logger.info('')

    base = 0
    for coprime_number in coprime_numbers:
        if is_factor_compliance_with_modulo(coprime_number, p) == True:
            base = coprime_number
            break

    logger.info('Selected coprime number as base: {0}'.format(base))

    # Aralarında asal olan köklerin arasından, modu en büyük olan seçilir.
    max_value = 0
    for coprime_number in coprime_numbers:
        exponent = coprime_number
        temp = base**exponent % p

        if (max_value < temp):
            max_value = temp

    logger.info('Selected prime root: {0}'.format(max_value))
    return max_value


def extract_data_from_image(image_path, p_prime_number):
    data_hidden_image = open_cv.imread(image_path, open_cv.IMREAD_GRAYSCALE)

    print()
    file_name = os.path.basename(image_path)
    logger.info(
        'The \'{0}\' file was read successfully. Features;'.format(file_name))

    height, width = data_hidden_image.shape
    print('width:  ', width)
    print('height: ', height)
    print('size:   ', data_hidden_image.size)
    print()

    a_prime_root = select_prime_root(p_prime_number)

    data_in_bits = bitarray.bitarray()

    HEADER_LENGTH = 6 * 8
    for i in range(0, HEADER_LENGTH):

        # yi = a_prime_root^i % p_prime_number
        yi_index = a_prime_root**i % p_prime_number
        logger.info('y{0}: {1}^{2} mod {3} = {4}'.format(
            i, a_prime_root, i, p_prime_number, yi_index))

        data_in_bits.append(
            extract_bit_from_image(data_hidden_image, width, height, yi_index))

    print('Data length: ' + data_in_bits.tobytes().decode('utf-8'))

    data_length = int(data_in_bits.tobytes().decode('utf-8')) * 8

    data_in_bits = bitarray.bitarray()
    for i in range(HEADER_LENGTH, data_length + HEADER_LENGTH):

        # yi = a_prime_root^i % p_prime_number
        yi_index = a_prime_root**i % p_prime_number
        logger.info('y{0}: {1}^{2} mod {3} = {4}'.format(
            i, a_prime_root, i, p_prime_number, yi_index))

        data_in_bits.append(
            extract_bit_from_image(data_hidden_image, width, height, yi_index))

    extracted_data = data_in_bits.tobytes().decode('utf-8')
    logger.warn('Extracted data: ' + extracted_data)
    return extracted_data


# Euler's Phi Function, bir sayının kendisinden küçük aralarında asal olan sayıların sayısını verir.
def euler_phi_function(number):
    """Calculate Euler's phi function"""

    coprime_number_count = 1

    # çarpanlarına ayırma işlemi
    factors_dictionary = factorize(number)
    if len(factors_dictionary) == 0:
        return 0

    for factor in factors_dictionary:
        base = factor
        exponent = factors_dictionary[factor]
        coprime_number_count *= (base**exponent - base**(exponent - 1))

    print('Co prime number count between 1 and {} is {}'.format(
        number, coprime_number_count))
    return coprime_number_count


# Çarpanlarına ayırır.
# 20 = 2 x 2 x 5
def factorize(n):
    """Factorize a number"""
    number = n
    factors_dictionary = {}

    while n % 2 == 0:
        factors_dictionary[2] = factors_dictionary.get(2, 0) + 1
        n //= 2

    f = 3
    while f * f <= n:
        if n % f == 0:
            factors_dictionary[f] = factors_dictionary.get(f, 0) + 1
            n //= f
        else:
            f += 2

    if n != 1:
        factors_dictionary[n] = 1

    print('factor\'s of {} is {}'.format(number, factors_dictionary))
    return factors_dictionary


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


# 1'den p - 1'e kadar olan tüm sayıları kapsıyor mu?
# TODO: Kullanım ve isim uyumsuzluğu var. Düzeltilecek.
def is_factor_compliance_with_modulo(factor, p):
    """Check if a is compliance with modulo"""

    logger.info('Trying coprime number: {0}'.format(factor))

    is_number_present = {}
    for i in range(0, p):
        is_number_present[i] = False

    for i in range(0, p):
        key = (factor**i) % p
        is_number_present[key] = True

        # printing for demonstration
        if (i == 0 or i == 1 or i == p - 2 or i == p - 1):
            logger.info('{0}^{1} mod {2} = {3}'.format(factor, i, p, key))

        if (i == 2):
            logger.info('...')

    is_all_numbers_present = True
    for i in range(1, p):
        if is_number_present[i] == False:
            is_all_numbers_present = False
            break

    if is_all_numbers_present == False:
        logger.warn(
            'The whole set is not covered with the coprime number: {0}'.format(
                factor))
    else:
        logger.info(
            'The whole set is covered with the coprime number: {0}'.format(
                factor))

    logger.info('')

    return is_all_numbers_present


# EBOB: En Büyük Ortak Bölen
# GCD: Greatest Common Divisor
# r0: 84, r1: 30
# r0: 30 * 2 + 24 ve , r0: 30, r1: 24
# r0: 24 * 1 + 6, ve r0: 24, r1: 6
# r0: 6 * 4 + 0, ve r0: 6, r1: 0
# r0: 6, r1: 0
def gcd(r0, r1):
    """Calculate the greatest common divisor of two numbers"""
    while r1 != 0:
        r0, r1 = r1, r0 % r1

    logger.debug('Greatest common divisor: {0}'.format(r0))
    return r0


def is_coprime(n1, n2):
    """Check if two numbers are coprime"""
    return gcd(n1, n2) == 1


def get_all_coprime_numbers_up_to_number(end):
    """Get all coprime numbers up to a number"""

    coprime_numbers = []
    for number in range(1, end):
        if is_coprime(number, end):
            coprime_numbers.append(number)

    logger.info(
        'Coprime number count between {0} and {1} are {2} (Ex: {3}, {4} ... {5}, {6})'
        .format(1, end, coprime_numbers.__len__(), coprime_numbers[0],
                coprime_numbers[1],
                coprime_numbers[coprime_numbers.__len__() - 2],
                coprime_numbers[coprime_numbers.__len__() - 1]))
    logger.debug('Coprime numbers between {0} and {1} are {2}'.format(
        1, end, coprime_numbers))

    return coprime_numbers


def convert_index_to_xy(index, width):
    """Convert index to x, y coordinates"""
    x = index % width
    y = index // width
    return x, y


def write_bit_to_image(data_hidden_image, width, index, bit):
    """Write a bit to image"""

    x, y = convert_index_to_xy(index, width)

    data_hidden_image[x][y] = data_hidden_image[x][y] & 0b11111110 | bit

    return data_hidden_image


def extract_bit_from_image(data_hidden_image, width, height, index):
    """Extract a bit from image"""

    x, y = convert_index_to_xy(index, width)

    bit = data_hidden_image[x][y] & 0b00000001

    return bit


def get_padded_length_string(length):
    """Get padded length string"""

    length_string = str(length)
    length_string = length_string.zfill(6)

    return length_string
