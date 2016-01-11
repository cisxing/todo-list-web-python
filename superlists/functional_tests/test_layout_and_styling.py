#from django.test import LiveServerTestCase
from unittest import skip
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from .base import TodoFunctionalTest
class LayoutAndStylingTest(TodoFunctionalTest):
    def test_layout_and_styling(self):
        self.browser.set_window_size(1024, 768)
        self.browser.get(self.live_server_url)

        #she noticed that the input box is nicely centered
        self.check_input_box_is_centered()
        self.enter_a_new_item('testing')
        self.check_input_box_is_centered()
    def check_input_box_is_centered(self):
        inputbox = self.browser.find_element_by_id('id_new_item')
        self.assertAlmostEqual(inputbox.location['x']+(inputbox.size['width']/2),
        512, delta = 5)



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
