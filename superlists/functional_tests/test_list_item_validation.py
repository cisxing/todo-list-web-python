#from django.test import LiveServerTestCase
from unittest import skip
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from .base import TodoFunctionalTest

class ItemValidationTest(TodoFunctionalTest):
    @skip("Haven't implemented this")
    def test_cannot_add_empty_list_item(self):
        self.fail("finish the test")
        #Edith goes to the home page, and accidentally tries to
        #submit an empty list item.
        #she hits enter on the empty input box

        #The homge page refreshes, and there is an error messages
        #saying that list items can not be blank.

        #she tries again with same text for the item
        #which now works

        #perversely tries to add a second blank item
        #she receives a similar warning on the list page.
        #And she can correct it by filling some text in.
