import unittest

import caesar_gs as caesar_gs


class TestCaesar_GS(unittest.TestCase):

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

    def test_caesar_encryption_hex(self):
        print("Test caesar_encrypt_hex() function starting...")

        hex_string = '47C7B4C58CC7B458C7B4'
        shift = 3
        returned_string = caesar_gs.caesar_encryption_hex(hex_string, shift)
        self.assertEqual("4ACAB7C88FCAB75BCAB7", returned_string)

        print("Test caesar_encrypt_hex() function finished successfully!")

    def test_caesar_decryption_hex(self):
        print("Test caesar_decrypt_hex() function starting...")

        hex_string = '4ACAB7C88FCAB75BCAB7'
        shift = 3
        returned_string = caesar_gs.caesar_decryption_hex(hex_string, shift)
        self.assertEqual("47C7B4C58CC7B458C7B4", returned_string)

        print("Test caesar_decrypt_hex() function finished successfully!")


if __name__ == '__main__':
    unittest.main()
    # Run only specific test method
    # unittest.main(argv=[''], defaultTest='TestRSA_GS.test_generate_key_pair')
