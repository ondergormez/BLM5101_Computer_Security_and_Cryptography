#!/usr/bin/python3

import unittest
import steganography as steg


class TestSteganography(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print("setUpClass method called!")

    @classmethod
    def tearDownClass(cls):
        print("tearDownClass method called!")

    def setUp(self):
        print('setUp method called!')

    def tearDown(cls):
        print("tearDown method called!")

    def test_hide_data_to_image(self):
        print("Test hide_data_to_image() function starting...")
        data_to_be_hidden = 'Hello World!'
        image_path = "/home/onder/Repos/BLM5101_Computer_Security_and_Cryptography/02-Homework/Homework-2/images/lenna.png"
        steg.hide_data_to_image(data_to_be_hidden, image_path)
        print("Test hide_data_to_image() function finished successfully!")

    def test_select_prime_number_between(self):
        print("Test select_prime_number_between() function starting...")
        m = 10
        l = 20
        p = steg.select_prime_number_between(m, l)
        self.assertTrue(m < p < l)
        print(
            "Test select_prime_number_between() function finished successfully!"
        )

    def test_select_prime_root(self):
        print("Test select_prime_root() function starting...")

        p = 17
        a = steg.select_prime_root(p)
        self.assertTrue(1 < a < p)
        self.assertEqual(14, a)

        p = 6427
        a = steg.select_prime_root(p)
        self.assertTrue(1 < a < p)

        print("Test select_prime_root() function finished successfully!")

    def test_euler_phi_function(self):
        print("Test euler_phi_function() function starting...")
        p = 16
        coprime_number_count = steg.euler_phi_function(p)
        self.assertEqual(8, coprime_number_count)

        p = 60
        coprime_number_count = steg.euler_phi_function(p)
        self.assertEqual(16, coprime_number_count)
        print("Test euler_phi_function() function finished successfully!")

    def test_factorize(self):
        print("Test factorize() function starting...")
        n = 84
        factors = steg.factorize(n)
        self.assertEqual(factors, {2: 2, 3: 1, 7: 1})

        n = 20
        factors = steg.factorize(n)
        self.assertEqual(factors, {2: 2, 5: 1})

        n = 31
        factors = steg.factorize(n)
        self.assertEqual(factors, {31: 1})

        print("Test factorize() function finished successfully!")

    def test_is_prime(self):
        print("Test is_prime() function starting...")
        self.assertEqual(steg.is_prime(2), True)
        self.assertEqual(steg.is_prime(3), True)
        self.assertEqual(steg.is_prime(4), False)
        self.assertEqual(steg.is_prime(5), True)
        self.assertEqual(steg.is_prime(6), False)
        self.assertEqual(steg.is_prime(7), True)
        self.assertEqual(steg.is_prime(8), False)
        self.assertEqual(steg.is_prime(9), False)
        self.assertEqual(steg.is_prime(10), False)
        self.assertEqual(steg.is_prime(11), True)
        self.assertEqual(steg.is_prime(12), False)
        self.assertEqual(steg.is_prime(13), True)
        self.assertEqual(steg.is_prime(14), False)
        self.assertEqual(steg.is_prime(15), False)
        self.assertEqual(steg.is_prime(16), False)
        self.assertEqual(steg.is_prime(17), True)
        self.assertEqual(steg.is_prime(18), False)
        self.assertEqual(steg.is_prime(19), True)
        self.assertEqual(steg.is_prime(20), False)
        self.assertEqual(steg.is_prime(21), False)
        self.assertEqual(steg.is_prime(22), False)
        self.assertEqual(steg.is_prime(23), True)
        self.assertEqual(steg.is_prime(24), False)
        self.assertEqual(steg.is_prime(25), False)
        self.assertEqual(steg.is_prime(26), False)
        self.assertEqual(steg.is_prime(27), False)
        self.assertEqual(steg.is_prime(28), False)
        self.assertEqual(steg.is_prime(29), True)
        self.assertEqual(steg.is_prime(30), False)
        self.assertEqual(steg.is_prime(31), True)
        self.assertEqual(steg.is_prime(32), False)
        self.assertEqual(steg.is_prime(33), False)
        self.assertEqual(steg.is_prime(34), False)
        self.assertEqual(steg.is_prime(35), False)
        self.assertEqual(steg.is_prime(36), False)
        self.assertEqual(steg.is_prime(37), True)
        self.assertEqual(steg.is_prime(38), False)
        self.assertEqual(steg.is_prime(39), False)
        self.assertEqual(steg.is_prime(40), False)
        self.assertEqual(steg.is_prime(41), True)
        self.assertEqual(steg.is_prime(42), False)
        print("Test is_prime() function finished successfully!")

    def test_is_factor_compliance_with_modulo(self):
        print("Test is_factor_compliance_with_modulo() function starting...")
        p = 17
        a = 3
        self.assertEqual(steg.is_factor_compliance_with_modulo(a, p), True)
        print(
            "Test is_factor_compliance_with_modulo() function finished successfully!"
        )

    def test_gcd(self):
        print("Test gcd() function starting...")
        self.assertEqual(steg.gcd(84, 30), 6)
        self.assertEqual(steg.gcd(30, 10), 10)
        self.assertEqual(steg.gcd(24, 6), 6)
        self.assertEqual(steg.gcd(6, 0), 6)
        print("Test gcd() function finished successfully!")

    def test_is_coprime(self):
        print("Test is_coprime() function starting...")
        self.assertEqual(steg.is_coprime(2, 3), True)
        self.assertEqual(steg.is_coprime(3, 5), True)
        self.assertEqual(steg.is_coprime(5, 7), True)
        self.assertEqual(steg.is_coprime(7, 11), True)
        self.assertEqual(steg.is_coprime(11, 13), True)
        self.assertEqual(steg.is_coprime(8, 4), False)
        self.assertEqual(steg.is_coprime(8, 15), True)
        print("Test is_coprime() function finished successfully!")

    def test_get_all_coprime_numbers_up_to_number(self):
        print(
            "Test get_all_coprime_numbers_up_to_number() function starting...")

        number = 16
        coprime_numbers = steg.get_all_coprime_numbers_up_to_number(number)
        self.assertEqual(coprime_numbers, [1, 3, 5, 7, 9, 11, 13, 15])
        self.assertEqual(len(coprime_numbers), steg.euler_phi_function(number))

        print(
            "Test get_all_coprime_numbers_up_to_number() function finished successfully!"
        )

    def test_convert_index_to_xy(self):
        print("Test convert_index_to_xy() function starting...")
        index = 0
        width = 3
        height = 2
        x, y = steg.convert_index_to_xy(index, width)
        self.assertEqual(x, 0)
        self.assertEqual(y, 0)

        index = 1
        width = 3
        height = 2
        x, y = steg.convert_index_to_xy(index, width)
        self.assertEqual(x, 1)
        self.assertEqual(y, 0)

        index = 2
        width = 3
        height = 2
        x, y = steg.convert_index_to_xy(index, width)
        self.assertEqual(x, 2)
        self.assertEqual(y, 0)

        index = 3
        width = 3
        height = 2
        x, y = steg.convert_index_to_xy(index, width)
        self.assertEqual(x, 0)
        self.assertEqual(y, 1)

        index = 4
        width = 3
        height = 2
        x, y = steg.convert_index_to_xy(index, width)
        self.assertEqual(x, 1)
        self.assertEqual(y, 1)

        index = 5
        width = 3
        height = 2
        x, y = steg.convert_index_to_xy(index, width)
        self.assertEqual(x, 2)
        self.assertEqual(y, 1)

        print("Test convert_index_to_xy() function finished successfully!")

    def test_get_padded_length_string(self):
        print("Test get_padded_length_string() function starting...")

        length = 10
        padded_length_string = steg.get_padded_length_string(length)
        self.assertEqual(padded_length_string, '000010')

        length = 500
        padded_length_string = steg.get_padded_length_string(length)
        self.assertEqual(padded_length_string, '000500')

        print(
            "Test get_padded_length_string() function finished successfully!")


if __name__ == '__main__':
    unittest.main()

    # Run only specific test method
    # unittest.main(argv=[''],
    #               defaultTest='TestSteganography.test_hide_data_to_image')
