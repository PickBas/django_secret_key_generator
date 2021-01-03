![Tests-CI](https://github.com/PickBas/django_secret_key_generator/workflows/Tests-CI/badge.svg)
![PyPI release](https://github.com/PickBas/django_secret_key_generator/workflows/PyPI%20release/badge.svg)
# Secret key generator for Django framework

## Installation

    pip install secret-key-generator


## Usage
In your settings.py file:
    
    from secret_key_generator import secret_key_generator
    
    SECRET_KEY = secret_key_generator.generate()
    
## Customize secret key

    SECRET_KEY = secret_key_generator.generate(chars=your_chars_to_use_in_secret_key,
                                               file_name=your_filename,
                                               len_of_secret_key=your_length)
                                               
With **chars** variable the library generates secret key.

**file_name** is used to name a file that is going to contain the secret key.

**len_of_secret_key** is used to set length of secret key
                                               
#### Defaults
    chars: abcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*(-_=+)
    file_name: .secret.txt
    len_of_secret_key: 50
    
## About the library
This library is meant to help you with the generation of secret keys in Django framework. You do not need to generate the secret keys by yourself, and you don't have to worry about keeping the key in a safe place. 

## How does it work?
The library randomly generates a secret key, saves it into a file, and reads the key from the file. Each time you run a Django project, the library checks if there is a file with the correct secret key. If there is, then the library reads it. If there no such file, then the library generates a new secret key and saves it into a new file.
