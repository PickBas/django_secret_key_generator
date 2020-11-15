"""secret_key_generator.py file"""
from . import properties
from .generator_class import SecretKeyGenerator


def generate(chars=properties.DEFAULT_CHARS,
             file_name=properties.DEFAULT_FILE_NAME,
             len_of_secret_key=properties.DEFAULT_LENGTH_OF_SECRET_KEY) -> str:
    """
    Returns:
        generator.generate(): secret key (str)
    """
    generator = SecretKeyGenerator(chars=chars,
                                   file_name=file_name,
                                   len_of_secret_key=len_of_secret_key)
    return generator.generate()
