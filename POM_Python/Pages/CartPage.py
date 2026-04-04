from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from POM_Python.Data.url_testdata import CART_PAGE_URL_TESTDATA
from POM_Python.Pages.GeneralPage import GeneralPage
from POM_Python.Pages.LoggedInPage import LoggedInPage
from POM_Python.Pages.MainPage import MainPage


class CartPage(GeneralPage):
    def __init__(self, browser=None):
        super().__init__(browser, CART_PAGE_URL_TESTDATA)
        self.main_page = MainPage(browser)
        self.logged_in_page = LoggedInPage(browser)

    page_header_locator = (By.XPATH, '//span[contains(text(), "Your Cart")]')

    # Az oldalt akkor tekinti betoltottnek, ha a "Your Cart" header megjelenik.
    def wait_for_page_to_load(self):
        WebDriverWait(self.browser, 20).until(EC.visibility_of_element_located(self.page_header_locator))

    def get_page_header(self):
        return WebDriverWait(self.browser, 5).until(EC.visibility_of_element_located(self.page_header_locator))

    def get_cart_items(self):
        return WebDriverWait(self.browser, 5).until(EC.visibility_of_all_elements_located(
            (By.CLASS_NAME, 'cart_item')))

    def get_cart_item_names(self):
        return WebDriverWait(self.browser, 5).until(
            EC.visibility_of_all_elements_located((By.CLASS_NAME, 'inventory_item_name')))

    def get_cart_item_prices(self):
        return WebDriverWait(self.browser, 5).until(
            EC.visibility_of_all_elements_located((By.CLASS_NAME, 'inventory_item_price')))

    def get_cart_item_descriptions(self):
        return WebDriverWait(self.browser, 5).until(
            EC.visibility_of_all_elements_located((By.CLASS_NAME, 'inventory_item_desc')))

    def get_cart_item_quantities(self):
        return WebDriverWait(self.browser, 5).until(
            EC.visibility_of_all_elements_located((By.CLASS_NAME, 'cart_quantity')))

    def get_cart_item_remove_buttons(self):
        return WebDriverWait(self.browser, 5).until(
            EC.visibility_of_all_elements_located((By.CLASS_NAME, 'cart_button')))

    def get_button_continue_shopping(self):
        return WebDriverWait(self.browser, 5).until(EC.visibility_of_element_located(
            (By.ID, 'continue-shopping')))

    def get_button_checkout(self):
        return WebDriverWait(self.browser, 5).until(EC.visibility_of_element_located((By.ID, 'checkout')))

    def goto_cart_page_with_two_items(self, username, password):
        self.main_page.do_login(username, password)
        self.logged_in_page.get_add_to_cart_button_list()[0].click()
        self.logged_in_page.get_add_to_cart_button_list()[1].click()
        self.logged_in_page.get_shopping_cart_button().click()
        self.wait_for_page_to_load()
