"""secret_key_generator.py file"""
from .generator_class import SecretKeyGenerator


def generate() -> str:
    """
    Returns:
        generator.generate(): secret key (str)
    """
    generator = SecretKeyGenerator()
    return generator.generate()
