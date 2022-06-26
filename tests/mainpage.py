import unittest
from selenium import webdriver
from config import PATH
from pages_url import main_page_url


class Main(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(PATH)
        self.driver.get(main_page_url)
        self.driver.maximize_window()

    def test_open_main_page(self):
        assert main_page_url == self.driver.current_url



    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main()