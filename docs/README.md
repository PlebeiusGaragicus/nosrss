# script to create a scraping bot

found !(here)[./create_scraper.sh]

# RUN AS `SATOSHI`  
```sh
alias create_rss_bot="curl --silent --output ~/create_rss_bot https://raw.githubusercontent.com/plebeiusgaragicus/nosrss/main/docs/create_rss_bot && /bin/bash ~/create_rss_bot"


curl --silent --output ~/create_rss_bot https://raw.githubusercontent.com/plebeiusgaragicus/nosrss/main/docs/create_rss_bot
chmod +x create_rss_bot
/bin/bash ~/create_rss_bot
```

if [ ! -f ~/create_rss_bot ]; then
    echo "need to download script..."
    curl --silent --output ~/create_rss_bot https://raw.githubusercontent.com/plebeiusgaragicus/nosrss/main/docs/create_rss_bot
fi
/bin/bash ~/create_rss_bot



```sh
alias create_rss_bot="if [ ! -f ~/create_rss_bot ]; then echo 'need to download script...'; curl --silent --output ~/create_rss_bot https://raw.githubusercontent.com/plebeiusgaragicus/nosrss/main/docs/create_rss_bot; fi; /bin/bash ~/create_rss_bot"
```



---



# RUN AS ROOT
```sh
alias enable_rss_bot="curl --silent --output ~/enable_rss_bot https://raw.githubusercontent.com/plebeiusgaragicus/nosrss/main/docs/enable_rss_bot && /bin/bash ~/enable_rss_bot"

curl --silent --output ~/enable_rss_bot https://raw.githubusercontent.com/plebeiusgaragicus/nosrss/main/docs/enable_rss_bot
chmod +x enable_rss_bot
/bin/bash ~/enable_rss_bot
```

if [ ! -f ~/enable_rss_bot ]; then
    echo "need to download script..."
    curl --silent --output ~/enable_rss_bot https://raw.githubusercontent.com/plebeiusgaragicus/nosrss/main/docs/enable_rss_bot
fi
/bin/bash ~/enable_rss_bot

```sh
alias enable_rss_bot="if [ ! -f ~/enable_rss_bot ]; then echo 'need to download script...'; curl --silent --output ~/enable_rss_bot https://raw.githubusercontent.com/plebeiusgaragicus/nosrss/main/docs/enable_rss_bot; fi; /bin/bash ~/enable_rss_bot"
```
