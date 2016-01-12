#from django.test import LiveServerTestCase
from unittest import skip
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from .base import TodoFunctionalTest

class ItemValidationTest(TodoFunctionalTest):
    # def test_cannot_add_empty_list_item(self):
    #     self.browser.get(self.live_server_url)
    #     self.enter_a_new_item('')
    #
    #     error = self.browser.find_element_by_css_selector('.has_error')
    #     self.assertEqual(error.text, "You can't have an empty list item")
    #     #Edith goes to the home page, and accidentally tries to
    #     #submit an empty list item.
    #     #she hits enter on the empty input box
    #
    #     #The homge page refreshes, and there is an error messages
    #     #saying that list items can not be blank.
    #
    #     #she tries again with same text for the item
    #     #which now works
    #     self.enter_a_new_item("Buy Milk")
    #     self.check_for_row_in_list_table('1. Buy Milk')
    #     #perversely tries to add a second blank item
    #     #she receives a similar warning on the list page.
    #     #And she can correct it by filling some text in.
    #     self.enter_a_new_item('')
    #     self.assertEqual(error.text, "You can't have an empty list item")
    #     self.enter_a_new_item('Make Tea')
    #     self.check_for_row_in_list_table("1. Buy Milk")
    #     self.check_for_row_in_list_table("2. Make Tea")
    def test_cannot_add_empty_list_item(self):

        self.browser.get(self.live_server_url)
        self.enter_a_new_item('')

        error = self.browser.find_element_by_css_selector('.has-error')
        self.assertEqual(error.text, "You can't have an empty list item")

        self.enter_a_new_item('Buy milk')
        self.check_for_row_in_list_table('1. Buy milk')

        self.enter_a_new_item('')
        self.check_for_row_in_list_table('1. Buy milk')
        error = self.browser.find_element_by_css_selector('.has-error')
        self.assertEqual(error.text, "You can't have an empty list item")

        self.enter_a_new_item('Make tea')
        self.check_for_row_in_list_table('1. Buy milk')
        self.check_for_row_in_list_table('2. Make tea')

        self.fail("Finish the test!")
