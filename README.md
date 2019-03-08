# Hashtrend - Hashtag your world!
## A Django-based aggregator app
![Hashtrend Homepage](https://github.com/emas89/HASHTREND/blob/master/hashtrend_app/static/hashtrend/images/thumbnail.png)

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
* An user account to get the API keys and acces to their services

## 2. Database
* PostgreSQL with psycopg2-binary database adapter because of Heroku deployment
* Run `manage.py migrate` command to implement the DB structure

## 3. Environment Variables and Heroku Deployment
This project is ready to deploy on Heroku platform. In order to run it, please set the following environment variables:

* `Django Secret Key` -> Secret key used by Django to generate CSRF token;
* PostgreSQL DB name for local use;
* PostgreSQL password for local use;
* PostgreSQL username for local use;
* `ENV` -> App environment: it can be DEVELOPMENT or PRODUCTION.

To deploy the application on Heroku, please set `ENV=PRODUCTION` by using __Heroku Postgres__ and __Whitenoise__.<br>

Heroku deployment assumes that into the project's dependencies there are `requirements.txt` with gunicorn and whitenoise installed, `Procfile` and the `runtime.txt` file (**optional**) to indicate your Python version for the project.
