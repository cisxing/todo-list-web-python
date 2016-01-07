from django.core.urlresolvers import resolve
from django.template.loader import render_to_string
from django.test import TestCase
from django.http import HttpRequest
from lists.views import home_page
from lists.models import Item

class HomePageTest(TestCase):
    def test_root_url_resolves_to_home_page_view(self):
        found = resolve('/')
        self.assertEqual(found.func, home_page)
    #we failed this test before we change the post['new_item_text'] to post.get('new_item_text','')
    def test_home_page_returns_correct_html(self):
        request = HttpRequest()
        #what do we get after we get the request
        response = home_page(request)
        expected_html = render_to_string('home.html')
        self.assertEqual(response.content.decode(),expected_html)

class NewListTest(TestCase):
    def test_save_a_POST_request(self):
        self.client.post('/lists/new',
        data= {'item_text': 'A new list item'}
        )
        #request = HttpRequest()

        #request.method = 'POST'
        #request.POST['item_text'] = 'A new list item'

        #response = home_page(request)
        self.assertEqual(Item.objects.count(),1)
        new_item = Item.objects.first()
        self.assertEqual(new_item.text, 'A new list item')

    def test_redirect_after_POST(self):

        response = self.client.post('/lists/new',
        data= {'item_text': 'A new list item'}
        )
        self.assertRedirects(response, '/lists/the-only-list/')
        #self.assertEqual(response.status_code, 302)
        #self.assertEqual(response['location'], '/lists/the-only-list/')



class ItemModelTest(TestCase):
    def test_saving_and_retrieving_items(self):
        first_item = Item()
        first_item.text = 'The first (ever) list item'
        first_item.save()

        second_item = Item()
        second_item.text = 'Item the second'
        second_item.save()

        saved_items = Item.objects.all()
        self.assertEqual(saved_items.count(), 2)
        first_saved_item = saved_items[0]
        second_saved_item = saved_items[1]
        self.assertEqual(first_saved_item.text, 'The first (ever) list item')
        self.assertEqual(second_saved_item.text, 'Item the second')


class ListViewTest(TestCase):
    def test_uses_list_template(self):
        response = self.client.get('/lists/the-only-list/')
        self.assertTemplateUsed(response, 'list.html')

    def test_displays_all_items(self):
        Item.objects.create(text='itemey 1')
        Item.objects.create(text='itemey 2')
        response = self.client.get('/lists/the-only-list/')
        self.assertContains(response, 'itemey 1')
        self.assertContains(response, 'itemey 2')
        #404 not found error- because we have not created it yet
# Model view controller
# Three conceptual segments
# Model: All the data for the application, for now strings, for later, maybe database
# View: A bunch of HTML today
# Controller: Logic
# URL: universal resources locator
# for Django: http:// protocol , other ones: https and fip
# domain name: ourapp.io for 2016
# what about the part /list/ABC123 -> unique indicator(id) : ABC123 and ABP: list
