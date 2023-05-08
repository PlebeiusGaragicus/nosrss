import os
import json
import re
import urllib
from pathlib import Path

import subprocess
import feedparser
from dateutil import parser
# import schedule
import docopt

from nosrss.usage import USAGE
from nosrss.version import VERSION


# FETCH_INTERVAL = 60 * 10 # minutes


def generate_filename(url):
    parsed_url = urllib.parse.urlparse(url)

    # Extract the domain name
    domain_name = parsed_url.netloc

    # Remove 'www.' if present
    if domain_name.startswith("www."):
        domain_name = domain_name[4:]

    # Remove the TLD (Top Level Domain)
    domain_name = domain_name.rsplit(".", 1)[0]

    home = Path.home()
    config_dir = home / ".config" / "nosrss"
    config_dir.mkdir(parents=True, exist_ok=True)
    file_path = config_dir / domain_name

    # return f"{domain_name}"
    return str(file_path)




def fetch_rss_feed(url):
    feed = feedparser.parse(url)
    # print(f"Fetching feed: {url}")

    return feed.entries



def post_to_nostr(title, link):
    # I think this is used to properly escape any quotes in the title and link
    # DO NOT use this.. it ruins apostrophes like "Oppenheimer’s"
    # title = json.dumps(title)[1:-1]
    # link = json.dumps(link)[1:-1]
    title = title.replace('"', '\\"')
    link = link.replace('"', '\\"')

    # print(f"Posting to Nostr:\n{title}\n\n{link}")
    # return

    cmd = f"""nospy publish \"{title}\n\n{link}\""""

    process = subprocess.Popen(cmd, shell=True)
    # TODO: see if nospy exited with an error.. or maybe nospy isn't found.. or something.
    process.wait()




# published
# published_parsed
# updated
# updated_parsed
# title
# title_detail
# content
# summary
# links
# link
# id
# guidislink
# authors
# author_detail
# author
def process_feed(url: str):
    file_name = generate_filename(url)
    entries = fetch_rss_feed(url)

    # Load the last_processed_article from file
    if os.path.exists(file_name):
        with open(file_name, "r") as f:
            last_processed_article = json.load(f)
    else:
        last_processed_article = None



    # Sort entries by published date
    entries.sort(key=lambda entry: parser.parse(entry.published))

    next_newest_article = None

    if last_processed_article:
        last_published_datetime = parser.parse(last_processed_article["published"])

        # Find the next newest article after the last one processed
        for entry in entries:
            entry_published_datetime = parser.parse(entry.published)

            if entry_published_datetime > last_published_datetime:
                next_newest_article = entry
                break

    else:
        next_newest_article = entries[0]  # Post the first article if no last_processed_article found

    if next_newest_article:
        # print(f"Posting article: {next_newest_article.title}")
        post_to_nostr(next_newest_article.title, next_newest_article.link)

        # Save the last_processed_article to file
        with open(file_name, "w") as f:
            json.dump({"id": next_newest_article.id, "published": next_newest_article.published}, f)
    else:
        print("No more articles to post.")








def main():
    args = docopt.docopt(USAGE, version=f"nospy {VERSION}")

    if args.get("version", False):
        print(f"nosrss {VERSION}")
    if args.get("fetch", False):
        url = args.get("--url", None)

        # if url is not None:
        # This regular expression matches the beginning of URLs with either "http://" or "https://" and will also match if "www." is present after the protocol.
        matched = re.match("https?:\/\/(?:www\.)?", url)
        if matched is not None:
            # Do something with the matched URL
            # print(f"URL matched: {url}")
            process_feed(url)
        else:
            print("URL seems improperly formatted")
        # else:
            # print("No URL provided") # I don't think I need this since docopt will handle it







# while True:
#     process_feed()
#     time.sleep(FETCH_INTERVAL)



#     schedule.every(fetch_interval).minutes.do(process_feed)
#     process_feed()
#     while True:
#         schedule.run_pending()
#         time.sleep(60) # NOTE: a fetch_interval less than one minute won't work due to this
