# script to create a scraping bot

found !(here)[./create_scraper.sh]

# RUN AS `SATOSHI`  
```sh
alias create_bot="curl --silent --output ./create_bot https://raw.githubusercontent.com/plebeiusgaragicus/nosrss/dev/docs/create_bot && /bin/bash ~/create_bot"
```

if [ ! -f ~/create_bot ]; then
    echo "need to download script..."
    curl --silent --output ~/create_bot https://raw.githubusercontent.com/plebeiusgaragicus/nosrss/dev/docs/create_bot
fi
/bin/bash ~/create_bot



```sh
alias create_bot="if [ ! -f ~/create_bot ]; then echo 'need to download script...'; curl --silent --output ~/create_bot https://raw.githubusercontent.com/plebeiusgaragicus/nosrss/dev/docs/create_bot; fi; /bin/bash ~/create_bot"
```



---



# RUN AS ROOT
```sh
alias enable_bot="curl --silent --output ./create_bot https://raw.githubusercontent.com/plebeiusgaragicus/nosrss/dev/docs/enable_bot && /bin/bash ~/enable_bot"
```

if [ ! -f ~/enable_bot ]; then
    echo "need to download script..."
    curl --silent --output ~/enable_bot https://raw.githubusercontent.com/plebeiusgaragicus/nosrss/dev/docs/enable_bot
fi
/bin/bash ~/enable_bot

```sh
alias enable_bot="if [ ! -f ~/enable_bot ]; then echo 'need to download script...'; curl --silent --output ~/enable_bot https://raw.githubusercontent.com/plebeiusgaragicus/nosrss/dev/docs/enable_bot; fi; /bin/bash ~/enable_bot"
```





https://feeds.macrumors.com/MacRumors-All
nsec1zmmgrpxhaa2l0v05rlrtrlk9fkv2aayp38qwvaxca3g92ku2q5squf509x
