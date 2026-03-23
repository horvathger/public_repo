from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from POM_Python.Data.url_testdata import CHECKOUT_COMPLETE_PAGE_URL_TESTDATA
from POM_Python.Pages.CheckoutStepTwoPage import CheckoutStepTwoPage
from POM_Python.Pages.GeneralPage import GeneralPage


class CheckoutCompletePage(GeneralPage):
    def __init__(self, browser=None):
        super().__init__(browser, CHECKOUT_COMPLETE_PAGE_URL_TESTDATA)

        self.checkout_step_two_page = CheckoutStepTwoPage(self.browser)

    page_header_locator = (By.XPATH, '//span[contains(text(), "Checkout: Complete!")]')

    # Az oldalt akkor tekinti betoltottnek, ha a "Checkout: Complete!" header megjelenik.
    def wait_for_page_to_load(self):
        WebDriverWait(self.browser, 20).until(EC.visibility_of_element_located(self.page_header_locator))

    def get_page_header(self):
        return WebDriverWait(self.browser, 5).until(EC.visibility_of_element_located(self.page_header_locator))

    def get_message_header(self):
        return WebDriverWait(self.browser, 5).until(
            EC.visibility_of_element_located((By.XPATH, '//*[@data-test="complete-header"]')))

    def get_message_text(self):
        return WebDriverWait(self.browser, 5).until(
            EC.visibility_of_element_located((By.XPATH, '//*[@data-test="complete-text"]')))

    def get_back_home_button(self):
        return WebDriverWait(self.browser, 5).until(EC.visibility_of_element_located(
            (By.ID, 'back-to-products')))

    def goto_checkout_complete_page(self, username, password, first_name, last_name, postal_code):
        self.checkout_step_two_page.goto_checkout_step_two_page(username, password, first_name, last_name, postal_code)
        self.checkout_step_two_page.get_button_finish().click()
        self.wait_for_page_to_load()
