# steps

(1) be root

- file: `scrape_nyt_frontpage.service`

```
[Unit]
Description=Scrape front page of NYT under TurkeyBiscuit nostr account
After=network.target

[Service]
User=turkeybiscuit
WorkingDirectory=/home/turkeybiscuit
ExecStart=/bin/bash /home/turkeybiscuit/scrape_nyt
Restart=always    

[Install]
WantedBy=multi-user.target
```

- place in: `/etc/systemd/system/`

- essentially run this...: `nano /etc/systemd/system/scrape_nyt_frontpage.service`

```sh
# Run the following command to make systemd aware of your new service:
sudo systemctl daemon-reload

# To start your newly created service, run the following command:
sudo systemctl start scrape_nyt_frontpage.service

# If you want your service to start automatically when the system boots, run the following command:
sudo systemctl enable scrape_nyt_frontpage.service

# To check the status of your service, run the following command:
sudo systemctl status scrape_nyt_frontpage.service
```
