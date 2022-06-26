import time
import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from config import PATH
from pages_url import main_page_url, searchbar_url



class SearchBar(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(PATH)
        self.driver.get(main_page_url)
        self.driver.maximize_window()
        self.search_bar = self.driver.find_element_by_id('search_query_top')


    def test_searchbar_visible(self):
        assert self.search_bar.is_displayed()

    def test_input_clear_value(self):
        self.search_bar.send_keys('dress')
        self.search_bar.clear()
        time.sleep(30)
        assert self.search_bar.text == ''

    def test_search_quotes(self):
        self.search_bar.send_keys('dress')
        self.search_bar.send_keys(Keys.RETURN)
        assert searchbar_url == self.driver.current_url

        title = self.driver.find_element_by_xpath('//*[@id="center_column"]/h1/span[1]').text
        assert title == '"DRESS"'



    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main()