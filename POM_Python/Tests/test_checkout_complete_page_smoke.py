import allure

from POM_Python.Data.checkout_complete_testdata import (CHECKOUT_COMPLETE_PAGE_HEADER_TESTDATA,
                                                        CHECKOUT_COMPLETE_PAGE_COMPLETE_MESSAGE_BODY_TESTDATA,
                                                        CHECKOUT_COMPLETE_PAGE_COMPLETE_MESSAGE_HEADER_TESTDATA)
from POM_Python.Data.checkout_step_one_testdata import CHECKOUT_STEP_ONE_INPUT_VALID_TESTDATA
from POM_Python.Data.url_testdata import CHECKOUT_COMPLETE_PAGE_URL_TESTDATA, LOGGED_IN_URL_TESTDATA
from POM_Python.Data.user_testdata import STANDARD_USER_LOGIN_DATA
from POM_Python.Pages.CheckoutCompletePage import CheckoutCompletePage
from POM_Python.Pages.LoggedInPage import LoggedInPage
from POM_Python.Utils.create_driver import create_preconfigured_chrome_driver


@allure.parent_suite("UI Tests")
@allure.suite("Checkout Step Two page smoke tests")
@allure.sub_suite("Test cases")
class TestCheckoutStepTwoPageSmoke:
    def setup_method(self):
        browser = create_preconfigured_chrome_driver()
        self.checkout_complete_page = CheckoutCompletePage(browser)
        self.logged_in_page = LoggedInPage(browser)

    def teardown_method(self):
        self.checkout_complete_page.quit()

    @allure.title('A Checkout Complete oldal fejszövegének ellenőrzése')
    @allure.description('A teszteset célja annak ellenőrzése, hogy a Checkout Complete Page fejszövege megjelenik-e.')
    @allure.severity(allure.severity_level.TRIVIAL)
    @allure.tag('checkout_complete', 'smoke', 'standard_user')
    def test_checkout_complete_page_header_visibility(self):
        self.checkout_complete_page.goto_checkout_complete_page(STANDARD_USER_LOGIN_DATA["username"],
                                                                STANDARD_USER_LOGIN_DATA["password"],
                                                                CHECKOUT_STEP_ONE_INPUT_VALID_TESTDATA["first_name"],
                                                                CHECKOUT_STEP_ONE_INPUT_VALID_TESTDATA["last_name"],
                                                                CHECKOUT_STEP_ONE_INPUT_VALID_TESTDATA["postal_code"])
        assert self.checkout_complete_page.get_page_header().is_displayed()
        assert self.checkout_complete_page.get_page_header().text == CHECKOUT_COMPLETE_PAGE_HEADER_TESTDATA

    @allure.title('A Checkout Complete oldalon az üzenet fejszövegének ellenőrzése')
    @allure.description('A teszteset célja annak ellenőrzése, hogy a Checkout Complete Page oldalon az üzenet '
                        'fejszövege megjelenik-e.')
    @allure.severity(allure.severity_level.TRIVIAL)
    @allure.tag('checkout_complete', 'smoke', 'standard_user')
    def test_checkout_complete_message_header_visibility(self):
        self.checkout_complete_page.goto_checkout_complete_page(STANDARD_USER_LOGIN_DATA["username"],
                                                                STANDARD_USER_LOGIN_DATA["password"],
                                                                CHECKOUT_STEP_ONE_INPUT_VALID_TESTDATA["first_name"],
                                                                CHECKOUT_STEP_ONE_INPUT_VALID_TESTDATA["last_name"],
                                                                CHECKOUT_STEP_ONE_INPUT_VALID_TESTDATA["postal_code"])
        assert self.checkout_complete_page.get_message_header().is_displayed()
        assert (self.checkout_complete_page.get_message_header().text ==
                CHECKOUT_COMPLETE_PAGE_COMPLETE_MESSAGE_HEADER_TESTDATA)

    @allure.title('A Checkout Complete oldalon az üzenet tartalmának ellenőrzése')
    @allure.description('A teszteset célja annak ellenőrzése, hogy a Checkout Complete Page oldalon az üzenet '
                        'tartalma megjelenik-e.')
    @allure.severity(allure.severity_level.TRIVIAL)
    @allure.tag('checkout_complete', 'smoke', 'standard_user')
    def test_checkout_complete_message_body_visibility(self):
        self.checkout_complete_page.goto_checkout_complete_page(STANDARD_USER_LOGIN_DATA["username"],
                                                                STANDARD_USER_LOGIN_DATA["password"],
                                                                CHECKOUT_STEP_ONE_INPUT_VALID_TESTDATA["first_name"],
                                                                CHECKOUT_STEP_ONE_INPUT_VALID_TESTDATA["last_name"],
                                                                CHECKOUT_STEP_ONE_INPUT_VALID_TESTDATA["postal_code"])
        assert self.checkout_complete_page.get_message_text().is_displayed()
        assert (self.checkout_complete_page.get_message_text().text ==
                CHECKOUT_COMPLETE_PAGE_COMPLETE_MESSAGE_BODY_TESTDATA)

    @allure.title('A Checkout Complete oldalon a "Back Home" gomb ellenőrzése')
    @allure.description('A teszteset célja annak ellenőrzése, hogy a Checkout Complete Page oldalon a "Back Home" '
                        'gomb megjelenik-e és interaktív-e.')
    @allure.severity(allure.severity_level.TRIVIAL)
    @allure.tag('checkout_complete', 'smoke', 'standard_user')
    def test_checkout_complete_button_back_home_visibility(self):
        self.checkout_complete_page.goto_checkout_complete_page(STANDARD_USER_LOGIN_DATA["username"],
                                                                STANDARD_USER_LOGIN_DATA["password"],
                                                                CHECKOUT_STEP_ONE_INPUT_VALID_TESTDATA["first_name"],
                                                                CHECKOUT_STEP_ONE_INPUT_VALID_TESTDATA["last_name"],
                                                                CHECKOUT_STEP_ONE_INPUT_VALID_TESTDATA["postal_code"])
        assert self.checkout_complete_page.get_back_home_button().is_displayed()
        assert self.checkout_complete_page.get_back_home_button().is_enabled()

    @allure.title('A Checkout Complete oldalon a "Back Home" gomb működésének az ellenőrzése')
    @allure.description('A teszteset célja annak ellenőrzése, hogy a Checkout Complete Page oldalon a "Back Home" '
                        'gomb megnyomásával visszajutunk-e a főoldalra.')
    @allure.severity(allure.severity_level.TRIVIAL)
    @allure.tag('checkout_complete', 'standard_user')
    def test_checkout_complete_button_back_home_functionality(self):
        self.checkout_complete_page.goto_checkout_complete_page(STANDARD_USER_LOGIN_DATA["username"],
                                                                STANDARD_USER_LOGIN_DATA["password"],
                                                                CHECKOUT_STEP_ONE_INPUT_VALID_TESTDATA["first_name"],
                                                                CHECKOUT_STEP_ONE_INPUT_VALID_TESTDATA["last_name"],
                                                                CHECKOUT_STEP_ONE_INPUT_VALID_TESTDATA["postal_code"])
        url_before_click = self.checkout_complete_page.get_current_url()
        self.checkout_complete_page.get_back_home_button().click()
        url_after_click = self.logged_in_page.get_current_url()
        assert url_before_click != url_after_click
        assert url_before_click == CHECKOUT_COMPLETE_PAGE_URL_TESTDATA
        assert url_after_click == LOGGED_IN_URL_TESTDATA
