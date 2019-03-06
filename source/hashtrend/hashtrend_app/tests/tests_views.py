from django.test import TestCase, Client
from django.urls import reverse
from hashtrend_app.models import User
from hashtrend_app.forms import UserCreationForm

# Create your tests here.

# Test homepage
class IndexPageTestCase(TestCase):
	"""
	Testing the homepage.
	"""
	def test_index_page(self):
		"""
		If http 200 or 302 status code
		is returned, test is passed.
		"""
		response = self.client.get(reverse('index'))
		self.assertEqual(response.status_code, 200)



# Test search page
class SearchPageTestCase(TestCase):
	"""
	Testing APIs data
	"""
	def test_search_page_returns_200(self):
		"""
		Try to access the search page with valid query parameters.
		If the request returns a http 200 status code, test is ok.
		"""
		response = self.client.get(reverse('hashtrend:search'), {"query":"NASA"})
		self.assertEqual(response.status_code, 200)

	def test_search_page_returns_404(self):
		"""
		Try to access the search page with invalid query parameters.
		If the request returns a http 404 status code, test is ok.
		"""
		response = self.client.get(reverse('hashtrend:search'), {"query":""})
		self.assertEqual(response.status_code, 404)



# Test registration page
class RegisterTestPageCase(TestCase):
	"""
	Testing user registration
	"""
	def setUp(self):
		"""
		Temporary data
		"""
		url = reverse('hashtrend:sign_up')
		data = {
				'username':'matt',
				'email':'matt@damon.com',
				'password1':'abcdef123456',
				'password2':'abcdef123456' # pwd confirmation
		}

		self.home_url = (reverse('hashtrend:account'))
		self.response = self.client.post(url, data)

	def test_register_page_returns_200(self):
		"""
		Testing page response. If a http 200 status code
		is returned, test is ok.
		"""
		response = self.client.get(reverse('hashtrend:sign_up'))
		self.assertEqual(response.status_code, 200)

	def test_csrf_token(self):
		"""
		Testing csrf token.
		"""
		response = self.client.get(reverse('hashtrend:sign_up'))
		self.assertContains(response, 'csrfmiddlewaretoken')

	def test_contains_form(self):
		"""
		Testing signup form.
		"""
		response = self.client.get(reverse('hashtrend:sign_up'))
		form = response.context.get('form')
		self.assertIsInstance(form, UserCreationForm)

	def test_user_authentication(self):
		"""
		Testing user authentication.
		"""
		response = self.client.get(self.home_url)
		user = response.context.get('user')
		self.assertTrue(user.is_authenticated)



# Invalid registration test
class InvalidSignupTest(TestCase):
	"""
	Testing an invalid registration.
	"""
	def setUp(self):
		"""
		Simple call
		"""
		url = reverse('hashtrend:sign_up')
		self.response = self.client.post(url, {}) # submit an empty dictionary

	def test_signup_status_code(self):
		"""
		Try to access with invalid data.
		If http 200 status code is returned, test is ok.
		"""
		self.assertEqual(self.response.status_code, 200)

		def test_form_errors(self):
			"""
			Testing error messages in
			registration form.
			"""
			form = self.response.context.get('form')
			self.assertTrue(form.errors)

	def test_dont_create_user(self):
		"""
		Try to access with invalid data.
		Request must return an assert error message.
		"""
		self.assertFalse(User.objects.exists())



# Test login page
class LoginTestPageCase(TestCase):
	"""
	Testing user login.
	"""
	def setUp(self):
		"""
		Temporary data.
		"""
		self.username = "tiesto"
		self.password = hash("12345abcde")
		self.user = User.objects.create_user(username=self.username, password=self.password)

	def test_login_page(self):
		"""
		Testing login page response.
		It must return a http 200 status code.
		"""
		response = self.client.get(reverse('hashtrend:login'))
		self.assertEqual(response.status_code, 200)

	def test_login(self):
		"""
		Try to login with valid data.
		It must return a http 302 code to /login/
		"""
		response = self.client.post(reverse('hashtrend:login'), {
			'username':self.username,
			'password': self.password,
			})
		self.assertEqual(response.status_code, 302)

	def test_login_fake_username(self):
		"""
		Try to login with an invalid username.
		It must return a http 200 status code.
		"""
		response = self.client.post(reverse('hashtrend:login'), {
			'username':' ',
			'password': self.password,
			})
		self.assertEqual(response.status_code, 200)

	def test_login_fake_password(self):
		"""
		Try to login with an invalid username.
		It must return a http 200 status code.
		"""
		response = self.client.post(reverse('hashtrend:login'), {
			'username': self.username,
			'password':'ashfjgh',
			})
		self.assertEqual(response.status_code, 200)

	def test_crsf(self):
		"""
		Testing crsf token.
		"""
		response = self.client.get(reverse('hashtrend:login'))
		self.assertContains(response, 'csrfmiddlewaretoken')



# Test user account page
class AccountTestPageCase(TestCase):
	"""
	Testing user account page.
	"""
	def setUp(self):
		"""
		Temporary data
		"""
		url = reverse('hashtrend:account')
		self.data = {
				'username': 'matt',
				'email': 'matt@damon.com',
				'password': 'abcdef123456',
		}

		self.response = self.client.post(url, self.data)
		self.user = User.objects.create_user(**self.data)

	def test_account_returns_200(self):
		"""
		Try to access account page when logged.
		It must return a http 200 status code.
		"""
		self.client.login(**self.data)
		response = self.client.get(reverse('hashtrend:account'))
		self.assertEqual(response.status_code, 200)

	def test_account_page_redirects(self):
		"""
		Try to access page without being logged.
		It must return a http 302 status code to /account/.
		"""
		response = self.client.get(reverse('hashtrend:account'))
		self.assertEqual(response.status_code, 302)