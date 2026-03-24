import allure
import pytest

from POM_Python.Data.cart_testdata import CART_TESTDATA
from POM_Python.Data.checkout_step_one_testdata import CHECKOUT_STEP_ONE_INPUT_VALID_TESTDATA
from POM_Python.Data.checkout_step_two_testdata import (CHECKOUT_STEP_TWO_PAGE_HEADER, CHECKOUT_STEP_TWO_URL,
                                                        CHECKOUT_STEP_TWO_PAGE_PAYMENT_INFO_TESTDATA,
                                                        CHECKOUT_STEP_TWO_PAGE_SHIPPING_INFO_TESTDATA,
                                                        CHECKOUT_STEP_TWO_PAGE_ITEM_TOTAL_TESTDATA,
                                                        CHECKOUT_STEP_TWO_PAGE_TAX_TESTDATA,
                                                        CHECKOUT_STEP_TWO_PAGE_TOTAL_TESTDATA)
from POM_Python.Data.user_testdata import STANDARD_USER_LOGIN_DATA, ALLOWED_USERS_LOGIN_DATA
from POM_Python.Pages.CheckoutStepTwoPage import CheckoutStepTwoPage
from POM_Python.Pages.LoggedInPage import LoggedInPage
from POM_Python.Utils.create_driver import create_preconfigured_chrome_driver


@pytest.fixture
def driver():
    driver = create_preconfigured_chrome_driver()
    yield driver
    driver.quit()


@pytest.fixture
def pages(driver):
    checkout_step_two_page = CheckoutStepTwoPage(driver)
    logged_in_page = LoggedInPage(driver)

    return {
        "checkout_step_two_page": checkout_step_two_page,
        "logged_in_page": logged_in_page
    }


@pytest.fixture
def user(request):
    return request.param


