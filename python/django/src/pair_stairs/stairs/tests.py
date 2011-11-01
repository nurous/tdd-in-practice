"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""

from django.test import TestCase
from django.test.client import Client
from pair_stairs.stairs.models import Programmer

NAMES = ['Mickey Mouse', 'Minnie Mouse']

def format_names(names):
    return ', '.join(names)


class TestCreatePairStairs(TestCase):
    def test_should_render_page_to_create_new_pair_stairs(self):
        response = Client().get('/create/')

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'create_stairs.html')

    def test_should_redirect_to_stairs_after_submission(self):
        response = Client().post('/create/', {'programmer_names': format_names(NAMES)})

        self.assertRedirects(response, '/stairs/')

    def test_should_pass_programmers_to_stairs_after_submission(self):
        response = Client().post('/create/', {'programmer_names': format_names(NAMES)}, follow=True)

        for name in NAMES:
            self.assertContains(response, name)

    def test_should_save_programmers(self):
        Client().post('/create/', {'programmer_names': format_names(NAMES)})

        for name in NAMES:
            self.assertEquals(Programmer.objects.filter(name = name).count(), 1, "Programmer '%s' not found" % name)

    def test_should_render_pair_stairs(self):
        response = Client().get('/stairs/')

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'stairs.html')




