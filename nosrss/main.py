import docopt

from nosrss.usage import USAGE
from nosrss.version import VERSION

from nosrss.commands.fetch import fetch

def main():
    args = docopt.docopt(USAGE, version=f"nospy {VERSION}")

    if args.get("version", False):
        print(f"nosrss {VERSION}")
    if args.get("fetch", False):
        fetch(args)
        # url = args.get("--url", None)

        # # This regular expression matches the beginning of URLs with either "http://" or "https://" and will also match if "www." is present after the protocol.
        # matched = re.match("(?:https?:\/\/)?(?:www\.)?", url)
        # if matched is not None:
        #     # Do something with the matched URL
        #     # print(f"URL matched: {url}")
        #     process_feed(url)
        # else:
        #     print("URL seems improperly formatted")
