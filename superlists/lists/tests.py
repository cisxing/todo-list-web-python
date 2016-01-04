from django.core.urlresolvers import resolve
from django.test import TestCase

# Create your tests here.
from lists.views import home_page

class HomePageTest(TestCase):
    def test_root_url_resolves_to_home_page_view(self):
        found = resolve('/')
        self.assertEqual(found.func, home_page)


# Model view controller
# Three conceptual segments
# Model: All the data for the application, for now strings, for later, maybe database
# View: A bunch of HTML today
# Controller: Logic
# URL: universal resources locator
# for Django: http:// protocol , other ones: https and fip
# domain name: ourapp.io for 2016
# what about the part /list/ABC123 -> unique indicator(id) : ABC123 and ABP: list
