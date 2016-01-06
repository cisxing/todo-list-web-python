from selenium import webdriver
from django.test import LiveServerTestCase
from selenium.webdriver.common.keys import Keys
import unittest
#difference between unit test and functional test?
#1. unit test is focused and precised and short while acceptance test is long
class NewVisitorTest(LiveServerTestCase):
    #before and after every single test for the two def
    def setUp(self):
        self.browser = webdriver.Firefox()
        #selenium may not know when the next step is ready.
        #so we automatically fail if nothing is happening in 3 sec
        self.browser.implicitly_wait(3)
    def tearDown(self):
        self.browser.quit()

    def check_for_row_in_list_table(self, row_text):
        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')
        self.assertIn(row_text, [row.text for row in rows])

    def send_key_and_enter(self, row_text):
        inputbox = self.browser.find_element_by_id('id_new_item')
        inputbox.send_keys(row_text)
        inputbox.send_keys(Keys.ENTER)

    def test_can_start_a_list_and_retrieve_it_later(self):

    #def test_can_log_in_a_new_account(self):



        # write test first before writing the program
        # Edith has heard abot a call new online to-do app
        # She goes to check out its homepage
        #start a portal 8000
        #go to the homepage

        #this does not need us to run the server anymore
        self.browser.get(self.live_server_url)
        # She notices the page title and header mention to-do lists.
        self.assertIn('To-Do', self.browser.title)
        #browser info given by selenium
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('To-Do',header_text)
        #the last line is similar to the following:
        #if ! 'django' in browser.title:
        #   throw new AssertionError


        #functional test, acceptance test, End to End (meaning from the point view of user)


        #She is invited to enter a to-do item straight away
        inputbox = self.browser.find_element_by_id('id_new_item')
        self.assertEqual(inputbox.get_attribute('placeholder'), 'enter a to-do item')
        # She types "Buy peacock feathers" into a textbox
        #her hobby is trying fly-fishing lures
        #When she hits enter, the page updates, and now the page lists
        #1. Buy peacock feathers as the item in a to-do lists
        self.send_key_and_enter("Buy peacock feathers")
        #when she hits enter, she is tsaken to a new url
        #and now the page lists "1.Buy peaock feathers"

        #useful debugging test for functional test
        #import time
        #time.sleep(15)
        edith_list_url = self.browser.current_url
        self.assertRegexpMatches(edith_list_url,'/lists/.+')
        self.check_for_row_in_list_table("1. Buy peacock feathers")
        #self.assertTrue(
        #    any(row.text=='1. Buy peacock feathers' for row in rows),
        #    "New to-do item did not appear in the table -- text was:\n%s" % (
        #    table.text,
        #    )
        #)
        #There is still a textbox inviting her to add another item
        # She enters 'Use peacock feathers to make fly'
        # She is very methdolical
        # The homepage updates again, and now shows both items on her lists

        self.send_key_and_enter("Use peacock feathers to make fly")

        #Edith wonders whether the site will remember her list. Then she sees
        #that the site has generated a unique URL for her -- there is some
        #explanatory text to that effect.
        self.check_for_row_in_list_table("1. Buy peacock feathers")
        self.check_for_row_in_list_table("2. Use peacock feathers to make fly")

        #She visits that URL - her to-do list is still there


        #now a new user, Francis comes along
        ## We use a new broswer session to make sure no information of Edith's
        ##comes a long( EG cookies, localstorage)
        self.browser.quit()
        self.browser = webdriver.Firefox()
        self.browser.get(self.live_server_url)
        page_text = self.browser.find_element_by_tag_name('body').text
        self.assertNotIn('Buy peacock feathers', page_text)
        self.assertNotIn('make a fly', page_text)
        print "everything is working up till this point"
        self.send_key_and_enter('Buy Milk')
        fracis_list_url = self.browser.current_url
        self.assertRegexpMatches(fracis_list_url, 'lists/.+')
        self.assertNotEqual(fracis_list_url, edith_list_url)
        page_text = self.browser.find_element_by_id('body').text
        self.assertNotIn('Buy peacock feathers', page_text)
        self.assertIn('Buy Milk', page_text)
        #Both satisfied, they both go back to sleep
        self.fail('Finish the app!')
