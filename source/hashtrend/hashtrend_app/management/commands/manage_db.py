"""
Script to manage Htrend database with latest Pins
from Pinterest through its API in JSON format.
Useful to populate the database and update it.
"""


"""
To run this script run the following command in your terminal:
					manage.py htrend_db"
"""



# Imports
import requests
from django.core.management.base import BaseCommand
from hashtrend_app.models import Photos
from django.db import IntegrityError


# Command
class Command(BaseCommand):
	"""
	Class to handle the "manage.py htrend" command.
	This class populates and updates the Htrend database.
	"""
	help = "Use this script to update the Htrend database with the latest data from Pinterest"
	def handle(self, *args, **kwargs):
		"""
		Handle updating process
		"""

		# Infos about the updating process
		self.stdout.write("Updating Htrend database. Please wait few minutes...", ending='\n')

		# Considered infos about Pins (according to Pinterest doc)
		# (For more details see 'Pinterest_JSON-test-request.png' image in Screenshots project's section)
		