import requests

class PretixAPI:

	def __init__(self, url, token, organizer, event):
		self.url = url
		self.organizer = organizer
		self.event = event
		self.headers = {
			"Accept": "application/json, text/javascript",
			"Authorization": f"Token {token}"
		}

	def get_paginated_result(self, url):
		results = list()
		response = requests.get(url, headers=self.headers).json()
		results.extend(response['results'])
		while response['next'] is not None:
			response = requests.get(response['next'], headers=self.headers).json()
			results.extend(response['results'])
		return results

	def get_orders(self):
		url = f"{self.url}/api/v1/organizers/{self.organizer}/events/{self.event}/orders/"
		return self.get_paginated_result(url)

	def get_products(self):
		url = f"{self.url}/api/v1/organizers/{self.organizer}/events/{self.event}/items/"
		return self.get_paginated_result(url)