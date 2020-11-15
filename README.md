![Tests-CI](https://github.com/PickBas/django_secret_key_generator/workflows/Tests-CI/badge.svg)
# Secret key generator for Django framework

### Installation

    pip install secret-key-generator


### Usage:
In your settings.py file:
    
    from secret_key_generator import secret_key_generator
    
    SECRET_KEY = secret_key_generator.generate()
