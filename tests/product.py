import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from config import PATH
from pages_url import main_page_url, product_women_tab_url, product_casual_dress_tab_url, product_dress_page_url, \
    product_cart_url


class Product(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(PATH)
        self.driver.get(main_page_url)
        self.driver.maximize_window()


    def test_go_to_dress_page_select_dress_and_size_(self):
        women_tab = self.driver.find_element_by_xpath('//*[@id="block_top_menu"]/ul/li[1]/a')
        women_tab.click()
        assert product_women_tab_url == self.driver.current_url

        dress_tab = self.driver.find_element_by_xpath('//*[@id="categories_block_left"]/div/ul/li[2]/span')
        dress_tab.click()
        casual_dresses = self.driver.find_element_by_xpath('//*[@id="categories_block_left"]/div/ul/li[2]/ul/li[1]/a')
        casual_dresses.click()
        assert product_casual_dress_tab_url == self.driver.current_url

        dress = self.driver.find_element_by_link_text('Printed Dress')
        dress.click()
        assert product_dress_page_url == self.driver.current_url

        select_size = Select(self.driver.find_element_by_id('group_1'))
        select_size.select_by_visible_text('M')
        selected_size = self.driver.find_element_by_xpath('//*[@id="uniform-group_1"]/span')
        assert selected_size.text == 'M'

    def test_add_to_cart(self):
        dress_page = self.driver.get(product_dress_page_url)
        add_to_cart = self.driver.find_element_by_css_selector('button[name=Submit]')
        add_to_cart.click()
        alert = self.driver.find_element_by_class_name('clearfix')
        element = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, '//span[normalize-space(text())="Proceed to checkout"]')))
        element.click()

        assert product_cart_url == self.driver.current_url




















    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()