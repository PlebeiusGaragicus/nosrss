#!/bin/bash

echo
echo "This script creates the scraping script and systemd service for a new bot."
read -p "Press Enter to continue or Ctrl+C to cancel."
echo

# SET USERNAME
read -p "nostr-bot username: " username
export NOSPY_USER=$username

export linuxuser=satoshi
export script_filename=/home/$linuxuser/scrape@$NOSPY_USER.sh
export service_filename=/etc/systemd/system/scrape@$NOSPY_USER.service

echo "linuxuser: $linuxuser"
echo "script_filename: $script_filename"
echo "service_filename: $service_filename"

# ./create_scraper.sh
# this runs create_scraper.sh as the satoshi user and therefore it configures satoshi's nospy, not root's
su - $linuxuser -c "/bin/bash ./create_scraper.sh"

./enable_bot.sh
