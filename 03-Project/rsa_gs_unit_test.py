import unittest

import rsa_gs


class TestRSA_GS(unittest.TestCase):

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

    def test_is_prime(self):
        print("Test is_prime() function starting...")
        self.assertEqual(rsa_gs.RSA_GS.is_prime(2), True)
        self.assertEqual(rsa_gs.RSA_GS.is_prime(3), True)
        self.assertEqual(rsa_gs.RSA_GS.is_prime(4), False)
        self.assertEqual(rsa_gs.RSA_GS.is_prime(5), True)
        self.assertEqual(rsa_gs.RSA_GS.is_prime(6), False)
        self.assertEqual(rsa_gs.RSA_GS.is_prime(7), True)
        self.assertEqual(rsa_gs.RSA_GS.is_prime(8), False)
        self.assertEqual(rsa_gs.RSA_GS.is_prime(9), False)
        self.assertEqual(rsa_gs.RSA_GS.is_prime(10), False)
        self.assertEqual(rsa_gs.RSA_GS.is_prime(11), True)
        self.assertEqual(rsa_gs.RSA_GS.is_prime(12), False)
        self.assertEqual(rsa_gs.RSA_GS.is_prime(13), True)
        self.assertEqual(rsa_gs.RSA_GS.is_prime(14), False)
        self.assertEqual(rsa_gs.RSA_GS.is_prime(15), False)
        self.assertEqual(rsa_gs.RSA_GS.is_prime(16), False)
        self.assertEqual(rsa_gs.RSA_GS.is_prime(17), True)
        self.assertEqual(rsa_gs.RSA_GS.is_prime(18), False)
        self.assertEqual(rsa_gs.RSA_GS.is_prime(19), True)
        self.assertEqual(rsa_gs.RSA_GS.is_prime(20), False)
        self.assertEqual(rsa_gs.RSA_GS.is_prime(21), False)
        self.assertEqual(rsa_gs.RSA_GS.is_prime(22), False)
        self.assertEqual(rsa_gs.RSA_GS.is_prime(23), True)
        self.assertEqual(rsa_gs.RSA_GS.is_prime(24), False)
        self.assertEqual(rsa_gs.RSA_GS.is_prime(25), False)
        self.assertEqual(rsa_gs.RSA_GS.is_prime(26), False)
        self.assertEqual(rsa_gs.RSA_GS.is_prime(27), False)
        self.assertEqual(rsa_gs.RSA_GS.is_prime(28), False)
        self.assertEqual(rsa_gs.RSA_GS.is_prime(29), True)
        self.assertEqual(rsa_gs.RSA_GS.is_prime(30), False)
        self.assertEqual(rsa_gs.RSA_GS.is_prime(31), True)
        self.assertEqual(rsa_gs.RSA_GS.is_prime(32), False)
        self.assertEqual(rsa_gs.RSA_GS.is_prime(33), False)
        self.assertEqual(rsa_gs.RSA_GS.is_prime(34), False)
        self.assertEqual(rsa_gs.RSA_GS.is_prime(35), False)
        self.assertEqual(rsa_gs.RSA_GS.is_prime(36), False)
        self.assertEqual(rsa_gs.RSA_GS.is_prime(37), True)
        self.assertEqual(rsa_gs.RSA_GS.is_prime(38), False)
        self.assertEqual(rsa_gs.RSA_GS.is_prime(39), False)
        self.assertEqual(rsa_gs.RSA_GS.is_prime(40), False)
        self.assertEqual(rsa_gs.RSA_GS.is_prime(41), True)
        self.assertEqual(rsa_gs.RSA_GS.is_prime(42), False)
        print("Test is_prime() function finished successfully!")

    def test_generate_large_prime(self):
        print("Test generate_large_prime() function starting...")

        for i in range(2, 8):
            self.assertEqual(
                rsa_gs.RSA_GS.is_prime(rsa_gs.RSA_GS.generate_large_prime(i)),
                True)

        print("Test generate_large_prime() function finished successfully!")

    def test_calculate_modulus(self):
        print("Test calculate_modulus() function starting...")
        self.assertEqual(rsa_gs.RSA_GS.calculate_modulus(2, 3), 6)
        self.assertEqual(rsa_gs.RSA_GS.calculate_modulus(3, 5), 15)
        self.assertEqual(rsa_gs.RSA_GS.calculate_modulus(5, 7), 35)
        self.assertEqual(rsa_gs.RSA_GS.calculate_modulus(7, 11), 77)
        self.assertEqual(rsa_gs.RSA_GS.calculate_modulus(11, 13), 143)
        self.assertEqual(rsa_gs.RSA_GS.calculate_modulus(13, 17), 221)
        self.assertEqual(rsa_gs.RSA_GS.calculate_modulus(73, 79), 5767)
        print("Test calculate_modulus() function finished successfully!")

    def test_gcd(self):
        print("Test gcd() function starting...")
        self.assertEqual(rsa_gs.RSA_GS.gcd(84, 30), 6)
        self.assertEqual(rsa_gs.RSA_GS.gcd(30, 10), 10)
        self.assertEqual(rsa_gs.RSA_GS.gcd(24, 6), 6)
        self.assertEqual(rsa_gs.RSA_GS.gcd(6, 0), 6)
        print("Test gcd() function finished successfully!")

    def test_is_coprime(self):
        print("Test is_coprime() function starting...")
        self.assertEqual(rsa_gs.RSA_GS.is_coprime(2, 3), True)
        self.assertEqual(rsa_gs.RSA_GS.is_coprime(3, 5), True)
        self.assertEqual(rsa_gs.RSA_GS.is_coprime(5, 7), True)
        self.assertEqual(rsa_gs.RSA_GS.is_coprime(7, 11), True)
        self.assertEqual(rsa_gs.RSA_GS.is_coprime(11, 13), True)
        self.assertEqual(rsa_gs.RSA_GS.is_coprime(8, 4), False)
        self.assertEqual(rsa_gs.RSA_GS.is_coprime(8, 15), True)
        print("Test is_coprime() function finished successfully!")

    def test_compute_phi(self):
        print("Test compute_phi() function starting...")
        self.assertEqual(rsa_gs.RSA_GS.compute_phi(2, 3), 2)
        self.assertEqual(rsa_gs.RSA_GS.compute_phi(3, 5), 8)
        self.assertEqual(rsa_gs.RSA_GS.compute_phi(5, 7), 24)
        self.assertEqual(rsa_gs.RSA_GS.compute_phi(7, 11), 60)
        self.assertEqual(rsa_gs.RSA_GS.compute_phi(11, 13), 120)
        self.assertEqual(rsa_gs.RSA_GS.compute_phi(13, 17), 192)
        self.assertEqual(rsa_gs.RSA_GS.compute_phi(73, 79), 5616)
        print("Test compute_phi() function finished successfully!")

    # Üretilen public exponent phi değerinden küçük olmalıdır.
    # Public exponent ve phi aralarında asal olmalıdır.
    def test_generate_public_exponent(self):
        print("Test generate_public_exponent() function starting...")

        phi_list = [8, 24, 60, 120, 192, 5616]
        for phi in phi_list:
            public_exponent = rsa_gs.RSA_GS.generate_public_exponent(phi)
            self.assertTrue(public_exponent < phi)
            self.assertTrue(rsa_gs.RSA_GS.is_coprime(public_exponent, phi))

        print(
            "Test generate_public_exponent() function finished successfully!")

    def test_generate_private_exponent(self):
        print("Test generate_private_exponent() function starting...")

        bit_count = 8

        for i in range(1, 6):
            while True:
                p = rsa_gs.RSA_GS.generate_large_prime(bit_count)
                q = rsa_gs.RSA_GS.generate_large_prime(bit_count)

                if p != q:
                    break

            phi = rsa_gs.RSA_GS.compute_phi(p, q)
            public_exponent = rsa_gs.RSA_GS.generate_public_exponent(phi)
            private_exponent = rsa_gs.RSA_GS.generate_private_exponent(
                public_exponent, phi)
            self.assertTrue((private_exponent * public_exponent) % phi == 1)

        print(
            "Test generate_private_exponent() function finished successfully!")

    def test_generate_key_pair(self):
        print("Test generate_key_pair() function starting...")

        bit_count = 8
        public_key, private_key = rsa_gs.RSA_GS.generate_key_pair(bit_count)

        plaintext = 'Merhaba Dünya!'
        shift = 3
        ciphertext_string, ciphertext_hex_string, plaintext_hex_string, caesar_ciphertext_hex_string = rsa_gs.RSA_GS.encrypt(
            public_key, shift, plaintext)
        plaintext_string, plaintext_hex_string = rsa_gs.RSA_GS.decrypt(
            private_key, caesar_ciphertext_hex_string, shift)
        self.assertEqual(plaintext, plaintext_string)

        print("Test generate_key_pair() function finished successfully!")

    def test_convert_to_hex_string(self):
        print("Test convert_to_hex_string() function starting...")

        plaintext = 'Merhaba'
        expected_hex_string = '4D657268616261'
        returned_hex_string = rsa_gs.RSA_GS.convert_to_hex_string(plaintext)
        self.assertEqual(expected_hex_string, returned_hex_string)

        print("Test convert_to_hex_string() function finished successfully!")

    def test_convert_to_int_array(self):
        print("Test convert_to_int_array() function starting...")

        hex_string = 'Merhaba'
        expected_int_array = [77, 101, 114, 104, 97, 98, 97]
        returned_int_array = rsa_gs.RSA_GS.convert_to_int_array(hex_string)
        self.assertEqual(expected_int_array, returned_int_array)

        print("Test convert_to_int_array() function finished successfully!")

    def test_convert_to_string(self):
        print("Test convert_to_string() function starting...")

        int_array = [77, 101, 114, 104, 97, 98, 97]
        expected_string = 'Merhaba'
        returned_string = rsa_gs.RSA_GS.convert_to_string(int_array)
        self.assertEqual(expected_string, returned_string)

        print("Test convert_to_string() function finished successfully!")

    def test_convert_to_text(self):
        print("Test convert_to_text() function starting...")

        hex_string = '44656E656D65'
        returned_string = rsa_gs.RSA_GS.convert_to_text(hex_string)
        print(hex_string, "  ", returned_string)
        self.assertEqual("Deneme", returned_string)

        print("Test convert_to_text() function finished successfully!")

if __name__ == '__main__':
    unittest.main()
    # Run only specific test method
    # unittest.main(argv=[''], defaultTest='TestRSA_GS.test_generate_key_pair')
