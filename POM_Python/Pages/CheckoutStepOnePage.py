from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from POM_Python.Data.url_testdata import CHECKOUT_STEP_ONE_PAGE_URL_TESTDATA
from POM_Python.Pages.CartPage import CartPage
from POM_Python.Pages.GeneralPage import GeneralPage
from POM_Python.Pages.LoggedInPage import LoggedInPage
from POM_Python.Pages.MainPage import MainPage


class CheckoutStepOnePage(GeneralPage):
    def __init__(self, browser=None):
        super().__init__(browser, CHECKOUT_STEP_ONE_PAGE_URL_TESTDATA)
        self.main_page = MainPage(self.browser)
        self.logged_in_page = LoggedInPage(self.browser)
        self.cart_page = CartPage(self.browser)

    page_header_locator = (By.XPATH, '//span[contains(text(), "Checkout: Your Information")]')

    # Az oldalt akkor tekinti betoltottnek, ha a "Checkout: Your Information" header megjelenik.
    def wait_for_page_to_load(self):
        WebDriverWait(self.browser, 20).until(EC.visibility_of_element_located(self.page_header_locator))

    def get_page_header(self):
        return WebDriverWait(self.browser, 5).until(EC.visibility_of_element_located(self.page_header_locator))

    def get_input_first_name(self):
        return WebDriverWait(self.browser, 5).until(EC.visibility_of_element_located((By.ID, 'first-name')))

    def get_input_last_name(self):
        return WebDriverWait(self.browser, 5).until(EC.visibility_of_element_located((By.ID, 'last-name')))

    def get_input_postal_code(self):
        return WebDriverWait(self.browser, 5).until(EC.visibility_of_element_located((By.ID, 'postal-code')))

    def get_button_continue(self):
        return WebDriverWait(self.browser, 5).until(EC.visibility_of_element_located((By.ID, 'continue')))

    def get_button_cancel(self):
        return WebDriverWait(self.browser, 5).until(EC.visibility_of_element_located((By.ID, 'cancel')))

    def get_error_message(self):
        return WebDriverWait(self.browser, 5).until(EC.visibility_of_element_located(
            (By.XPATH, '//h3[@data-test="error"]')))

    def goto_checkout_step_one_page(self, username, password):
        self.cart_page.goto_cart_page_with_two_items(username, password)
        self.cart_page.get_button_checkout().click()
        self.wait_for_page_to_load()
