from django.core.urlresolvers import resolve
from django.test import TestCase
from lists.views import home_page
# Create your tests here.


class SmokeTest(TestCase):

    def test_root_url_resovles_to_homepage_view(self):
        found = resolve('/')
        self.assertEqual(found.func, home_page)
