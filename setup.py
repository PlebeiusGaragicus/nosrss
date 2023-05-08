from setuptools import setup, find_packages

from nosrss.version import VERSION

setup(
    name='nosrss',
    version=VERSION,
    description='A command-line utility for nostr',
    author='Micah Fullerton',
    author_email='plebeiusgaragicus@gmail.com',
    url='https://github.com/PlebeiusGaragicus/nosrss',
    packages=find_packages(),
    install_requires=[
        # List your app's dependencies here
        'docopt',
        'feedparser',
        'python-dateutil',
        'nospy',
    ],
    classifiers=[
        # Choose classifiers from https://pypi.org/classifiers/
        # TODO:
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
    ],
    entry_points={
        'console_scripts': [
            'nosrss=nosrss:main',
        ],
    },
)
