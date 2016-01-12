from django.core.urlresolvers import resolve
from django.http import HttpRequest
from django.template.loader import render_to_string
from django.test import TestCase
from django.utils.html  import escape

from lists.models import Item, List
from lists.views import home_page

class HomePageTest(TestCase):

    def test_root_url_resolves_to_home_page_view(self):

        found = resolve('/')
        self.assertEqual(found.func, home_page)

    def test_home_page_returns_correct_html(self):

        request = HttpRequest()
        response = home_page(request)

        expected_html = render_to_string('home.html')

        self.assertEqual(response.content.decode(), expected_html)


class ListViewTest(TestCase):

    def test_passes_correct_list_to_template(self):
        correct_list = List.objects.create()
        response = self.client.get('/lists/%d/' % (correct_list.id,))
        self.assertEqual(response.context['list'], correct_list)

    def test_uses_list_template(self):
        new_list = List.objects.create()
        response = self.client.get('/lists/%d/' %(new_list.id, ))
        self.assertTemplateUsed(response, 'list.html')

    def test_displays_all_items(self):
        new_list = List.objects.create()
        Item.objects.create(text='itemey 1', list = new_list)
        Item.objects.create(text='itemey 2', list = new_list)
        other_list = List.objects.create()
        Item.objects.create(text='other item 1', list = other_list)
        Item.objects.create(text='other item 2', list = other_list)
        response = self.client.get('/lists/%d/' %(new_list.id, ))
        self.assertContains(response, 'itemey 1')
        self.assertContains(response, 'itemey 2')

        self.assertNotContains(response, 'other item 1')
        self.assertNotContains(response, 'other item 2')
    def test_can_save_a_POST_request_to_an_existing_list(self):
        other_list = List.objects.create()
        correct_list = List.objects.create()

        # Slash for retrieving data, no slash for sending data
        self.client.post(
            '/lists/%d/' % (correct_list.id, ),
            data={'item_text': 'A new item for an existing list'}
        )

        self.assertEqual(Item.objects.count(), 1)
        new_item = Item.objects.first()
        self.assertEqual(new_item.text, 'A new item for an existing list')
        self.assertEqual(new_item.list, correct_list)

    def test_validation_errors_stay_on_list(self):
        current_list = List.objects.create()
        response = self.client.post('/lists/%d/' %(current_list.id,),
        data = {'item_text': ''})
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'list.html')
        expected_error = escape("You can't have an empty list item")
        self.assertContains(response, expected_error)

    def test_invalid_items_arent_saved(self):
        current_list = List.objects.create()
        response = self.client.post('/lists/%d/' %(current_list.id,),
        data = {'item_text': ''})
        self.assertEqual(Item.objects.count(),0)
        #self.assertRedirects(response, '/lists/%d/' % (correct_list.id,))


class NewListTest(TestCase):

    def test_saving_a_POST_request(self):

        self.client.post(
            '/lists/new',
            data={'item_text': 'A new list item'}
        )

        self.assertEqual(Item.objects.count(), 1)

        new_item = Item.objects.first()

        self.assertEqual(new_item.text, 'A new list item')

        self.assertEqual(Item.objects.count(), 1)
        new_item = Item.objects.first()
        self.assertEqual(new_item.text, 'A new list item')

    def test_redirects_after_POST(self):

        response = self.client.post(
            '/lists/new',
            data={'item_text': 'A new list item'}
        )

        new_list = List.objects.first()
        self.assertRedirects(response, '/lists/%d/' %(new_list.id,))
    def test_validation_errors_are_sent_back_to_home_page(self):
        response = self.client.post("/lists/new", data = {'item_text': ''})
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'home.html')
        expected_error = escape("You can't have an empty list item")
        self.assertContains(response, expected_error)

    def test_invalid_items_arent_saved(self):
        self.client.post('/lists/new', data = {'item_text': ''})
        self.assertEqual(List.objects.count(),0)
        self.assertEqual(Item.objects.count(), 0)

# Model view controller
# Three conceptual segments
# Model: All the data for the application, for now strings, for later, maybe database
# View: A bunch of HTML today
# Controller: Logic
# URL: universal resources locator
# for Django: http:// protocol , other ones: https and fip
# domain name: ourapp.io for 2016
# what about the part /list/ABC123 -> unique indicator(id) : ABC123 and ABP: list


##
# First step: What does the website do
# Who is using it
# Create project
# Run test
# Domain name
# What technologies
# Experience
# Security, authentication

# Write a user story
#   -Begining/ middle/ End
#   -Have a problem and solve
#   -maybe around 20- 30 lines of code, using selenium
#Obey the testing goat!


##