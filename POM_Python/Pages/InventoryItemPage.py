from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from POM_Python.Pages.GeneralPage import GeneralPage

URL = 'https://www.saucedemo.com/inventory-item.html'


class InventoryItemPage(GeneralPage):
    def __init__(self, browser=None):
        super().__init__(browser, URL)

    def get_back_to_products_button(self):
        return WebDriverWait(self.browser, 5).until(EC.visibility_of_element_located((By.ID, 'back-to-products')))

    def get_item_image(self):
        return WebDriverWait(self.browser, 5).until(
            EC.visibility_of_element_located((By.CLASS_NAME, 'inventory_details_img')))

    def get_item_name(self):
        return WebDriverWait(self.browser, 5).until(
            EC.visibility_of_element_located((By.XPATH, '//div[@data-test="inventory-item-name"]')))

    def get_item_description(self):
        return WebDriverWait(self.browser, 5).until(
            EC.visibility_of_element_located((By.XPATH, '//div[@data-test="inventory-item-desc"]')))

    def get_item_price(self):
        return WebDriverWait(self.browser, 5).until(
            EC.visibility_of_element_located((By.XPATH, '//div[@data-test="inventory-item-price"]')))

    def get_add_to_cart_button(self):
        return WebDriverWait(self.browser, 5).until(
            EC.visibility_of_element_located((By.XPATH, '//div[@data-test="add-to-cart"]')))

    def get_remove_from_cart_button(self):
        return WebDriverWait(self.browser, 5).until(
            EC.visibility_of_element_located((By.XPATH, '//div[@data-test="remove"]')))