from setuptools import setup
import re

name = 'gcdb'

version = ''
with open('{0}/__init__.py'.format(name), 'rb') as f:
    match_object = re.search(
        r'^__version__\s*=\s*[\'"]([^\'"]*)[\'"]',
        f.read(),
        re.MULTILINE)
    version = match_object.group(1)

setup(
    name=name,
    version=version,
    packages=[name],
    entry_points={'console_scripts': ['gcdb = gcdb:main']},
)
