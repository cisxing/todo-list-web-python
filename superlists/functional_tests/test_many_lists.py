from .base import TodoFunctionalTest

class ManyListsTest(TodoFunctionalTest):
    def change_list_name(self, list_name):
        pass
    def test_can_create_and_view_many_lists(self):
        #List1. Groceries
        #List2. Homework
        #Edith comes to the home page, creates a new list
        #and fills in her grocery list
        self.browser.get(self.live_server_url)
        self.enter_a_new_item("Buy milk")
        self.enter_a_new_item("Buy cheese")
        self.check_for_row_in_list_table('Buy milk')
        self.check_for_row_in_list_table('Buy cheese')

        #She sees that she can change the list name
        self.change_list_name('Groceries')
        #Edith goes back to the homepage and sees her grocery list
        self.browser.get(self.live_server_url)
        self.check_for_row_in_list_table('Groceries')
        #Edith creates a new list for her art history Homework
        self.browser.enter_a_new_item('Read Camille')
        #Edith opens the homepage later and sees both lists
        self.browser.get(self.live_server_url)
        self.check_for_row_in_list_table('Groceries')
        self.check_for_row_in_list_table('Read Camille')
        #Edith goes to the grocery list and sees what she needs to buy
        rows = self.browser.find_table_row('Groceries')
        row = self.find_element_by_tag_name('a').click()
        self.check_for_row_in_list_table("Buy milk")
        self.check_for_row_in_list_table("Buy cheese")
