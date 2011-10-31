"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""

from django.test import TestCase
from django.test.client import Client
from pair_stairs.stairs.models import Programmer

MICKEY_MOUSE = 'Mickey Mouse'

class TestCreatePairStairs(TestCase):
    def test_should_render_page_to_create_new_pair_stairs(self):
        response = Client().get('/create/')

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'create_stairs.html')

    def test_should_redirect_to_stairs_after_submission(self):
        response = Client().post('/create/', {'programmer_names': MICKEY_MOUSE})

        self.assertRedirects(response, '/stairs/')

    def test_should_pass_programmers_to_stairs_after_submission(self):
        response = Client().post('/create/', {'programmer_names': MICKEY_MOUSE}, follow=True)

        self.assertContains(response, MICKEY_MOUSE)

    def test_should_save_programmers(self):
        Client().post('/create/', {'programmer_names': MICKEY_MOUSE})

        self.assertEquals(Programmer.objects.filter(name = MICKEY_MOUSE).count(), 1)

    def test_should_render_pair_stairs(self):
        response = Client().get('/stairs/')

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'stairs.html')




