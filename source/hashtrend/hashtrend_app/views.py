# IMPORTS

from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator
from django.http import Http404
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required

from .forms import SignUpForm
from .models import SavedPhotos

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


# SEARCH QUERIES
def search(request):
	"""
	Search a trend through the form in the homepage.
	Results from Twitter API and Instagram API
	"""
	query = request.GET.get(URL)

	# Render
	context = {
		'query': query,
		'page_title': 'Results'
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