from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from POM_Python.Pages.GeneralPage import GeneralPage
from POM_Python.Pages.LoggedInPage import LoggedInPage

URL = 'https://www.saucedemo.com/'


class MainPage(GeneralPage):
    def __init__(self, browser=None):
        super().__init__(browser, URL)  # self.login_page = LoginPage(self.browser)
        self.logged_in_page = LoggedInPage(self.browser)

    page_header_locator = (By.CLASS_NAME, 'login_logo')

    # Az oldalt akkor tekinti betoltottnek, ha a "Swag Labs" felirat megjelenik.
    def wait_for_page_to_load(self):
        WebDriverWait(self.browser, 20).until(EC.visibility_of_element_located(self.page_header_locator))

    def set_window_size(self, width, height):
        self.browser.set_window_size(width, height)

    def get_page_header(self):
        return WebDriverWait(self.browser, 5).until(EC.visibility_of_element_located(self.page_header_locator))

    def get_input_username(self):
        return WebDriverWait(self.browser, 5).until(EC.visibility_of_element_located((By.ID, 'user-name')))

    def get_input_password(self):
        return WebDriverWait(self.browser, 5).until(EC.visibility_of_element_located((By.ID, 'password')))

    def get_button_login(self):
        return WebDriverWait(self.browser, 5).until(EC.visibility_of_element_located((By.ID, 'login-button')))

    ### Osszetettebb muveletek:

    def do_login(self, username, password):
        self.visit()
        self.wait_for_page_to_load()
        self.get_input_username().send_keys(username)
        self.get_input_password().send_keys(password)
        self.get_button_login().click()
        self.logged_in_page.wait_for_page_to_load()
