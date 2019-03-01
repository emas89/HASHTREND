# Hashtrend - Hashtag your world!
## A Django-based aggregator app
![Hashtrend Homepage](https://github.com/emas89/HASHTREND/blob/master/source/hashtrend/hashtrend_app/static/hashtrend/images/thumbnail.png)

## Mission
### Hashtrend's mission is to use social medias to stay informed on the news, create and share knowledge and awareness among his users.
Turn public posts shared by users and organizations into a comfortable stream of news consultable from a single place. <br>
Sign up or login to start a search and grow your knowledge!

## 1. Requirements
* Python 3.7
* Django 2.1.5
* **pip** package management system to install the dependencies
* PostgreSQL 11.1
* Using a virtual environment is strongly recommended
* Tweepy library to access the Twitter API
* Praw library to access the Reddit API
* News-api library to access the Google News API

## 2. Database
* PostgreSQL with psycopg2 database adapter because of Heroku deployment
* Run `manage.py migrate` command to implement the DB structure
