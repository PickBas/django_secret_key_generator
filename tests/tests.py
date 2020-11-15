import os
import unittest

from secret_key_generator import secret_key_generator, properties


class MyTestCase(unittest.TestCase):

    @staticmethod
    def get_secret_key_from_file(filename: str) -> str:
        secret_key_file = open(filename, 'r')
        secret_key_from_file = secret_key_file.readline()
        secret_key_file.close()

        os.remove(filename)

        return secret_key_from_file

    @staticmethod
    def validate_secret_key_with_string(to_validate: str, allowed_chars: str) -> bool:
        for char in to_validate:
            if char not in allowed_chars:
                return False
        return True

    def test_secret_key_generation_default(self):
        secret_key = secret_key_generator.generate()

        self.assertEqual(properties.DEFAULT_LENGTH_OF_SECRET_KEY, len(secret_key))
        self.assertTrue(os.path.isfile(properties.DEFAULT_FILE_NAME))
        self.assertEqual(secret_key, self.get_secret_key_from_file(properties.DEFAULT_FILE_NAME))

    def test_secret_key_generation_custom_len(self):
        len_of_sk = 15
        secret_key = secret_key_generator.generate(len_of_secret_key=len_of_sk)

        self.assertEqual(len_of_sk, len(secret_key))
        self.assertTrue(os.path.isfile(properties.DEFAULT_FILE_NAME))
        self.assertEqual(secret_key, self.get_secret_key_from_file(properties.DEFAULT_FILE_NAME))

    def test_secret_key_generation_custom_chars(self):
        chars = 'asd'
        secret_key = secret_key_generator.generate(chars=chars)

        self.assertEqual(properties.DEFAULT_LENGTH_OF_SECRET_KEY, len(secret_key))
        self.assertTrue(os.path.isfile(properties.DEFAULT_FILE_NAME))
        self.assertEqual(secret_key, self.get_secret_key_from_file(properties.DEFAULT_FILE_NAME))
        self.assertTrue(self.validate_secret_key_with_string(secret_key, chars))

    def test_secret_key_generation_custom_filename(self):
        filename = 'testfile.txt'
        secret_key = secret_key_generator.generate(file_name=filename)

        self.assertEqual(properties.DEFAULT_LENGTH_OF_SECRET_KEY, len(secret_key))
        self.assertTrue(os.path.isfile(filename))
        self.assertEqual(secret_key, self.get_secret_key_from_file(filename))




if __name__ == '__main__':
    unittest.main()
