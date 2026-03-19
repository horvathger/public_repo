import allure

from POM_Python.Data.checkout_step_one_testdata import (CHECKOUT_STEP_ONE_INPUT_VALID_TESTDATA,
                                                        CHECKOUT_STEP_ONE_ERROR_MESSAGE_EMPTY_FIRSTNAME,
                                                        CHECKOUT_STEP_ONE_ERROR_MESSAGE_EMPTY_LASTNAME,
                                                        CHECKOUT_STEP_ONE_ERROR_MESSAGE_EMPTY_POSTALCODE)
from POM_Python.Data.url_testdata import CHECKOUT_STEP_TWO_PAGE_URL_TESTDATA
from POM_Python.Data.user_testdata import STANDARD_USER_LOGIN_DATA
from POM_Python.Pages.CheckoutStepOnePage import CheckoutStepOnePage
from POM_Python.Utils.create_driver import create_preconfigured_chrome_driver


@allure.parent_suite("UI Tests")
@allure.suite("Cart page UI tests")
@allure.sub_suite("Test cases")
class TestCheckoutStepOnePage:
    def setup_method(self):
        browser = create_preconfigured_chrome_driver()
        self.checkout_step_one_page = CheckoutStepOnePage(browser)

    def teardown_method(self):
        self.checkout_step_one_page.quit()

    @allure.title('A Checkout Step One Page form kitöltése pozitív ágon')
    @allure.description('A teszteset célja annak ellenőrzése, hogy a Checkout Step One Page form kitöltésével tovább '
                        'lehet-e lépni a Checkout Step Two Page-re.')
    @allure.severity(allure.severity_level.TRIVIAL)
    @allure.tag('checkout_step_one', 'positive', 'standard_user')
    def test_checkout_step_one_page_positive(self):
        self.checkout_step_one_page.goto_checkout_step_one_page(STANDARD_USER_LOGIN_DATA["username"],
                                                                STANDARD_USER_LOGIN_DATA["password"])
        self.checkout_step_one_page.get_input_first_name().send_keys(
            CHECKOUT_STEP_ONE_INPUT_VALID_TESTDATA['first_name'])
        self.checkout_step_one_page.get_input_last_name().send_keys(
            CHECKOUT_STEP_ONE_INPUT_VALID_TESTDATA['last_name'])
        (self.checkout_step_one_page.get_input_postal_code().send_keys
         (CHECKOUT_STEP_ONE_INPUT_VALID_TESTDATA['postal_code']))
        self.checkout_step_one_page.get_button_continue().click()
        assert self.checkout_step_one_page.get_current_url() == CHECKOUT_STEP_TWO_PAGE_URL_TESTDATA

    @allure.title('A Checkout Step One Page form firstname nélküli kitöltése és továbblépés kísérlete')
    @allure.description('A teszteset célja annak ellenőrzése, hogy a Checkout Step One Page form kitöltése során a '
                        'firstname mező üresen hagyását követően tovább lehet-e lépni a Checkout Step Two Page-re.')
    @allure.severity(allure.severity_level.TRIVIAL)
    @allure.tag('checkout_step_one', 'negatív', 'standard_user')
    def test_checkout_step_one_page_empty_firstname(self):
        self.checkout_step_one_page.goto_checkout_step_one_page(STANDARD_USER_LOGIN_DATA["username"],
                                                                STANDARD_USER_LOGIN_DATA["password"])
        self.checkout_step_one_page.get_input_last_name().send_keys(
            CHECKOUT_STEP_ONE_INPUT_VALID_TESTDATA['last_name'])
        self.checkout_step_one_page.get_input_postal_code().send_keys(
            CHECKOUT_STEP_ONE_INPUT_VALID_TESTDATA['postal_code'])
        self.checkout_step_one_page.get_button_continue().click()

        assert self.checkout_step_one_page.get_error_message().text == CHECKOUT_STEP_ONE_ERROR_MESSAGE_EMPTY_FIRSTNAME

    @allure.title('A Checkout Step One Page form lastname nélküli kitöltése és továbblépés kísérlete')
    @allure.description('A teszteset célja annak ellenőrzése, hogy a Checkout Step One Page form kitöltése során a '
                        'lastname mező üresen hagyását követően tovább lehet-e lépni a Checkout Step Two Page-re.')
    @allure.severity(allure.severity_level.TRIVIAL)
    @allure.tag('checkout_step_one', 'negatív', 'standard_user')
    def test_checkout_step_one_page_empty_lastname(self):
        self.checkout_step_one_page.goto_checkout_step_one_page(STANDARD_USER_LOGIN_DATA["username"],
                                                                STANDARD_USER_LOGIN_DATA["password"])
        self.checkout_step_one_page.get_input_first_name().send_keys(
            CHECKOUT_STEP_ONE_INPUT_VALID_TESTDATA['first_name'])
        self.checkout_step_one_page.get_input_postal_code().send_keys(
            CHECKOUT_STEP_ONE_INPUT_VALID_TESTDATA['postal_code'])
        self.checkout_step_one_page.get_button_continue().click()

        assert self.checkout_step_one_page.get_error_message().text == CHECKOUT_STEP_ONE_ERROR_MESSAGE_EMPTY_LASTNAME

    @allure.title('A Checkout Step One Page form postal code nélküli kitöltése és továbblépés kísérlete')
    @allure.description('A teszteset célja annak ellenőrzése, hogy a Checkout Step One Page form kitöltése során a '
                        'postal code mező üresen hagyását követően tovább lehet-e lépni a Checkout Step Two Page-re.')
    @allure.severity(allure.severity_level.TRIVIAL)
    @allure.tag('checkout_step_one', 'negatív', 'standard_user')
    def test_checkout_step_one_page_empty_postal_code(self):
        self.checkout_step_one_page.goto_checkout_step_one_page(STANDARD_USER_LOGIN_DATA["username"],
                                                                STANDARD_USER_LOGIN_DATA["password"])
        self.checkout_step_one_page.get_input_first_name().send_keys(
            CHECKOUT_STEP_ONE_INPUT_VALID_TESTDATA['first_name'])
        self.checkout_step_one_page.get_input_last_name().send_keys(
            CHECKOUT_STEP_ONE_INPUT_VALID_TESTDATA['last_name'])
        self.checkout_step_one_page.get_button_continue().click()

        assert self.checkout_step_one_page.get_error_message().text == CHECKOUT_STEP_ONE_ERROR_MESSAGE_EMPTY_POSTALCODE
