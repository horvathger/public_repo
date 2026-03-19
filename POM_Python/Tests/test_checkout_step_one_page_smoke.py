import allure

from POM_Python.Data.checkout_step_one_testdata import (CHECKOUT_STEP_ONE_URL, CHECKOUT_STEP_ONE_PAGE_HEADER)
from POM_Python.Data.user_testdata import STANDARD_USER_LOGIN_DATA
from POM_Python.Pages.CheckoutStepOnePage import CheckoutStepOnePage
from POM_Python.Utils.create_driver import create_preconfigured_chrome_driver


@allure.parent_suite("UI Tests")
@allure.suite("Checkout Step One page smoke tests")
@allure.sub_suite("Test cases")
class TestCheckoutStepOnePageSmoke:
    def setup_method(self):
        browser = create_preconfigured_chrome_driver()
        self.checkout_step_one_page = CheckoutStepOnePage(browser)

    def teardown_method(self):
        self.checkout_step_one_page.quit()

    @allure.title('A Checkout Step One Page oldal fejszövegének ellenőrzése')
    @allure.description('A teszteset célja annak ellenőrzése, hogy a Checkout Step One Page fejszövege megjelenik-e.')
    @allure.severity(allure.severity_level.TRIVIAL)
    @allure.tag('checkout_step_one', 'smoke', 'standard_user')
    def test_checkout_step_one_page_header_visibility(self):
        self.checkout_step_one_page.goto_checkout_step_one_page(STANDARD_USER_LOGIN_DATA["username"],
                                                                STANDARD_USER_LOGIN_DATA["password"])
        assert self.checkout_step_one_page.get_page_header().is_displayed()
        assert self.checkout_step_one_page.get_page_header().text == CHECKOUT_STEP_ONE_PAGE_HEADER
        assert self.checkout_step_one_page.get_current_url() == CHECKOUT_STEP_ONE_URL

    @allure.title('A Checkout Step One oldal firstname mezőjének ellenőrzése')
    @allure.description('A teszteset célja annak ellenőrzése, hogy a Checkout Step One Page-en megjelenik-e a '
                        'firstname input mező és interaktív-e.')
    @allure.severity(allure.severity_level.TRIVIAL)
    @allure.tag('checkout_step_one', 'smoke', 'standard_user')
    def test_checkout_step_one_page_input_firstname_visibility(self):
        self.checkout_step_one_page.goto_checkout_step_one_page(STANDARD_USER_LOGIN_DATA["username"],
                                                                STANDARD_USER_LOGIN_DATA["password"])
        assert self.checkout_step_one_page.get_input_first_name().is_displayed()
        assert self.checkout_step_one_page.get_input_first_name().is_enabled()

    @allure.title('A Checkout Step One oldal lastname mezőjének ellenőrzése')
    @allure.description('A teszteset célja annak ellenőrzése, hogy a Checkout Step One Page-en megjelenik-e a '
                        'lastname mező és interaktív-e.')
    @allure.severity(allure.severity_level.TRIVIAL)
    @allure.tag('checkout_step_one', 'smoke', 'standard_user')
    def test_checkout_step_one_page_input_lastname_visibility(self):
        self.checkout_step_one_page.goto_checkout_step_one_page(STANDARD_USER_LOGIN_DATA["username"],
                                                                STANDARD_USER_LOGIN_DATA["password"])
        assert self.checkout_step_one_page.get_input_last_name().is_displayed()
        assert self.checkout_step_one_page.get_input_last_name().is_enabled()

    @allure.title('A Checkout Step One oldal zip/postal code mezőjének ellenőrzése')
    @allure.description('A teszteset célja annak ellenőrzése, hogy a Checkout Step One Page-en megjelenik-e a '
                        'zip/postal code mező és interaktív-e.')
    @allure.severity(allure.severity_level.TRIVIAL)
    @allure.tag('checkout_step_one', 'smoke', 'standard_user')
    def test_checkout_step_one_page_input_zip_postal_code_visibility(self):
        self.checkout_step_one_page.goto_checkout_step_one_page(STANDARD_USER_LOGIN_DATA["username"],
                                                                STANDARD_USER_LOGIN_DATA["password"])
        assert self.checkout_step_one_page.get_input_postal_code().is_displayed()
        assert self.checkout_step_one_page.get_input_postal_code().is_enabled()

    @allure.title('A Checkout Step One oldalon a Cancel gomb ellenőrzése')
    @allure.description('A teszteset célja annak ellenőrzése, hogy a Checkout Step One Page-en megjelenik-e a '
                        'Cancel gomb és interaktív-e.')
    @allure.severity(allure.severity_level.TRIVIAL)
    @allure.tag('checkout_step_one', 'smoke', 'standard_user')
    def test_checkout_step_one_page_button_cancel_visibility(self):
        self.checkout_step_one_page.goto_checkout_step_one_page(STANDARD_USER_LOGIN_DATA["username"],
                                                                STANDARD_USER_LOGIN_DATA["password"])
        assert self.checkout_step_one_page.get_button_cancel().is_displayed()
        assert self.checkout_step_one_page.get_button_cancel().is_enabled()

    @allure.title('A Checkout Step One oldalon a Continue gomb ellenőrzése')
    @allure.description('A teszteset célja annak ellenőrzése, hogy a Checkout Step One Page-en megjelenik-e a '
                        'Continue gomb és interaktív-e.')
    @allure.severity(allure.severity_level.TRIVIAL)
    @allure.tag('checkout_step_one', 'smoke', 'standard_user')
    def test_checkout_step_one_page_button_continue_visibility(self):
        self.checkout_step_one_page.goto_checkout_step_one_page(STANDARD_USER_LOGIN_DATA["username"],
                                                                STANDARD_USER_LOGIN_DATA["password"])
        assert self.checkout_step_one_page.get_button_continue().is_displayed()
        assert self.checkout_step_one_page.get_button_continue().is_enabled()
