import os
import subprocess
import feedparser
import time

def fetch_rss_feed(url):
    feed = feedparser.parse(url)
    print(feed)
    return feed.entries

def post_to_nostr(title, link):
    # Replace 'nostr_cli_app' with the actual command-line application name
    print(f"Posting to Nostr: {title} - {link}")
    # cmd = f"nostr_cli_app --title \"{title}\" --link \"{link}\""
    # process = subprocess.Popen(cmd, shell=True)
    # process.wait()

last_processed_article_id = None

def process_feed():
    global last_processed_article_id
    rss_url = "https://www.theverge.com/rss/index.xml"
    entries = fetch_rss_feed(rss_url)

    if last_processed_article_id is None:
        last_processed_article_id = entries[0].id

    for entry in entries:
        print(entry)
        if entry.id == last_processed_article_id:
            break

        # post_to_nostr(entry.title, entry.link)
        print(f"${entry.title} - {entry.link}")

    last_processed_article_id = entries[0].id

if __name__ == "__main__":
    process_feed()

# fetch_interval = 60  # minutes
# schedule.every(fetch_interval).minutes.do(process_feed)

# if __name__ == "__main__":
#     while True:
#         schedule.run_pending()
#         time.sleep(1)
