from setuptools import setup, find_packages

from nosrss.version import VERSION

setup(
    name='rss_to_nostr',
    version=VERSION,
    description='A command-line utility for nostr',
    author='Micah Fullerton',
    author_email='plebeiusgaragicus@gmail.com',
    url='https://github.com/PlebeiusGaragicus/rss_to_nostr',
    packages=find_packages(),
    install_requires=[
        # List your app's dependencies here
        'docopt',
        'nospy',
    ],
    classifiers=[
        # Choose classifiers from https://pypi.org/classifiers/
        # TODO:
        "Development Status :: 3 - Alpha",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
    ],
    entry_points={
        'console_scripts': [
            'rss_to_nostr=rss_to_nostr:main',
        ],
    },
)
