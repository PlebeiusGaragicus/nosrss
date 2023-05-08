# This line is here so it's exposed as the entrypoint in setup.py
from nosrss.main import main

# putting this here will cause a circular import during 'pip install -e .'
# VERSION = '0.0.1'