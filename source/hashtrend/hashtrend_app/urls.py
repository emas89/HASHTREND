from django.conf.urls import url
from django.contrib.auth import views as auth_views

from . import views


urlpatterns = [
	url(r'^search/$', views.search, name='search'),
	url(r'^login/$', auth_views.LoginView.as_view(), name='login'),
	url(r'^logout/$', auth_views.LogoutView.as_view(), name='logout'),
	url(r'^register/$', views.sign_up, name='sign_up'),
	url(r'^account/$', views.account, name='account'),
	url(r'^faq/$', views.faq, name='faq')
]