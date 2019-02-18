# IMPORTS

from django.shortcuts import render, get_object_or_404, redirect
from django.http import Http404
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.conf import settings

from .forms import SignUpForm
from .models import SavedPhotos

# Tweepy library to access the Twitter API
import tweepy
# Facebook-SDK library to access the Facebook Graph API
import facebook
# News library to access the Google News API
from newsapi import NewsApiClient

# Create your views here.


# INDEX
def index(request):
	"""
	Homepage
	"""
	context = {
	"page_title" : "Accueil"
	}
	return render(request, 'hashtrend/index.html')


################################################
#			TWITTER API INTERACTION			   #
################################################

# Twitter keys to access the API
twitter_access_token = settings.TWITTER_ACCESS_TOKEN
access_secret = settings.ACCESS_SECRET
consumer_key = settings.CONSUMER_KEY
consumer_secret = settings.CONSUMER_SECRET

# Setup tweepy to authenticate with Twitter credentials:
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(twitter_access_token, access_secret)

# Create the API to connect to Twitter with credentials
api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True, compression=True)


################################################
#			FACEBOOK API INTERACTION		   #
################################################

# Facebook keys to access the API
app_id = settings.APP_ID
app_secret = settings.APP_SECRET
fb_access_token = settings.FB_USER_ACCESS_TOKEN

# Create the API to connect to Facebook with app credentials
graph = facebook.GraphAPI(access_token=fb_access_token, version="3.1")


###############################################
#		GOOGLE NEWS API INTERACTION			  #
###############################################

# Google News API key to access the API
news_api_key = settings.NEWS_API_KEY

# Create the API to connect to Google News with API key
newsapi = NewsApiClient(api_key=news_api_key)


# SEARCH QUERIES
def search(request):
	"""
	Search a trend through the form in the homepage.
	Results comes from Twitter 'Standard Search' API,
	Facebook 'Graph' API and Google News API.
	"""
	
	# Query
	query = request.GET.get('query')

	# Search for most popular tweets about user's query
	tweets = tweepy.Cursor(api.search, q=query, lang="en", tweet_mode='extended', include_entities=True, result_type='popular').items(100)

	#fb_data = graph.search(q=query, type='place')

	# Search for most relevant news about user's query
	all_news = newsapi.get_everything(q=query, language='en', sort_by='relevancy')

	context = {
		"tweets": tweets,
		#"fb_data": fb_data
		"all_news": all_news
	}

	return render(request, 'hashtrend/search.html', context)



# USER SIGN UP
def sign_up(request):
	"""
	User registration page
	"""
	if request.method =='POST':
		form = SignUpForm(request.POST)
		# If form is valid
		if form.is_valid():
			form.save()
			username = form.cleaned_data.get('username')
			raw_password = form.cleaned_data.get('password1')
			user = authenticate(username=username, password=raw_password)
			login(request, user)
			return redirect('/hashtrend_app/account')
	else:
		form = SignUpForm()

	# Render
	context = {
		"form": form,
		"title": "Sign up",
		"page_title": "Sign up"
	}
	return render(request, 'hashtrend/sign_up.html', context)


# USER ACCOUNT
@login_required

def account(request):
	"""
	User infos page
	"""

	# Render
	context = {
		"user": request.user,
		"page_title": "Your account"
	}
	return render(request, 'hashtrend/account.html', context)



# FAQ page
def faq(request):
	"""
	Hashtrend FAQ section
	"""
	
	# Render
	return render(request, 'hashtrend/faq.html')