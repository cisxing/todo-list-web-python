from django.template.loader import render_to_string
from django.test import TestCase
from lists.models import Item, List
from django.core.exceptions import ValidationError

class ItemAndListModelsTest(TestCase):

    def test_saving_and_retrieving_items_in_list(self):

        new_list = List()
        new_list.save()

        first_item = Item()
        first_item.text = 'The first (ever) list item'
        first_item.list = new_list
        first_item.save()

        second_item = Item()
        second_item.text = 'Item the second'
        second_item.list = new_list
        second_item.save()

        saved_list = List.objects.first()
        self.assertEqual(new_list, saved_list)

        saved_items = Item.objects.all()
        self.assertEqual(saved_items.count(), 2)

        first_saved_item = saved_items[0]
        second_saved_item = saved_items[1]
        self.assertEqual(first_saved_item.text, 'The first (ever) list item')
        self.assertEqual(second_saved_item.text, 'Item the second')
        self.assertEqual(first_saved_item.list, new_list)
        self.assertEqual(second_saved_item.list, new_list)
    def test_cannot_save_empty_list_items(self):
        new_list = List.objects.create()
        item = Item(list = new_list, text = '')
        # try:
        #     item.save()
        #     self.fail('The save should have raised an exception')
        # except ValidationError:
        #     pass

        with self.assertRaises(ValidationError):
            item.save()
            item.full_clean()
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
