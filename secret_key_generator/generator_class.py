"""generator_class.py module"""

from random import SystemRandom
import os

from secret_key_generator import properties


class SecretKeyGenerator:
    """SecretKeyGenerator class"""

    def __init__(self,
                 chars=properties.DEFAULT_CHARS,
                 file_name=properties.DEFAULT_FILE_NAME,
                 len_of_secret_key=properties.DEFAULT_LENGTH_OF_SECRET_KEY):
        self._chars = chars
        self._secret_key = ""
        self._len_of_secret_key = len_of_secret_key
        self._file_name = file_name
        self._system_random = SystemRandom()

    def _get_random_string(self):
        """
        Getting random string from self._chars.
            This random string is going to be the secret key
        """

        self._secret_key = ''.join(self._system_random.choice(self._chars)
                                   for _ in range(self._len_of_secret_key))

    def get_secret_key_from_file(self) -> str:
        """
        Getting secret key from a file

        Returns:
            secret_key: str
        """

        secret_key_file = open(self._file_name, 'r')
        secret_key = secret_key_file.readline()
        secret_key_file.close()
        return secret_key

    def _validate_secret_key(self, secret_key_to_validate: str):
        """
        Checking if the secret key is valid

        Args:
            secret_key_to_validate: str

        Raises:
            ValueError: if the secret key is invalid
        """

        if len(secret_key_to_validate) != self._len_of_secret_key:
            os.remove(self._file_name)
            raise ValueError

    def _write_secret_key_to_file(self):
        """Writing the secret key to file"""

        secret_key_file = open(self._file_name, 'x')
        secret_key_file.write(self._secret_key)
        secret_key_file.close()

    def generate(self) -> str:
        """
        Processing generation of the secret key

        If the file already contains the correct secret key,
            then this method reads the secret key and returns it.
        If the file already contains an incorrect secret key,
            then this method deletes that file and creates a new one
            with a correct secret key.
        If no file was found,
            then this method creates a new file with the correct secret key.

        Returns:
            str: secret key
        """

        try:
            secret_key_from_file = self.get_secret_key_from_file()
            self._validate_secret_key(secret_key_from_file)
            self._secret_key = secret_key_from_file
        except (FileNotFoundError, ValueError):
            self._get_random_string()
            self._write_secret_key_to_file()

        return self._secret_key
