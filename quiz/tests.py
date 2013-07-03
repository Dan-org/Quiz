from django.test import TestCase
from django.test.client import Client
from django.core.urlresolvers import reverse

from models import Quiz

class TestViews(TestCase):
	fixtures = ['quiz_testing']

	def test_quizzes(self):
		client = Client()
		response = client.get(reverse('all_quizzes'))
		self.assertEqual(response.status_code, 200)

	def test_quiz(self):
		client = Client()
		response = client.get(reverse('quiz', kwargs={'quiz_id': 1}))
		self.assertEqual(response.status_code, 200)
 
