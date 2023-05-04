import os
import subprocess
import feedparser
import json
import time

FETCH_INTERVAL = 60 * 10 # minutes

def fetch_rss_feed(url):
    feed = feedparser.parse(url)
    print(f"Fetching feed: {url}")

    # print(f"{feed.keys()}")
    # dict_keys(['bozo', 'entries', 'feed', 'headers', 'etag', 'href', 'status', 'encoding', 'version', 'namespaces'])

    return feed.entries

def post_to_nostr(title, link):
    # Replace 'nostr_cli_app' with the actual command-line application name
    print(f"Posting to Nostr: {title} - {link}")
    # cmd = f"nostr_cli_app --title \"{title}\" --link \"{link}\""
    # process = subprocess.Popen(cmd, shell=True)
    # process.wait()

last_processed_article_id = None

# def process_feed():
#     global last_processed_article_id
#     # rss_url = "https://www.theverge.com/rss/index.xml"
#     rss_url = "https://www.theverge.com/reviews/rss/index.xml"
#     entries = fetch_rss_feed(rss_url)

#     # if last_processed_article_id is None:
#     #     last_processed_article_id = entries[0].id

#     for entry in entries:
#         print(entry['title'], entry['link'])
#     #     if entry.id == last_processed_article_id:
#     #         break

#     #     # post_to_nostr(entry.title, entry.link)
#     #     print(f"${entry.title} - {entry.link}")

#     # last_processed_article_id = entries[0].id


def process_feed():
    print("Processing feed...")
    # Load the last_processed_articles from file
    if os.path.exists("last_processed_articles.json"):
        with open("last_processed_articles.json", "r") as f:
            last_processed_articles = json.load(f)
    else:
        last_processed_articles = []

    # rss_url = "https://www.theverge.com/reviews/rss/index.xml"
    rss_url = "https://www.theverge.com/rss/index.xml"
    entries = fetch_rss_feed(rss_url)

    entries_to_post = []

    for entry in entries:
        if entry.id in last_processed_articles:
            continue

        entries_to_post.append(entry)

    for entry in entries_to_post:
        post_to_nostr(entry.title, entry.link)
        last_processed_articles.append(entry.id)

    # Keep only the last 20 processed articles
    last_processed_articles = last_processed_articles[-20:]

    # Save the last_processed_articles to file
    with open("last_processed_articles.json", "w") as f:
        json.dump(last_processed_articles, f)



if __name__ == "__main__":
    while True:
        process_feed()
        time.sleep(FETCH_INTERVAL)


# if __name__ == "__main__":
#     # fetch_interval = 0.1  # minutes
#     fetch_interval = 10  # minutes
#     schedule.every(fetch_interval).minutes.do(process_feed)

#     process_feed()
#     while True:
#         schedule.run_pending()
#         time.sleep(60) # NOTE: a fetch_interval less than one minute won't work due to this
