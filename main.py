"""main.py file"""
from generator_class import SecretKeyGenerator


def generate_secret_key():
    generator = SecretKeyGenerator()
    return generator.generate()


if __name__ == "__main__":
    generate_secret_key()
