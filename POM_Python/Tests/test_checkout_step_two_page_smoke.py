import allure

from POM_Python.Data.cart_testdata import CART_TESTDATA
from POM_Python.Data.checkout_step_one_testdata import CHECKOUT_STEP_ONE_INPUT_VALID_TESTDATA
from POM_Python.Data.checkout_step_two_testdata import (CHECKOUT_STEP_TWO_PAGE_HEADER, CHECKOUT_STEP_TWO_URL,
                                                        CHECKOUT_STEP_TWO_PAGE_PAYMENT_INFO_TESTDATA,
                                                        CHECKOUT_STEP_TWO_PAGE_SHIPPING_INFO_TESTDATA,
                                                        CHECKOUT_STEP_TWO_PAGE_ITEM_TOTAL_TESTDATA,
                                                        CHECKOUT_STEP_TWO_PAGE_TAX_TESTDATA,
                                                        CHECKOUT_STEP_TWO_PAGE_TOTAL_TESTDATA)
from POM_Python.Data.user_testdata import STANDARD_USER_LOGIN_DATA
from POM_Python.Pages.CheckoutStepTwoPage import CheckoutStepTwoPage
from POM_Python.Pages.LoggedInPage import LoggedInPage
from POM_Python.Utils.create_driver import create_preconfigured_chrome_driver


