# EventbriteBot

Simple Eventbrite Bot to post in facebook page with free seminar in Jakarta, Indonesia. Just a simple bot to educational purpose.

## Requirement
Selenium browser, python, sqlalchemy, and sqlite

## Install
1. Install requirement
2. Copy config.py.sample to config.py and fill with ur FB username and password.
3. Run model.py to create local sqllite db. 
```
python model.py
```
4. Setup cronjob
5. Enjoy

## Automatic Post with Cron

1. Edit crontab
```
crontab -e
```

2. fill the bottom with
```
.
.
# use your own path if dont work or where you put your mozilla geckodrive binary
# PATH=...

# absolute location of your project
*/5 * * * * /usr/bin/python ~/Desktop/EventBot/mainbot.py >> ~/cron.log 2>&1
```

Save. Wait for the 5 minutes. Enjoy