@allure.parent_suite("SAUCE - 26 project")
@allure.suite("Checkout Step Two page smoke tests")
@allure.sub_suite("Test Cycle - 007")
class TestCheckoutStepTwoPageSmoke:

    @pytest.mark.parametrize("user", ALLOWED_USERS_LOGIN_DATA, ids=[u["username"] for u in ALLOWED_USERS_LOGIN_DATA],
                             indirect=True)
    @allure.severity(allure.severity_level.TRIVIAL)
    @allure.tag('checkout_step_two', 'smoke')
    def test_checkout_step_two_page_header_visibility(self, user, pages):
        allure.dynamic.title(f'A Checkout Step Two Page oldal fejszövegének ellenőrzése ({user["username"]} '
                             f'felhasználó)')
        allure.dynamic.description(f'A teszteset célja annak ellenőrzése, hogy {user["username"]} userrel belépve, '
                                   f'a Checkout Step Two Page fejszövege megjelenik-e.')
        allure.dynamic.tag(f'{user["username"]}')
        checkout_step_two_page = pages["checkout_step_two_page"]

        checkout_step_two_page.goto_checkout_step_two_page(STANDARD_USER_LOGIN_DATA["username"],
                                                           STANDARD_USER_LOGIN_DATA["password"],
                                                           CHECKOUT_STEP_ONE_INPUT_VALID_TESTDATA["first_name"],
                                                           CHECKOUT_STEP_ONE_INPUT_VALID_TESTDATA["last_name"],
                                                           CHECKOUT_STEP_ONE_INPUT_VALID_TESTDATA["postal_code"])

        assert checkout_step_two_page.get_current_url() == CHECKOUT_STEP_TWO_URL
        assert checkout_step_two_page.get_page_header().is_displayed()
        assert checkout_step_two_page.get_page_header().text == CHECKOUT_STEP_TWO_PAGE_HEADER

    @pytest.mark.parametrize("user", ALLOWED_USERS_LOGIN_DATA, ids=[u["username"] for u in ALLOWED_USERS_LOGIN_DATA],
                             indirect=True)
    @allure.severity(allure.severity_level.TRIVIAL)
    @allure.tag('checkout_step_two', 'smoke')
    def test_checkout_step_two_page_item_quantity_visibility(self, user, pages):
        allure.dynamic.title(f'A Checkout Step Two Page oldalon a termékek számának ellenőrzése ({user["username"]} '
                             f'felhasználó)')
        allure.dynamic.description(f'A teszteset célja annak ellenőrzése, hogy {user["username"]} userrel belépve a '
                                   f'Checkout Step Two Page-en megjelennek-e a termékmennyiséget tartalmazó mezők.')
        allure.dynamic.tag(f'{user["username"]}')
        checkout_step_two_page = pages["checkout_step_two_page"]
        logged_in_page = pages["logged_in_page"]

        checkout_step_two_page.goto_checkout_step_two_page(STANDARD_USER_LOGIN_DATA["username"],
                                                           STANDARD_USER_LOGIN_DATA["password"],
                                                           CHECKOUT_STEP_ONE_INPUT_VALID_TESTDATA["first_name"],
                                                           CHECKOUT_STEP_ONE_INPUT_VALID_TESTDATA["last_name"],
                                                           CHECKOUT_STEP_ONE_INPUT_VALID_TESTDATA["postal_code"])

        assert checkout_step_two_page.get_items_quantity_list() != []

        shopping_cart_item_counter = logged_in_page.get_number_of_items_in_cart()
        assert len(checkout_step_two_page.get_items_quantity_list()) == shopping_cart_item_counter
        assert len(checkout_step_two_page.get_items_quantity_list()) == len(checkout_step_two_page.get_items_list())

    @pytest.mark.parametrize("user", ALLOWED_USERS_LOGIN_DATA, ids=[u["username"] for u in ALLOWED_USERS_LOGIN_DATA],
                             indirect=True)
    @allure.severity(allure.severity_level.TRIVIAL)
    @allure.tag('checkout_step_two', 'smoke')
    def test_checkout_step_two_page_item_name_visibility(self, user, pages):
        allure.dynamic.title(f'A Checkout Step Two Page oldalon megjelennek-e a termékek nevei '
                             f'({user["username"]} felhasználó)')
        allure.dynamic.description(f'A teszteset célja annak ellenőrzése, hogy {user["username"]} userrel belépve, '
                                   f'a Checkout Step Two Page-en megjelennek-e a termékek nevei.')
        allure.dynamic.tag(f'{user["username"]}')
        checkout_step_two_page = pages["checkout_step_two_page"]

        checkout_step_two_page.goto_checkout_step_two_page(STANDARD_USER_LOGIN_DATA["username"],
                                                           STANDARD_USER_LOGIN_DATA["password"],
                                                           CHECKOUT_STEP_ONE_INPUT_VALID_TESTDATA["first_name"],
                                                           CHECKOUT_STEP_ONE_INPUT_VALID_TESTDATA["last_name"],
                                                           CHECKOUT_STEP_ONE_INPUT_VALID_TESTDATA["postal_code"])
        assert checkout_step_two_page.get_item_name_list()[0].is_displayed()
        assert checkout_step_two_page.get_item_name_list()[0].text == CART_TESTDATA['cart_item_1']['name']
        assert checkout_step_two_page.get_item_name_list()[1].is_displayed()
        assert checkout_step_two_page.get_item_name_list()[1].text == CART_TESTDATA['cart_item_2']['name']

    @pytest.mark.parametrize("user", ALLOWED_USERS_LOGIN_DATA, ids=[u["username"] for u in ALLOWED_USERS_LOGIN_DATA],
                             indirect=True)
    @allure.severity(allure.severity_level.TRIVIAL)
    @allure.tag('checkout_step_two', 'smoke')
    def test_checkout_step_two_page_item_description_visibility(self, user, pages):
        allure.dynamic.title(f'A Checkout Step Two Page oldalon megjelennek-e a termékek leírásai ({user["username"]}'
                             f' felhasználó)')
        allure.dynamic.description(f'A teszteset célja annak ellenőrzése, hogy {user["username"]} userrel belépve, '
                                   f'a Checkout Step Two Page-en megjelennek-e a termékek leírásai.')
        allure.dynamic.tag(f'{user["username"]}')
        checkout_step_two_page = pages["checkout_step_two_page"]

        checkout_step_two_page.goto_checkout_step_two_page(STANDARD_USER_LOGIN_DATA["username"],
                                                           STANDARD_USER_LOGIN_DATA["password"],
                                                           CHECKOUT_STEP_ONE_INPUT_VALID_TESTDATA["first_name"],
                                                           CHECKOUT_STEP_ONE_INPUT_VALID_TESTDATA["last_name"],
                                                           CHECKOUT_STEP_ONE_INPUT_VALID_TESTDATA["postal_code"])

        assert checkout_step_two_page.get_item_description_list()[0].is_displayed()
        assert checkout_step_two_page.get_item_description_list()[0].text == CART_TESTDATA['cart_item_1'][
            'description']
        assert checkout_step_two_page.get_item_description_list()[1].is_displayed()
        assert checkout_step_two_page.get_item_description_list()[1].text == CART_TESTDATA['cart_item_2'][
            'description']

    @pytest.mark.parametrize("user", ALLOWED_USERS_LOGIN_DATA, ids=[u["username"] for u in ALLOWED_USERS_LOGIN_DATA],
                             indirect=True)
    @allure.severity(allure.severity_level.TRIVIAL)
    @allure.tag('checkout_step_two', 'smoke')
    def test_checkout_step_two_page_item_price_visibility(self, pages, user):
        allure.dynamic.title(f'A Checkout Step Two Page oldalon megjelennek-e a termékek árai ({user["username"]} '
                             f'felhasználó)')
        allure.dynamic.description(f'A teszteset célja annak ellenőrzése, hogy {user["username"]} userrel belépve, '
                                   f'a Checkout Step Two Page-en megjelennek-e a termékek árai.')
        allure.dynamic.tag(f'{user["username"]}')
        checkout_step_two_page = pages["checkout_step_two_page"]

        checkout_step_two_page.goto_checkout_step_two_page(STANDARD_USER_LOGIN_DATA["username"],
                                                           STANDARD_USER_LOGIN_DATA["password"],
                                                           CHECKOUT_STEP_ONE_INPUT_VALID_TESTDATA["first_name"],
                                                           CHECKOUT_STEP_ONE_INPUT_VALID_TESTDATA["last_name"],
                                                           CHECKOUT_STEP_ONE_INPUT_VALID_TESTDATA["postal_code"])
        assert checkout_step_two_page.get_item_price_list()[0].is_displayed()
        assert checkout_step_two_page.get_item_price_list()[0].text == CART_TESTDATA['cart_item_1']['price']
        assert checkout_step_two_page.get_item_price_list()[1].is_displayed()
        assert checkout_step_two_page.get_item_price_list()[1].text == CART_TESTDATA['cart_item_2']['price']

    @pytest.mark.parametrize("user", ALLOWED_USERS_LOGIN_DATA, ids=[u["username"] for u in ALLOWED_USERS_LOGIN_DATA],
                             indirect=True)
    @allure.severity(allure.severity_level.TRIVIAL)
    @allure.tag('checkout_step_two', 'smoke')
    def test_checkout_step_two_page_payment_information_visibility(self, user, pages):
        allure.dynamic.title(f'A Checkout Step Two Page oldalon megjelenik-e a "Payment Information" mező '
                             f'({user["username"]} felhasználó).')
        allure.dynamic.description(f'A teszteset célja annak ellenőrzése, hogy {user["username"]} userrel belépve '
                                   f'a Checkout Step Two Page-en megjelenik-e a "Payment Information" mező.')
        allure.dynamic.tag(f'{user["username"]}')
        checkout_step_two_page = pages["checkout_step_two_page"]

        checkout_step_two_page.goto_checkout_step_two_page(STANDARD_USER_LOGIN_DATA["username"],
                                                           STANDARD_USER_LOGIN_DATA["password"],
                                                           CHECKOUT_STEP_ONE_INPUT_VALID_TESTDATA["first_name"],
                                                           CHECKOUT_STEP_ONE_INPUT_VALID_TESTDATA["last_name"],
                                                           CHECKOUT_STEP_ONE_INPUT_VALID_TESTDATA["postal_code"])
        assert checkout_step_two_page.get_payment_info().is_displayed()
        assert checkout_step_two_page.get_payment_info().text == CHECKOUT_STEP_TWO_PAGE_PAYMENT_INFO_TESTDATA

    @pytest.mark.parametrize("user", ALLOWED_USERS_LOGIN_DATA, ids=[u["username"] for u in ALLOWED_USERS_LOGIN_DATA],
                             indirect=True)
    @allure.severity(allure.severity_level.TRIVIAL)
    @allure.tag('checkout_step_two', 'smoke')
    def test_checkout_step_two_page_shipping_information_visibility(self, user, pages):
        allure.dynamic.title(f'A Checkout Step Two Page oldalon megjelenik-e a "Shipping Information" mező. '
                             f'({user["username"]} felhasználó)')
        allure.dynamic.description(f'A teszteset célja annak ellenőrzése, hogy {user["username"]} a Checkout Step '
                                   f'Two Page-en megjelenik-e a "Shipping Information" mező.')
        allure.dynamic.tag(f'{user["username"]}')
        checkout_step_two_page = pages["checkout_step_two_page"]

        checkout_step_two_page.goto_checkout_step_two_page(STANDARD_USER_LOGIN_DATA["username"],
                                                           STANDARD_USER_LOGIN_DATA["password"],
                                                           CHECKOUT_STEP_ONE_INPUT_VALID_TESTDATA["first_name"],
                                                           CHECKOUT_STEP_ONE_INPUT_VALID_TESTDATA["last_name"],
                                                           CHECKOUT_STEP_ONE_INPUT_VALID_TESTDATA["postal_code"])
        assert checkout_step_two_page.get_shipping_info().is_displayed()
        assert checkout_step_two_page.get_shipping_info().text == CHECKOUT_STEP_TWO_PAGE_SHIPPING_INFO_TESTDATA

    @pytest.mark.parametrize("user", ALLOWED_USERS_LOGIN_DATA, ids=[u["username"] for u in ALLOWED_USERS_LOGIN_DATA],
                             indirect=True)
    @allure.severity(allure.severity_level.TRIVIAL)
    @allure.tag('checkout_step_two', 'smoke')
    def test_checkout_step_two_page_item_total_visibility(self, user, pages):
        allure.dynamic.title(f'A Checkout Step Two Page oldalon megjelenik-e az "Item total:" mező. '
                             f'({user["username"]} felhasználó)')
        allure.dynamic.description(f'A teszteset célja annak ellenőrzése, hogy {user["username"]} userrel belépve, '
                                   f'a Checkout Step Two Page-en megjelenik-e a "Item total" mező.')
        allure.dynamic.tag(f'{user["username"]}')
        checkout_step_two_page = pages["checkout_step_two_page"]

        checkout_step_two_page.goto_checkout_step_two_page(STANDARD_USER_LOGIN_DATA["username"],
                                                           STANDARD_USER_LOGIN_DATA["password"],
                                                           CHECKOUT_STEP_ONE_INPUT_VALID_TESTDATA["first_name"],
                                                           CHECKOUT_STEP_ONE_INPUT_VALID_TESTDATA["last_name"],
                                                           CHECKOUT_STEP_ONE_INPUT_VALID_TESTDATA["postal_code"])
        assert checkout_step_two_page.get_item_total().is_displayed()
        assert checkout_step_two_page.get_item_total().text == CHECKOUT_STEP_TWO_PAGE_ITEM_TOTAL_TESTDATA

    @pytest.mark.parametrize("user", ALLOWED_USERS_LOGIN_DATA, ids=[u["username"] for u in ALLOWED_USERS_LOGIN_DATA],
                             indirect=True)
    @allure.severity(allure.severity_level.TRIVIAL)
    @allure.tag('checkout_step_two', 'smoke')
    def test_checkout_step_two_page_tax_visibility(self, user, pages):
        allure.dynamic.title(f'A Checkout Step Two Page oldalon megjelenik-e a "Tax:" mező '
                             f'({user["username"]} felhasználó).')
        allure.dynamic.description(f'A teszteset célja annak ellenőrzése, hogy {user["username"]} userrel belépve, '
                                   f'a Checkout Step Two Page-en megjelenik-e a "Tax" mező.')
        allure.dynamic.tag(f'{user["username"]}')
        checkout_step_two_page = pages["checkout_step_two_page"]

        checkout_step_two_page.goto_checkout_step_two_page(STANDARD_USER_LOGIN_DATA["username"],
                                                           STANDARD_USER_LOGIN_DATA["password"],
                                                           CHECKOUT_STEP_ONE_INPUT_VALID_TESTDATA["first_name"],
                                                           CHECKOUT_STEP_ONE_INPUT_VALID_TESTDATA["last_name"],
                                                           CHECKOUT_STEP_ONE_INPUT_VALID_TESTDATA["postal_code"])
        assert checkout_step_two_page.get_tax().is_displayed()
        assert checkout_step_two_page.get_tax().text == CHECKOUT_STEP_TWO_PAGE_TAX_TESTDATA

    @pytest.mark.parametrize("user", ALLOWED_USERS_LOGIN_DATA, ids=[u["username"] for u in ALLOWED_USERS_LOGIN_DATA],
                             indirect=True)
    @allure.severity(allure.severity_level.TRIVIAL)
    @allure.tag('checkout_step_two', 'smoke')
    def test_checkout_step_two_page_total_visibility(self, user, pages):
        allure.dynamic.title(f'A Checkout Step Two Page oldalon megjelenik-e az "Total:" mező '
                             f'({user["username"]} felhasználó).')
        allure.dynamic.description(f'A teszteset célja annak ellenőrzése, hogy {user["username"]} userrel belépve, '
                                   f'a Checkout Step Two Page-en megjelenik-e a "Total:" mező.')
        allure.dynamic.tag(f'{user["username"]}')
        checkout_step_two_page = pages["checkout_step_two_page"]

        checkout_step_two_page.goto_checkout_step_two_page(STANDARD_USER_LOGIN_DATA["username"],
                                                           STANDARD_USER_LOGIN_DATA["password"],
                                                           CHECKOUT_STEP_ONE_INPUT_VALID_TESTDATA["first_name"],
                                                           CHECKOUT_STEP_ONE_INPUT_VALID_TESTDATA["last_name"],
                                                           CHECKOUT_STEP_ONE_INPUT_VALID_TESTDATA["postal_code"])
        assert checkout_step_two_page.get_total().is_displayed()
        assert checkout_step_two_page.get_total().text == CHECKOUT_STEP_TWO_PAGE_TOTAL_TESTDATA

    @pytest.mark.parametrize("user", ALLOWED_USERS_LOGIN_DATA, ids=[u["username"] for u in ALLOWED_USERS_LOGIN_DATA],
                             indirect=True)
    @allure.severity(allure.severity_level.TRIVIAL)
    @allure.tag('checkout_step_two', 'smoke')
    def test_checkout_step_two_page_button_cancel_visibility(self, user, pages):
        allure.dynamic.title(f'A Checkout Step Two Page oldalon megjelenik-e az "Cancel" gomb '
                             f'({user["username"]} felhasználó).')
        allure.dynamic.description(f'A teszteset célja annak ellenőrzése, hogy {user["username"]} userrel belépve, '
                                   f'a Checkout Step Two Page-en megjelenik-e a "Cancel" gomb.')
        allure.dynamic.tag(f'{user["username"]}')
        checkout_step_two_page = pages["checkout_step_two_page"]

        checkout_step_two_page.goto_checkout_step_two_page(STANDARD_USER_LOGIN_DATA["username"],
                                                           STANDARD_USER_LOGIN_DATA["password"],
                                                           CHECKOUT_STEP_ONE_INPUT_VALID_TESTDATA["first_name"],
                                                           CHECKOUT_STEP_ONE_INPUT_VALID_TESTDATA["last_name"],
                                                           CHECKOUT_STEP_ONE_INPUT_VALID_TESTDATA["postal_code"])
        assert checkout_step_two_page.get_button_cancel().is_displayed()
        assert checkout_step_two_page.get_button_cancel().is_enabled()

    @pytest.mark.parametrize("user", ALLOWED_USERS_LOGIN_DATA, ids=[u["username"] for u in ALLOWED_USERS_LOGIN_DATA],
                             indirect=True)
    @allure.severity(allure.severity_level.TRIVIAL)
    @allure.tag('checkout_step_two', 'smoke')
    def test_checkout_step_two_page_button_finish_visibility(self, user, pages):
        allure.dynamic.title(f'A Checkout Step Two Page oldalon megjelenik-e az "Finish" gomb '
                             f'({user["username"]} felhasználó).')
        allure.dynamic.description(f'A teszteset célja annak ellenőrzése, hogy {user["username"]} userrel belépve '
                                   f'a Checkout Step Two Page-en megjelenik-e a "Finish" gomb.')
        allure.dynamic.tag(f'{user["username"]}')
        checkout_step_two_page = pages["checkout_step_two_page"]

        checkout_step_two_page.goto_checkout_step_two_page(STANDARD_USER_LOGIN_DATA["username"],
                                                           STANDARD_USER_LOGIN_DATA["password"],
                                                           CHECKOUT_STEP_ONE_INPUT_VALID_TESTDATA["first_name"],
                                                           CHECKOUT_STEP_ONE_INPUT_VALID_TESTDATA["last_name"],
                                                           CHECKOUT_STEP_ONE_INPUT_VALID_TESTDATA["postal_code"])
        assert checkout_step_two_page.get_button_finish().is_displayed()
        assert checkout_step_two_page.get_button_finish().is_enabled()
