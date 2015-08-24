from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import unittest


class NewVisitorTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(3)

    def tearDown(self):
        self.browser.quit()

    def test_can_start_a_list_and_recieve_it_later(self):
        self.browser.get('http://localhost:8000')

        """The user has heard of a cool new To Do App and decides to go check
        it out
        """

        self.assertIn('To-Do', self.browser.title)
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('To-Do', header_text)
        """
        She is invited to enter a To Do item straight away and enters buy
        peacock feathers
        """
        inputbox = self.browser.find_element_by_id('id_new_item')
        self.assertEqual(
                inputbox.get_attribute('placeholder'),
                'Enter a To-Do item'
        )
        inputbox.send_keys('Buy peacock feathers')
        # When she hits enter the page lists the item
        inputbox.send_keys(Keys.ENTER)

        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')
        self.assertTrue(
            any(row.text == '1: Buy peacock feathers' for row in rows),
            "The item did not appear in a new row"
        )
        # She enters another item buy peacock feathers to make her fly

        # She hits enter again and the page now shows both items

        """
        She wonders if the site will remember her and see she's the site has
        generated a unique url for her, she visits the new url and the list is
        still there
        Satisfied she goes to sleep """
        self.fail('Finish the test!')
if __name__ == '__main__':
    unittest.main(warnings='ignore')
