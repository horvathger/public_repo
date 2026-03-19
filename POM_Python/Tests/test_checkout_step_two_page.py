import allure

from POM_Python.Data.checkout_step_one_testdata import CHECKOUT_STEP_ONE_INPUT_VALID_TESTDATA
from POM_Python.Data.checkout_step_two_testdata import (CHECKOUT_STEP_TWO_PAGE_ITEM_TOTAL_TESTDATA,
                                                        CHECKOUT_STEP_TWO_PAGE_TOTAL_TESTDATA)
from POM_Python.Data.url_testdata import CHECKOUT_STEP_TWO_PAGE_URL_TESTDATA, LOGGED_IN_URL_TESTDATA
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

    @allure.title('A Checkout Step Two Page oldalon a termékek összértékének ellenőrzése')
    @allure.description('A teszteset célja annak ellenőrzése, hogy a Checkout Step Two Page-en az egyes termékek '
                        'árainak összege megegyezik-e az "Item total:" mezőben szereplő összeggel.')
    @allure.severity(allure.severity_level.TRIVIAL)
    @allure.tag('checkout_step_two', 'price', 'standard_user')
    def test_checkout_step_two_page_item_price_summary(self):
        self.checkout_step_two_page.goto_checkout_step_two_page(STANDARD_USER_LOGIN_DATA["username"],
                                                                STANDARD_USER_LOGIN_DATA["password"],
                                                                CHECKOUT_STEP_ONE_INPUT_VALID_TESTDATA["first_name"],
                                                                CHECKOUT_STEP_ONE_INPUT_VALID_TESTDATA["last_name"],
                                                                CHECKOUT_STEP_ONE_INPUT_VALID_TESTDATA["postal_code"])
        number_of_items = len(self.checkout_step_two_page.get_items_list())
        items_total = None
        for index in range(number_of_items):
            item_price = self.checkout_step_two_page.get_item_price_list()[index].text
            item_price = float(item_price.replace("$", ""))
            item_quantity = self.checkout_step_two_page.get_items_quantity_list()[index].text
            item_quantity = int(item_quantity)
            item_total_price = item_price * item_quantity
            if items_total is None:
                items_total = item_total_price
            else:
                items_total += item_total_price

        assert items_total == float(CHECKOUT_STEP_TWO_PAGE_ITEM_TOTAL_TESTDATA.replace("Item total: $", ""))

        item_total_numeric = float(self.checkout_step_two_page.get_item_total().text.replace("Item total: $", ""))

        assert item_total_numeric == float(CHECKOUT_STEP_TWO_PAGE_ITEM_TOTAL_TESTDATA.replace("Item total: $", ""))

    @allure.title('A Checkout Step Two Page oldalon a termékek összértéke + adó egyenlő-e a végösszeggel')
    @allure.description('A teszteset célja annak ellenőrzése, hogy a Checkout Step Two Page-en az egyes termékek '
                        'árainak összegéhez ha hozzá adjuk az adó összegét, akkor megkapjuk-e a számla végösszegét.')
    @allure.severity(allure.severity_level.TRIVIAL)
    @allure.tag('checkout_step_two', 'price', 'standard_user')
    def test_checkout_step_two_page_items_price_plus_total_eqv_total(self):
        self.checkout_step_two_page.goto_checkout_step_two_page(STANDARD_USER_LOGIN_DATA["username"],
                                                                STANDARD_USER_LOGIN_DATA["password"],
                                                                CHECKOUT_STEP_ONE_INPUT_VALID_TESTDATA["first_name"],
                                                                CHECKOUT_STEP_ONE_INPUT_VALID_TESTDATA["last_name"],
                                                                CHECKOUT_STEP_ONE_INPUT_VALID_TESTDATA["postal_code"])

        item_total_numeric = float(self.checkout_step_two_page.get_item_total().text.replace("Item total: $", ""))
        tax_numeric = float(self.checkout_step_two_page.get_tax().text.replace("Tax: $", ""))
        total_numeric = float(self.checkout_step_two_page.get_total().text.replace("Total: $", ""))

        assert item_total_numeric + tax_numeric == total_numeric
        assert total_numeric == float(CHECKOUT_STEP_TWO_PAGE_TOTAL_TESTDATA.replace("Total: $", ""))

    @allure.title('A Checkout Step Two Page oldalon a Cancel gomb működésének ellenőrzése')
    @allure.description('A teszteset célja annak ellenőrzése, hogy a Checkout Step Two Page-en a Cancel gomb '
                        'megnyomásával visszajutunk-e az előző oldalra.')
    @allure.severity(allure.severity_level.TRIVIAL)
    @allure.tag('checkout_step_two', 'price', 'standard_user')
    def test_checkout_step_two_page_button_cancel_functionality(self):
        self.checkout_step_two_page.goto_checkout_step_two_page(STANDARD_USER_LOGIN_DATA["username"],
                                                                STANDARD_USER_LOGIN_DATA["password"],
                                                                CHECKOUT_STEP_ONE_INPUT_VALID_TESTDATA["first_name"],
                                                                CHECKOUT_STEP_ONE_INPUT_VALID_TESTDATA["last_name"],
                                                                CHECKOUT_STEP_ONE_INPUT_VALID_TESTDATA["postal_code"])
        url_before_cancel = self.checkout_step_two_page.get_current_url()
        self.checkout_step_two_page.get_button_cancel().click()
        url_after_cancel = self.logged_in_page.get_current_url()

        assert url_before_cancel != url_after_cancel
        assert url_after_cancel == LOGGED_IN_URL_TESTDATA
        assert url_before_cancel == CHECKOUT_STEP_TWO_PAGE_URL_TESTDATA
