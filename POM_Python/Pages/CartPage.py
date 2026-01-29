import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait

from POM_Python.Pages.GeneralPage import GeneralPage

URL = 'https://www.saucedemo.com/cart.html'


class LoggedInPage(GeneralPage):
    def __init__(self, browser=None):
        super().__init__(browser, URL)

    page_header_locator = (By.ID, 'checkout')

    # Az oldalt akkor tekinti betoltottnek, ha a "Checkout" gomb megjelenik.
    def wait_for_page_to_load(self):
        WebDriverWait(self.browser, 20).until(EC.visibility_of_element_located(self.page_header_locator))

    def get_button_continue_shopping(self):
        return WebDriverWait(self.browser, 5).until(EC.visibility_of_element_located((By.ID, 'continue-shopping')))

    def get_button_checkout(self):
        return WebDriverWait(self.browser, 5).until(EC.visibility_of_element_located(self.page_header_locator))