from setuptools import setup
from setuptools import find_packages

version = '0.0.3'

with open('README.md', encoding='UTF-8') as f:
    long_description = f.read()

setup(
    name='chacha20poly1305',
    version=version,
    description='Chacha20Poly1305',
    long_description=long_description,
    url='https://github.com/zkonge/chacha20poly1305',
    author='zkonge',
    author_email='zkonge@outlook.com',
    classifiers=[
        'Intended Audience :: Developers',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Topic :: Security',
    ],
    packages=find_packages()
)
