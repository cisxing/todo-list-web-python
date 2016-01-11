#from django.test import LiveServerTestCase
from unittest import skip
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class TodoFunctionalTest(StaticLiveServerTestCase):

    def setUp(self):

        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(3)

    def tearDown(self):

        self.browser.quit()

    def check_for_row_in_list_table(self, row_text):

        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')

        self.assertIn(row_text, [row.text for row in rows])

    def enter_a_new_item(self, todo_text):

        inputbox = self.browser.find_element_by_id('id_new_item')
        inputbox.send_keys(todo_text)
        inputbox.send_keys(Keys.ENTER)

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
