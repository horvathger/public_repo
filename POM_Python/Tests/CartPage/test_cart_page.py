import allure
import pytest

from POM_Python.Data.cart_testdata import CART_TESTDATA
from POM_Python.Data.checkout_step_one_testdata import CHECKOUT_STEP_ONE_PAGE_HEADER
from POM_Python.Data.user_testdata import ALLOWED_USERS_LOGIN_DATA


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

        # A törlés előtti termékek számának eltárolása egy változóban, majd egy termék törlése a "Remove" gomb
        # megnyomásával, végül a törlés utáni termékek számának eltárolása egy változóban és összehasonlítása a
        # törlés előtti termékek számával úgy, hogy a törlés előtti termékek számából egyet levonunk, és ez egyenlő
        # legyen a törlés utáni termékek számával.
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

        # A "Continue Shopping" gomb megnyomása után ellenőrizzük, hogy a jelenlegi URL megegyezik-e a Logged in page
        # URL-jével, és hogy a kosárban lévő termékek száma megegyezik-e a CART_TESTDATA-ban szereplő termékek számával.
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

        # A "Checkout" gomb megnyomása után ellenőrizzük, hogy a jelenlegi URL megegyezik-e a Checkout Step One page
        # URL-jével, és hogy a Checkout Step One page fejlécének szövege megegyezik-e a CHECKOUT_STEP_ONE_PAGE_HEADER
        # változóban tárolt értékkel.
        cart_page.get_button_checkout().click()
        assert cart_page.get_current_url() == checkout_step_one_page.url
        assert checkout_step_one_page.get_page_header().text == CHECKOUT_STEP_ONE_PAGE_HEADER
