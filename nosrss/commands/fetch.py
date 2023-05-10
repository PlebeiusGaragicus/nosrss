import sys
import os
import json
import re
import urllib
from pathlib import Path

import logging
logger = logging.getLogger("nosrss")

import subprocess
import feedparser
from dateutil import parser



def generate_filename(url):
    parsed_url = urllib.parse.urlparse(url)

    # Extract the domain name
    domain_name = parsed_url.netloc

    # Get the remaining URL path after the domain name, replace '/' with '_'
    path = parsed_url.path.replace('/', '_')

    # Concatenate domain name and path to get the full name
    full_name = domain_name + path

    config_dir = Path.home() / ".config" / "nosrss"
    config_dir.mkdir(parents=True, exist_ok=True)
    file_path = config_dir / full_name

    return str(file_path)



def fetch_rss_feed(url):
    feed = feedparser.parse(url)

    #logger.debug(feed)
    return feed.entries



# def post_to_nostr(title, link):
#     # escape double quotes
#     title = title.replace('"', '\\"')

#     cmd = f"""nospy publish \"{title}\n\n{link}\""""

#     process = subprocess.Popen(cmd, shell=True)
#     # TODO: see if nospy exited with an error.. or maybe nospy isn't found.. or something.
#     process.wait()



def fetch(args):
    """ TODO:
    """

    url = args.get("--url", None)

    #TODO: I fucked it up... This regular expression matches the beginning of URLs with either "http://" or "https://" and will also match if "www." is present after the protocol.
    matched = re.match("https?:\/\/(?:www\.)?", url)
    if matched is None:
        logger.error("URL seems improperly formatted")
        return
    
    # test_mode = args.get("--test", False)


    file_name = generate_filename(url)
    entries = fetch_rss_feed(url)

    if len(entries) == 0:
        logger.error("Given RSS feed has no entries")
        return

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
        try:
            next_newest_article = entries[0]  # Post the first article if no last_processed_article found
        except IndexError:
            logger.error("Unable to find any articles")
            sys.exit(1)

    if next_newest_article:
        # Save the last_processed_article to file
        with open(file_name, "w") as f:
            json.dump({"id": next_newest_article.id, "published": next_newest_article.published}, f)

        # NOTE: this utility is used to print to the console.  Make sure the file writes before printing
        print(f"{next_newest_article.title}\n\n{next_newest_article.link}")
    else:
        logger.info("No new articles to post.")