@allure.parent_suite("UI Tests")
@allure.suite("Checkout Step Two page smoke tests")
@allure.sub_suite("Test cases")
class TestCheckoutStepTwoPageSmoke:
    def setup_method(self):
        browser = create_preconfigured_chrome_driver()
        self.checkout_step_two_page = CheckoutStepTwoPage(browser)
        self.logged_in_page = LoggedInPage(browser)

    def teardown_method(self):
        self.checkout_step_two_page.quit()

    @allure.title('A Checkout Step Two Page oldal fejszövegének ellenőrzése')
    @allure.description('A teszteset célja annak ellenőrzése, hogy a Checkout Step Two Page fejszövege megjelenik-e.')
    @allure.severity(allure.severity_level.TRIVIAL)
    @allure.tag('checkout_step_two', 'smoke', 'standard_user')
    def test_checkout_step_two_page_header_visibility(self):
        self.checkout_step_two_page.goto_checkout_step_two_page(STANDARD_USER_LOGIN_DATA["username"],
                                                                STANDARD_USER_LOGIN_DATA["password"],
                                                                CHECKOUT_STEP_ONE_INPUT_VALID_TESTDATA["first_name"],
                                                                CHECKOUT_STEP_ONE_INPUT_VALID_TESTDATA["last_name"],
                                                                CHECKOUT_STEP_ONE_INPUT_VALID_TESTDATA["postal_code"])
        assert self.checkout_step_two_page.get_page_header().is_displayed()
        assert self.checkout_step_two_page.get_page_header().text == CHECKOUT_STEP_TWO_PAGE_HEADER
        assert self.checkout_step_two_page.get_current_url() == CHECKOUT_STEP_TWO_URL

    @allure.title('A Checkout Step Two Page oldalon a termékek számának ellenőrzése')
    @allure.description('A teszteset célja annak ellenőrzése, hogy a Checkout Step Two Page-en megjelennek-e a '
                        'termékmennyiséget tartalmazó mezők.')
    @allure.severity(allure.severity_level.TRIVIAL)
    @allure.tag('checkout_step_two', 'smoke', 'standard_user')
    def test_checkout_step_two_page_item_quantity_visibility(self):
        self.checkout_step_two_page.goto_checkout_step_two_page(STANDARD_USER_LOGIN_DATA["username"],
                                                                STANDARD_USER_LOGIN_DATA["password"],
                                                                CHECKOUT_STEP_ONE_INPUT_VALID_TESTDATA["first_name"],
                                                                CHECKOUT_STEP_ONE_INPUT_VALID_TESTDATA["last_name"],
                                                                CHECKOUT_STEP_ONE_INPUT_VALID_TESTDATA["postal_code"])

        assert self.checkout_step_two_page.get_items_quantity_list() != []

        shopping_cart_item_counter = self.logged_in_page.get_number_of_items_in_cart()
        assert len(self.checkout_step_two_page.get_items_quantity_list()) == shopping_cart_item_counter
        assert (len(self.checkout_step_two_page.get_items_quantity_list()) == len(
            self.checkout_step_two_page.get_items_list()))

    @allure.title('A Checkout Step Two Page oldalon megjelennek-e a termékek nevei')
    @allure.description('A teszteset célja annak ellenőrzése, hogy a Checkout Step Two Page-en megjelennek-e a '
                        'termékek nevei.')
    @allure.severity(allure.severity_level.TRIVIAL)
    @allure.tag('checkout_step_two', 'smoke', 'standard_user')
    def test_checkout_step_two_page_item_name_visibility(self):
        self.checkout_step_two_page.goto_checkout_step_two_page(STANDARD_USER_LOGIN_DATA["username"],
                                                                STANDARD_USER_LOGIN_DATA["password"],
                                                                CHECKOUT_STEP_ONE_INPUT_VALID_TESTDATA["first_name"],
                                                                CHECKOUT_STEP_ONE_INPUT_VALID_TESTDATA["last_name"],
                                                                CHECKOUT_STEP_ONE_INPUT_VALID_TESTDATA["postal_code"])
        assert self.checkout_step_two_page.get_item_name_list()[0].is_displayed()
        assert self.checkout_step_two_page.get_item_name_list()[0].text == CART_TESTDATA['cart_item_1']['name']
        assert self.checkout_step_two_page.get_item_name_list()[1].is_displayed()
        assert self.checkout_step_two_page.get_item_name_list()[1].text == CART_TESTDATA['cart_item_2']['name']

    @allure.title('A Checkout Step Two Page oldalon megjelennek-e a termékek leírásai')
    @allure.description('A teszteset célja annak ellenőrzése, hogy a Checkout Step Two Page-en megjelennek-e a '
                        'termékek leírásai.')
    @allure.severity(allure.severity_level.TRIVIAL)
    @allure.tag('checkout_step_two', 'smoke', 'standard_user')
    def test_checkout_step_two_page_item_description_visibility(self):
        self.checkout_step_two_page.goto_checkout_step_two_page(STANDARD_USER_LOGIN_DATA["username"],
                                                                STANDARD_USER_LOGIN_DATA["password"],
                                                                CHECKOUT_STEP_ONE_INPUT_VALID_TESTDATA["first_name"],
                                                                CHECKOUT_STEP_ONE_INPUT_VALID_TESTDATA["last_name"],
                                                                CHECKOUT_STEP_ONE_INPUT_VALID_TESTDATA["postal_code"])
        assert self.checkout_step_two_page.get_item_description_list()[0].is_displayed()
        assert (self.checkout_step_two_page.get_item_description_list()[0].text == CART_TESTDATA['cart_item_1'][
            'description'])
        assert self.checkout_step_two_page.get_item_description_list()[1].is_displayed()
        assert (self.checkout_step_two_page.get_item_description_list()[1].text == CART_TESTDATA['cart_item_2'][
            'description'])

    @allure.title('A Checkout Step Two Page oldalon megjelennek-e a termékek árai')
    @allure.description('A teszteset célja annak ellenőrzése, hogy a Checkout Step Two Page-en megjelennek-e a '
                        'termékek árai.')
    @allure.severity(allure.severity_level.TRIVIAL)
    @allure.tag('checkout_step_two', 'smoke', 'standard_user')
    def test_checkout_step_two_page_item_price_visibility(self):
        self.checkout_step_two_page.goto_checkout_step_two_page(STANDARD_USER_LOGIN_DATA["username"],
                                                                STANDARD_USER_LOGIN_DATA["password"],
                                                                CHECKOUT_STEP_ONE_INPUT_VALID_TESTDATA["first_name"],
                                                                CHECKOUT_STEP_ONE_INPUT_VALID_TESTDATA["last_name"],
                                                                CHECKOUT_STEP_ONE_INPUT_VALID_TESTDATA["postal_code"])
        assert self.checkout_step_two_page.get_item_price_list()[0].is_displayed()
        assert self.checkout_step_two_page.get_item_price_list()[0].text == CART_TESTDATA['cart_item_1']['price']
        assert self.checkout_step_two_page.get_item_price_list()[1].is_displayed()
        assert self.checkout_step_two_page.get_item_price_list()[1].text == CART_TESTDATA['cart_item_2']['price']

    @allure.title('A Checkout Step Two Page oldalon megjelenik-e a "Payment Information" mező.')
    @allure.description('A teszteset célja annak ellenőrzése, hogy a Checkout Step Two Page-en megjelenik-e a '
                        '"Payment Information" mező.')
    @allure.severity(allure.severity_level.TRIVIAL)
    @allure.tag('checkout_step_two', 'smoke', 'standard_user')
    def test_checkout_step_two_page_payment_information_visibility(self):
        self.checkout_step_two_page.goto_checkout_step_two_page(STANDARD_USER_LOGIN_DATA["username"],
                                                                STANDARD_USER_LOGIN_DATA["password"],
                                                                CHECKOUT_STEP_ONE_INPUT_VALID_TESTDATA["first_name"],
                                                                CHECKOUT_STEP_ONE_INPUT_VALID_TESTDATA["last_name"],
                                                                CHECKOUT_STEP_ONE_INPUT_VALID_TESTDATA["postal_code"])
        assert self.checkout_step_two_page.get_payment_info().is_displayed()
        assert self.checkout_step_two_page.get_payment_info().text == CHECKOUT_STEP_TWO_PAGE_PAYMENT_INFO_TESTDATA

    @allure.title('A Checkout Step Two Page oldalon megjelenik-e a "Shipping Information" mező.')
    @allure.description('A teszteset célja annak ellenőrzése, hogy a Checkout Step Two Page-en megjelenik-e a '
                        '"Shipping Information" mező.')
    @allure.severity(allure.severity_level.TRIVIAL)
    @allure.tag('checkout_step_two', 'smoke', 'standard_user')
    def test_checkout_step_two_page_shipping_information_visibility(self):
        self.checkout_step_two_page.goto_checkout_step_two_page(STANDARD_USER_LOGIN_DATA["username"],
                                                                STANDARD_USER_LOGIN_DATA["password"],
                                                                CHECKOUT_STEP_ONE_INPUT_VALID_TESTDATA["first_name"],
                                                                CHECKOUT_STEP_ONE_INPUT_VALID_TESTDATA["last_name"],
                                                                CHECKOUT_STEP_ONE_INPUT_VALID_TESTDATA["postal_code"])
        assert self.checkout_step_two_page.get_shipping_info().is_displayed()
        assert self.checkout_step_two_page.get_shipping_info().text == CHECKOUT_STEP_TWO_PAGE_SHIPPING_INFO_TESTDATA

    @allure.title('A Checkout Step Two Page oldalon megjelenik-e az "Item total:" mező.')
    @allure.description('A teszteset célja annak ellenőrzése, hogy a Checkout Step Two Page-en megjelenik-e a '
                        '"Item total" mező.')
    @allure.severity(allure.severity_level.TRIVIAL)
    @allure.tag('checkout_step_two', 'smoke', 'standard_user')
    def test_checkout_step_two_page_item_total_visibility(self):
        self.checkout_step_two_page.goto_checkout_step_two_page(STANDARD_USER_LOGIN_DATA["username"],
                                                                STANDARD_USER_LOGIN_DATA["password"],
                                                                CHECKOUT_STEP_ONE_INPUT_VALID_TESTDATA["first_name"],
                                                                CHECKOUT_STEP_ONE_INPUT_VALID_TESTDATA["last_name"],
                                                                CHECKOUT_STEP_ONE_INPUT_VALID_TESTDATA["postal_code"])
        assert self.checkout_step_two_page.get_item_total().is_displayed()
        assert self.checkout_step_two_page.get_item_total().text == CHECKOUT_STEP_TWO_PAGE_ITEM_TOTAL_TESTDATA

    @allure.title('A Checkout Step Two Page oldalon megjelenik-e az "Tax:" mező.')
    @allure.description('A teszteset célja annak ellenőrzése, hogy a Checkout Step Two Page-en megjelenik-e a '
                        '"Tax" mező.')
    @allure.severity(allure.severity_level.TRIVIAL)
    @allure.tag('checkout_step_two', 'smoke', 'standard_user')
    def test_checkout_step_two_page_tax_visibility(self):
        self.checkout_step_two_page.goto_checkout_step_two_page(STANDARD_USER_LOGIN_DATA["username"],
                                                                STANDARD_USER_LOGIN_DATA["password"],
                                                                CHECKOUT_STEP_ONE_INPUT_VALID_TESTDATA["first_name"],
                                                                CHECKOUT_STEP_ONE_INPUT_VALID_TESTDATA["last_name"],
                                                                CHECKOUT_STEP_ONE_INPUT_VALID_TESTDATA["postal_code"])
        assert self.checkout_step_two_page.get_tax().is_displayed()
        assert self.checkout_step_two_page.get_tax().text == CHECKOUT_STEP_TWO_PAGE_TAX_TESTDATA

    @allure.title('A Checkout Step Two Page oldalon megjelenik-e az "Total:" mező.')
    @allure.description('A teszteset célja annak ellenőrzése, hogy a Checkout Step Two Page-en megjelenik-e a '
                        '"Total:" mező.')
    @allure.severity(allure.severity_level.TRIVIAL)
    @allure.tag('checkout_step_two', 'smoke', 'standard_user')
    def test_checkout_step_two_page_total_visibility(self):
        self.checkout_step_two_page.goto_checkout_step_two_page(STANDARD_USER_LOGIN_DATA["username"],
                                                                STANDARD_USER_LOGIN_DATA["password"],
                                                                CHECKOUT_STEP_ONE_INPUT_VALID_TESTDATA["first_name"],
                                                                CHECKOUT_STEP_ONE_INPUT_VALID_TESTDATA["last_name"],
                                                                CHECKOUT_STEP_ONE_INPUT_VALID_TESTDATA["postal_code"])
        assert self.checkout_step_two_page.get_total().is_displayed()
        assert self.checkout_step_two_page.get_total().text == CHECKOUT_STEP_TWO_PAGE_TOTAL_TESTDATA

    @allure.title('A Checkout Step Two Page oldalon megjelenik-e az "Cancel" gomb.')
    @allure.description('A teszteset célja annak ellenőrzése, hogy a Checkout Step Two Page-en megjelenik-e a '
                        '"Cancel" gomb.')
    @allure.severity(allure.severity_level.TRIVIAL)
    @allure.tag('checkout_step_two', 'smoke', 'standard_user')
    def test_checkout_step_two_page_button_cancel_visibility(self):
        self.checkout_step_two_page.goto_checkout_step_two_page(STANDARD_USER_LOGIN_DATA["username"],
                                                                STANDARD_USER_LOGIN_DATA["password"],
                                                                CHECKOUT_STEP_ONE_INPUT_VALID_TESTDATA["first_name"],
                                                                CHECKOUT_STEP_ONE_INPUT_VALID_TESTDATA["last_name"],
                                                                CHECKOUT_STEP_ONE_INPUT_VALID_TESTDATA["postal_code"])
        assert self.checkout_step_two_page.get_button_cancel().is_displayed()
        assert self.checkout_step_two_page.get_button_cancel().is_enabled()

    @allure.title('A Checkout Step Two Page oldalon megjelenik-e az "Finish" gomb.')
    @allure.description('A teszteset célja annak ellenőrzése, hogy a Checkout Step Two Page-en megjelenik-e a '
                        '"Finish" gomb.')
    @allure.severity(allure.severity_level.TRIVIAL)
    @allure.tag('checkout_step_two', 'smoke', 'standard_user')
    def test_checkout_step_two_page_button_finish_visibility(self):
        self.checkout_step_two_page.goto_checkout_step_two_page(STANDARD_USER_LOGIN_DATA["username"],
                                                                STANDARD_USER_LOGIN_DATA["password"],
                                                                CHECKOUT_STEP_ONE_INPUT_VALID_TESTDATA["first_name"],
                                                                CHECKOUT_STEP_ONE_INPUT_VALID_TESTDATA["last_name"],
                                                                CHECKOUT_STEP_ONE_INPUT_VALID_TESTDATA["postal_code"])
        assert self.checkout_step_two_page.get_button_finish().is_displayed()
        assert self.checkout_step_two_page.get_button_finish().is_enabled()
