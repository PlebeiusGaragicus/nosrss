import os
import subprocess
import feedparser
import json
import docopt

RSS_URL = "https://www.theverge.com/rss/index.xml"

FETCH_INTERVAL = 60 * 10 # minutes
last_processed_article_id = None

def fetch_rss_feed(url):
    feed = feedparser.parse(url)
    print(f"Fetching feed: {url}")

    return feed.entries

def post_to_nostr(title, link):
    print(f"Posting to Nostr: {title} - {link}")

    cmd = f"""nospy publish \"{title}

{link}\""""
    process = subprocess.Popen(cmd, shell=True)
    process.wait()



def process_feed():
    print("Processing feed...")
    # Load the last_processed_articles from file
    if os.path.exists("last_processed_articles.json"):
        with open("last_processed_articles.json", "r") as f:
            last_processed_articles = json.load(f)
    else:
        last_processed_articles = []

    entries = fetch_rss_feed(RSS_URL)

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



def main():
    process_feed()










# while True:
#     process_feed()
#     time.sleep(FETCH_INTERVAL)


# if __name__ == "__main__":
#     # fetch_interval = 0.1  # minutes
#     fetch_interval = 10  # minutes
#     schedule.every(fetch_interval).minutes.do(process_feed)

#     process_feed()
#     while True:
#         schedule.run_pending()
#         time.sleep(60) # NOTE: a fetch_interval less than one minute won't work due to this
