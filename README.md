# nostr rss

Inspired by [dergigi](https://dergigi.com/2023/01/19/how-to-build-a-nostr-gm-bot/) and [fiatjaf](https://github.com/fiatjaf/noscl).


# Instructions for setting up an RSS-scraping nostr bot

1. Use a hosted linux server (or whatever spare hardware you have).

## initial setup as `root` user

0. Update, configure, secure and install dependencies.
2. Install `nospy` [available here](https://github.com/plebeiusGaragicus/nospy)
3. Install `nosrss` [available here](https://github.com/plebeiusGaragicus/nosrss)

```sh
# update
apt-get update && apt-get upgrade --yes

# configure
timedatectl set-timezone America/Los_Angeles

# secure
# TODO

# install dependencies
apt-get install git pip curl --yes
apt-get install figlet lolcat --yes
pip install --upgrade pip

# install nospy
cd
git clone https://github.com/PlebeiusGaragicus/nospy.git
cd nospy
pip install -r requirements.txt
pip install .

# install nosrss
cd
git clone https://github.com/PlebeiusGaragicus/nosrss.git
cd nosrss
pip install -r requirements.txt
pip install .


# verify installs
which nospy
nospy version

which nosrss
nosrss version
```

4. Create a new user account that will run your bots using `adduser`

NOTE: **replace** `__USERNAME__` and `__PASSWORD__` below
```sh
# add a new user
adduser --gecos "" __USERNAME__ --disabled-password
echo "__USERNAME__:__PASSWORD__" | chpasswd
```

## setup bot user account

1. Login as the new user you just created.

2. Download needed scripts and make directories.

```sh
curl -s -o ~/run_nostr_bots https://raw.githubusercontent.com/PlebeiusGaragicus/nosrss/main/scripts/run_nostr_bots
chmod +x ~/run_nostr_bots

curl -s -o ~/rss_bot https://raw.githubusercontent.com/PlebeiusGaragicus/nosrss/main/scripts/rss_bot
chmod +x ~/rss_bot

curl -s -o ~/add_rss_bot https://raw.githubusercontent.com/PlebeiusGaragicus/nosrss/main/scripts/add_rss_bot
chmod +x ~/add_rss_bot

mkdir ~/active_bots
mkdir ~/disabled_bots
```

3. Use `./add_rss_bot` to configure a new nospy user and generate a bot .env file.

4. Verify the generated .env file is correct, if so move to `~/active_bots`.

The bot .env file should be in the form:
```sh
# 
export NOSPY_USER=...
export RSS_FEED_URL=...
export BEHAVIOR_SCRIPT=...
```

## setup systemd service as `root` user

1. Login as `root`.

2. Use `./setup_bot_service` to create and run a new `systemd` service

```sh
curl -s -o ~/setup_bot_service https://raw.githubusercontent.com/PlebeiusGaragicus/nosrss/main/scripts/setup_bot_service
chmod +x ~/setup_bot_service
./setup_bot_service
```

...or do it manually...

---

```sh
nano /etc/systemd/system/nostr-bots.service
```

NOTE: use the linux user name you just setup.
```
[Unit]
Description=nostr bot service
After=network.target

[Service]
User=satoshi
WorkingDirectory=/home/satoshi
ExecStart=/bin/bash /home/satoshi/run_nostr_bots
StandardOutput=append:/home/satoshi/nostr-bots.log
StandardError=inherit
Restart=always

[Install]
WantedBy=multi-user.target
```

3. Setup `systemd` to run the bot script

NOTE: use the service name you just setup above

```sh
# make systemd aware of your new service:
systemctl daemon-reload

# start your newly created service
systemctl start nostr-bots.service

# start service automatically when the system boots
systemctl enable nostr-bots.service

# disable a service from starting automatically:
systemctl disable nostr-bots.service
# Removed /etc/systemd/system/multi-user.target.wants/nostr-bots.service

# check the status of your service
systemctl status nostr-bots.service
```
