import time

import allure
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait

URL = 'https://www.saucedemo.com'

USER = ['standard_user', 'locked_out_user', 'problem_user', 'error_user']
PASS = 'secret_sauce'

expected_error_message = 'Epic sadface: Sorry, this user has been locked out.'



class TestSauceDemo(object):
    def setup_method(self):
        options = Options()
        options.add_experimental_option("detach", True)
        options.add_argument('--guest')
        self.browser = webdriver.Chrome(options=options)
        self.browser.maximize_window()
        # betoltom az oldalt
        self.browser.get(URL)

    def teardown_method(self):
        pass  # self.browser.quit()

    # TESZTESETEK:  ***************************************


    def login(self, username = USER[0], password = PASS):
        # - bejelentkezek
        WebDriverWait(self.browser, 5).until(EC.element_to_be_clickable((By.ID, 'user-name'))).send_keys(username)
        time.sleep(1)
        WebDriverWait(self.browser, 5).until(EC.element_to_be_clickable((By.ID, 'password'))).send_keys(password)
        WebDriverWait(self.browser, 5).until(EC.element_to_be_clickable((By.ID, 'login-button'))).click()

        shopping_cart_icon = WebDriverWait(self.browser, 5).until(
            EC.visibility_of_element_located((By.XPATH, '//a[@data-test="shopping-cart-link"]')))
        assert shopping_cart_icon.is_displayed()

    def test_login_standard_user(self):
        TestSauceDemo.login(self)

    def test_login_locked_out_user(self, username = USER[1], password = PASS):
        TestSauceDemo.login(self, username, password)

    def test_login_problem_user(self, username = USER[2], password = PASS):
        TestSauceDemo.login(self, username, password)

    def test_login_error_user(self, username=USER[3], password=PASS):
        TestSauceDemo.login(self, username, password)
