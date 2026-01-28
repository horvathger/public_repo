from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from POM_Python.Pages.GeneralPage import GeneralPage

URL = 'https://www.saucedemo.com/inventory.html'

class LoggedInPage(GeneralPage):
    def __init__(self, browser=None):
        super().__init__(browser, URL)

    page_header_locator = (By.CLASS_NAME, 'app_logo')

    # Az oldalt akkor tekinti betoltottnek, ha a "Swag Labs" felirat megjelenik.
    def wait_for_page_to_load(self):
        WebDriverWait(self.browser, 20).until(EC.visibility_of_element_located(self.page_header_locator))

    def set_window_size(self, width, height):
        self.browser.set_window_size(width, height)

    def get_page_header(self):
        return WebDriverWait(self.browser, 5).until(EC.visibility_of_element_located(self.page_header_locator))

    def get_hamburger_menu_button(self):
        return WebDriverWait(self.browser, 5).until(EC.visibility_of_element_located(
            (By.ID, 'react-burger-menu-btn')))

    def get_shopping_cart_button(self):
        return WebDriverWait(self.browser, 5).until(EC.visibility_of_element_located(
            (By.ID, 'shopping_cart_container')))