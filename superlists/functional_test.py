from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import unittest
#difference between unit test and functional test?
#1. unit test is focused and precised and short while acceptance test is long
class NewVisitorTest(unittest.TestCase):
    #before and after every single test for the two def
    def setUp(self):
        self.browser = webdriver.Firefox()
        #selenium may not know when the next step is ready.
        #so we automatically fail if nothing is happening in 3 sec
        self.browser.implicitly_wait(3)
    def tearDown(self):
        self.browser.quit()

    def test_can_start_a_list_and_retrieve_it_later(self):

    #def test_can_log_in_a_new_account(self):



        # write test first before writing the program
        # Edith has heard abot a call new online to-do app
        # She goes to check out its homepage
        #start a portal 8000
        #go to the homepage
        self.browser.get('http://localhost:8000')
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
        inputbox.send_keys('Buy peacock feathers')
        #When she hits enter, the page updates, and now the page lists
        #1. Buy peacock feathers as the item in a to-do lists
        inputbox.send_keys(Keys.ENTER)

        #useful debugging test for functional test
        #import time
        #time.sleep(15)

        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')
        self.assertIn('1. Buy peacock feathers', [row.text for row in rows])
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

        #Edith wonders whether the site will remember her list. Then she sees
        #that the site has generated a unique URL for her -- there is some
        #explanatory text to that effect.

        #She visits that URL - her to-do list is still there

        #satisfied, she goes back to sleep
        self.fail('Finish the app!')
if __name__ == '__main__':
    unittest.main()
