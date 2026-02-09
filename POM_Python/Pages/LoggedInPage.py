import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
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

    def get_page_header(self):
        return WebDriverWait(self.browser, 5).until(EC.visibility_of_element_located(self.page_header_locator))

    def get_hamburger_menu_button(self):
        return WebDriverWait(self.browser, 5).until(EC.visibility_of_element_located(
            (By.ID, 'react-burger-menu-btn')))

    def get_hamburger_menu_close_button(self):
        return WebDriverWait(self.browser, 5).until(EC.visibility_of_element_located(
            (By.ID, 'react-burger-cross-btn')))

    def wait_for_hamburger_menu_to_open(self):
        end_time = time.time() + 10
        last_position = None

        element = self.get_hamburger_menu_close_button()

        while time.time() < end_time:
            current_position = element.location

            if last_position == current_position:
                # pozíció nem változik → elem megállt
                return True

            last_position = current_position
            time.sleep(0.1)

        raise TimeoutError("Element did not stop moving within timeout.")

    def get_hamburger_menu_all_items(self):
        return WebDriverWait(self.browser, 5).until(EC.visibility_of_element_located(
            (By.ID, 'inventory_sidebar_link')))

    def get_hamburger_menu_about(self):
        return WebDriverWait(self.browser, 5).until(EC.visibility_of_element_located(
            (By.ID, 'about_sidebar_link')))

    def get_hamburger_menu_logout(self):
        return WebDriverWait(self.browser, 5).until(EC.visibility_of_element_located(
            (By.ID, 'logout_sidebar_link')))

    def get_hamburger_menu_reset_app_state(self):
        return WebDriverWait(self.browser, 5).until(EC.visibility_of_element_located(
            (By.ID, 'reset_sidebar_link')))

    def get_shopping_cart_button(self):
        return WebDriverWait(self.browser, 5).until(
            EC.visibility_of_element_located((By.ID, 'shopping_cart_container')))

    def get_number_of_items_in_cart(self):
        try:
            cart_badge = WebDriverWait(self.browser, 5).until(
                EC.visibility_of_element_located((By.CLASS_NAME, 'shopping_cart_badge')))
            return int(cart_badge.text)
        except:
            return 0

    def get_sorting_list(self):
        return WebDriverWait(self.browser, 5).until(
            EC.visibility_of_element_located((By.CLASS_NAME, 'product_sort_container')))

    def select_az_sorting_options(self):
        sorting_selection = Select(self.get_sorting_list())
        return sorting_selection.select_by_value('az')

    def select_za_sorting_options(self):
        sorting_selection = Select(self.get_sorting_list())
        return sorting_selection.select_by_value('za')

    def select_price_low_to_high_sorting_options(self):
        sorting_selection = Select(self.get_sorting_list())
        return sorting_selection.select_by_value('lohi')

    def select_price_hig_to_low_sorting_options(self):
        sorting_selection = Select(self.get_sorting_list())
        return sorting_selection.select_by_value('hilo')

    def get_product_img_list(self):
        return WebDriverWait(self.browser, 5).until(
            EC.visibility_of_all_elements_located((By.XPATH, '//img[@class="inventory_item_img"]')))

    def get_product_name_list(self):
        return WebDriverWait(self.browser, 5).until(
            EC.visibility_of_all_elements_located((By.CLASS_NAME, 'inventory_item_name')))

    def get_product_price_list(self):
        return WebDriverWait(self.browser, 5).until(
            EC.visibility_of_all_elements_located((By.CLASS_NAME, 'inventory_item_price')))

    def get_add_to_cart_button_list(self):
        return WebDriverWait(self.browser, 5).until(
            EC.visibility_of_all_elements_located((By.XPATH, '//button[contains(@class, "btn_inventory")]')))

    def get_product_description_list(self):
        return WebDriverWait(self.browser, 5).until(
            EC.visibility_of_all_elements_located((By.CLASS_NAME, 'inventory_item_desc')))

    def get_footer_twitter_icon(self):
        return WebDriverWait(self.browser, 5).until(
            EC.visibility_of_element_located((By.XPATH, '//a[@data-test="social-twitter"]')))

    def get_footer_facebook_icon(self):
        return WebDriverWait(self.browser, 5).until(
            EC.visibility_of_element_located((By.XPATH, '//a[@data-test="social-facebook"]')))

    def get_footer_linkedin_icon(self):
        return WebDriverWait(self.browser, 5).until(
            EC.visibility_of_element_located((By.XPATH, '//a[@data-test="social-linkedin"]')))
