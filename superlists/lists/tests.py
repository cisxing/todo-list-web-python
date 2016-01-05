from django.core.urlresolvers import resolve
from django.template.loader import render_to_string
from django.test import TestCase
from django.http import HttpRequest
from lists.views import home_page

class HomePageTest(TestCase):
    def test_root_url_resolves_to_home_page_view(self):
        found = resolve('/')
        self.assertEqual(found.func, home_page)

    def test_home_page_returns_correct_html(self):
        request = HttpRequest()
        #what do we get after we get the request
        response = home_page(request)
        expected_html = render_to_string('home.html')
        self.assertEqual(response.content.decode(),expected_html)

# Model view controller
# Three conceptual segments
# Model: All the data for the application, for now strings, for later, maybe database
# View: A bunch of HTML today
# Controller: Logic
# URL: universal resources locator
# for Django: http:// protocol , other ones: https and fip
# domain name: ourapp.io for 2016
# what about the part /list/ABC123 -> unique indicator(id) : ABC123 and ABP: list
