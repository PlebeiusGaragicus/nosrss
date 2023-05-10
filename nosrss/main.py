import docopt

from nosrss.usage import USAGE
from nosrss.version import VERSION
from nosrss.logger import setup_logging

from nosrss.commands.fetch import fetch

def main():
    setup_logging()

    args = docopt.docopt(USAGE, version=f"nospy {VERSION}")

    if args.get("version", False):
        print(f"nosrss {VERSION}")
    if args.get("fetch", False):
        fetch(args)
