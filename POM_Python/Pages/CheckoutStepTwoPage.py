import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from POM_Python.Pages.CheckoutStepOnePage import CheckoutStepOnePage
from POM_Python.Pages.GeneralPage import GeneralPage
from POM_Python.Data.url_testdata import CHECKOUT_STEP_TWO_PAGE_URL_TESTDATA


class CheckoutStepTwoPage(GeneralPage):
    def __init__(self, browser=None):
        super().__init__(browser, CHECKOUT_STEP_TWO_PAGE_URL_TESTDATA)
        self.checkout_step_one_page = CheckoutStepOnePage(self.browser)

    page_header_locator = (By.XPATH, '//span[contains(text(), "Checkout: Overview")]')

    # Az oldalt akkor tekinti betoltottnek, ha a "Checkout: Overview" header megjelenik.
    def wait_for_page_to_load(self):
        WebDriverWait(self.browser, 20).until(EC.visibility_of_element_located(self.page_header_locator))

    def get_page_header(self):
        return WebDriverWait(self.browser, 5).until(EC.visibility_of_element_located(self.page_header_locator))

    def get_items_list(self):
        return WebDriverWait(self.browser, 5).until(EC.visibility_of_all_elements_located(
            (By.CLASS_NAME, 'cart_item')))

    def get_items_quantity_list(self):
        return WebDriverWait(self.browser, 5).until(
            EC.visibility_of_all_elements_located((By.CLASS_NAME, 'cart_quantity')))

    def get_item_name_list(self):
        return WebDriverWait(self.browser, 5).until(
            EC.visibility_of_all_elements_located((By.CLASS_NAME, 'inventory_item_name')))

    def get_item_description_list(self):
        return WebDriverWait(self.browser, 5).until(
            EC.visibility_of_all_elements_located((By.CLASS_NAME, 'inventory_item_desc')))

    def get_item_price_list(self):
        return WebDriverWait(self.browser, 5).until(
            EC.visibility_of_all_elements_located((By.CLASS_NAME, 'inventory_item_price')))

    def get_payment_info(self):
        return WebDriverWait(self.browser, 5).until(
            EC.visibility_of_element_located((By.XPATH, '//div[@data-test="payment-info-value"]')))

    def get_shipping_info(self):
        return WebDriverWait(self.browser, 5).until(
            EC.visibility_of_element_located((By.XPATH, '//div[@data-test="shipping-info-value"]')))

    def get_item_total(self):
        return WebDriverWait(self.browser, 5).until(
            EC.visibility_of_element_located((By.XPATH, '//div[@data-test="subtotal-label"]')))

    def get_tax(self):
        return WebDriverWait(self.browser, 5).until(
            EC.visibility_of_element_located((By.XPATH, '//div[@data-test="tax-label"]')))

    def get_total(self):
        return WebDriverWait(self.browser, 5).until(
            EC.visibility_of_element_located((By.XPATH, '//div[@data-test="total-label"]')))

    def get_button_finish(self):
        return WebDriverWait(self.browser, 5).until(EC.visibility_of_element_located((By.ID, 'finish')))

    def get_button_cancel(self):
        return WebDriverWait(self.browser, 5).until(EC.visibility_of_element_located((By.ID, 'cancel')))

    def goto_checkout_step_two_page(self, username, password, first_name, last_name, postal_code):
        self.checkout_step_one_page.goto_checkout_step_one_page(username, password)
        self.checkout_step_one_page.get_input_first_name().send_keys(first_name)
        self.checkout_step_one_page.get_input_last_name().send_keys(last_name)
        self.checkout_step_one_page.get_input_postal_code().send_keys(postal_code)
        self.checkout_step_one_page.get_button_continue().click()
        self.wait_for_page_to_load()
