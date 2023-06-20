# nostr rss

Inspired by [dergigi](https://dergigi.com/2023/01/19/how-to-build-a-nostr-gm-bot/) and [fiatjaf](https://github.com/fiatjaf/noscl)


# Instructions for setting up an RSS-scraping nostr bot

1. Use a hosted linux server (or whatever spare hardware you have)

## initial setup as `root` user

0. Update and secure the server
1. Install git, upgrade pip
2. Install `nospy` [available here](https://github.com/plebeiusGaragicus/nospy)
3. Install `nosrss` [available here](https://github.com/plebeiusGaragicus/nosrss)
4. Create a new user account that will run your bots using `useradd`


```sh
# update
apt-get update && apt-get upgrade --yes

# configure
timedatectl set-timezone America/Los_Angeles

# secure
# TODO

# install requirements
apt-get install git pip --yes
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

# **replace** `__USERNAME__` and `__PASSWORD__` below
```sh
# add a new user
adduser --gecos "" __USERNAME__ --disabled-password
echo "__USERNAME__:__PASSWORD__" | chpasswd
```

## setup bot user account

1. Login as the new user your just created

2. Setup `nospy` with a private key, add needed relays and ensure profile the is setup

NOTE: `nospy` is now multi-user capable so remember to set `export NOSPY_USER=<nostr_user>` while setting up each bot account with `nospy`

3. Create bot script in home directory - see example:

NOTE: Replace <nostr_user> with the username you setup `nospy` with

NOTE: Replace <RSS_URL> with the URL of the RSS feed you are scraping.

```sh
#!/bin/bash

export NOSPY_USER=<nospy_user>

while true; do
    POST=$(nosrss fetch --url=<RSS_URL>)

    if [ $? -ne 0 ]; then
        echo "Error: nosrss command failed"
        exit 1
    fi

    if [[ -n "$POST" ]]; then
        nospy publish "$POST"
    else
        echo "norsrr did not fetch any new posts."
    fi

    sleep 360 # Sleep for 6 minutes
done
```

4. make executible via: `chmod +x ./<YOUR_SCRIPT>`

## setup system service as `root` user

1. Login as root user

2. Create new `systemd` service file: `nano /etc/systemd/system/<SERVICE_NAME>.service`

NOTE: use the linux user name and script file you just setup for this bot

```
[Unit]
Description=Scrapes some website under XXX nostr account
After=network.target

[Service]
User=<LINUX_USERNAME>
WorkingDirectory=/home/<LINUX_USERNAME>
ExecStart=/bin/bash /home/<LINUX_USERNAME>/<SCRIPT_NAME>
Restart=always

[Install]
WantedBy=multi-user.target
```

3. Setup `systemd` to run the bot script

NOTE: use the service name you just setup above

```sh
# Run the following command to make systemd aware of your new service:
sudo systemctl daemon-reload

# To start your newly created service, run the following command:
sudo systemctl start <SERVICE_NAME>.service

# If you want your service to start automatically when the system boots, run the following command:
sudo systemctl enable <SERVICE_NAME>.service

# disable a service from starting automatically:
sudo systemctl disable <SERVICE_NAME>.service
# Removed /etc/systemd/system/multi-user.target.wants/<SERVICE_NAME>.service

# To check the status of your service, run the following command:
sudo systemctl status <SERVICE_NAME>.service
```
