import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="secret-key-generator",
    version="0.0.7",
    author="Kirill Sayed",
    author_email="sayed.kirill@gmail.com",
    description="Package for secret key generation in Django framework.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/PickBas/django_secret_key_generator",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
