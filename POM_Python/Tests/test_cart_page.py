import allure
import pytest

from POM_Python.Data.cart_testdata import CART_TESTDATA
from POM_Python.Data.checkout_step_one_testdata import CHECKOUT_STEP_ONE_PAGE_HEADER
from POM_Python.Data.user_testdata import ALLOWED_USERS_LOGIN_DATA
from POM_Python.Pages.CartPage import CartPage
from POM_Python.Pages.CheckoutStepOnePage import CheckoutStepOnePage
from POM_Python.Pages.LoggedInPage import LoggedInPage
from POM_Python.Utils.create_driver import create_preconfigured_chrome_driver


@pytest.fixture
def driver():
    driver = create_preconfigured_chrome_driver()
    yield driver
    driver.quit()


@pytest.fixture
def pages(driver, user):
    cart_page = CartPage(driver)
    logged_in_page = LoggedInPage(driver)
    checkout_step_one_page = CheckoutStepOnePage(driver)

    cart_page.goto_cart_page_with_two_items(user["username"], user["password"])

    return {
        "cart_page": cart_page,
        "logged_in_page": logged_in_page,
        "checkout_step_one_page": checkout_step_one_page,
    }


@allure.parent_suite("SAUCE - 26 project")
@allure.suite("Cart page UI tests")
@allure.sub_suite("Test Cycle - 001")
class TestCartPage:
    @pytest.mark.parametrize("user", ALLOWED_USERS_LOGIN_DATA, ids=[u["username"] for u in ALLOWED_USERS_LOGIN_DATA])
    @allure.severity(allure.severity_level.NORMAL)
    @allure.tag('cart')
    def test_cart_page_remove_item_button(self, user, pages):
        allure.dynamic.title(f'A Cart Page oldalon a termék törlése funkció ellenőrzése ({user["username"]})')
        allure.dynamic.description(f'A teszteset célja annak ellenőrzése, hogy {user["username"]} userrel belépve, '
                                   f'a bevásárló kosárban a termékek melletti "Remove" gombbal '
                                   f'törölhetők-e a termékek.')
        allure.dynamic.tag(f'{user["username"]}')
        cart_page = pages["cart_page"]

        item_count_before_removal = len(cart_page.get_cart_items())
        cart_page.get_cart_item_remove_buttons()[0].click()
        item_count_after_removal = len(cart_page.get_cart_items())
        assert item_count_before_removal - 1 == item_count_after_removal

    @pytest.mark.parametrize("user", ALLOWED_USERS_LOGIN_DATA, ids=[u["username"] for u in ALLOWED_USERS_LOGIN_DATA])
    @allure.severity(allure.severity_level.NORMAL)
    @allure.tag('cart')
    def test_cart_page_continue_shopping_button(self, user, pages):
        allure.dynamic.title(f'A Cart Page oldalon a "Continue Shopping" gomb működésének ellenőrzése '
                             f'({user["username"]} felhasználó)')
        allure.dynamic.description(f'A teszteset célja annak ellenőrzése, hogy {user["username"]} userrel belépve a'
                                   f' bevásárló kosárban a "Continue Shopping" gomb megnyomásával visszajutunk-e a '
                                   f'termékek oldalára.')
        allure.dynamic.tag(f'{user["username"]}')
        cart_page = pages["cart_page"]
        logged_in_page = pages["logged_in_page"]

        cart_page.get_button_continue_shopping().click()
        assert cart_page.get_current_url() == logged_in_page.url
        assert logged_in_page.get_number_of_items_in_cart() == len(CART_TESTDATA)

    @pytest.mark.parametrize("user", ALLOWED_USERS_LOGIN_DATA, ids=[u["username"] for u in ALLOWED_USERS_LOGIN_DATA])
    @allure.severity(allure.severity_level.NORMAL)
    @allure.tag('cart')
    def test_cart_page_checkout_button(self, user, pages):
        allure.dynamic.title(f'A Cart Page oldalon a "Checkout" gomb működésének ellenőrzése ({user["username"]}'
                             f'felhasználó)')
        allure.dynamic.description(f'A teszteset célja annak ellenőrzése, hogy {user["username"]} userrel belépve, a '
                           f'bevásárlókosárban a "Checkout" gomb megnyomásával továbbjutunk-e a checkout formra.')
        allure.dynamic.tag(f'{user["username"]}')
        cart_page = pages["cart_page"]
        checkout_step_one_page = pages["checkout_step_one_page"]

        cart_page.get_button_checkout().click()
        assert cart_page.get_current_url() == checkout_step_one_page.url
        assert checkout_step_one_page.get_page_header().text == CHECKOUT_STEP_ONE_PAGE_HEADER
