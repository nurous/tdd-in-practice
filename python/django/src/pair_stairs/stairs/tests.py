"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""

from django.test import TestCase
from django.test.client import Client

class TestCreatePairStairs(TestCase):
    def test_should_render_page_to_create_new_pair_stairs(self):
        response = Client().get('/create/')

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'create_stairs.html')

    def test_should_redirect_to_stairs_after_submission(self):
        response = Client().post('/create/', {'programmer_names': 'Mickey Mouse'})

        self.assertRedirects(response, '/stairs/')

    def test_should_pass_programmers_to_stairs_after_submission(self):
        response = Client().post('/create/', {'programmer_names': 'Mickey Mouse'}, follow=True)

        self.assertContains(response, 'Mickey Mouse')

    def test_should_render_pair_stairs(self):
        response = Client().get('/stairs/')

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'stairs.html')




