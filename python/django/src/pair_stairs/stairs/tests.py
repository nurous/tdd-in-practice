"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""

from django.test import TestCase
from django.test.client import Client

class TestUrls(TestCase):
    def test_should_render_page_to_create_new_pair_stairs(self):
        response = Client().get('/create/')

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'create_stairs.html')
