import allure
import pytest

from POM_Python.Data.cart_testdata import CART_TESTDATA, CART_PAGE_HEADER_TESTDATA
from POM_Python.Data.user_testdata import ALLOWED_USERS_LOGIN_DATA


@allure.parent_suite("SAUCE - 26 project")
@allure.suite("Cart page smoke tests")
@allure.sub_suite("Test Cycle - 002")
class TestCartPageSmoke:

    @pytest.mark.parametrize("user", ALLOWED_USERS_LOGIN_DATA, ids=[u["username"] for u in ALLOWED_USERS_LOGIN_DATA])
    @allure.severity(allure.severity_level.TRIVIAL)
    @allure.tag('cart', 'smoke')
    def test_cart_page_header_visibility(self, user, pages):
        allure.dynamic.title(f'A Cart Page oldal fejszövegének ellenőrzése ({user["username"]} felhasználó)')
        allure.dynamic.description(f'A teszteset célja annak ellenőrzése, hogy {user["username"]} userrel belépve, '
                                   f'a bevásárló kosár fejszövege megjelenik-e.')
        allure.dynamic.tag(f'{user["username"]}')
        cart_page = pages["cart_page"]

        assert cart_page.get_page_header().is_displayed()
        assert cart_page.get_page_header().text == CART_PAGE_HEADER_TESTDATA
        assert cart_page.get_current_url() == cart_page.url

    @pytest.mark.parametrize("user", ALLOWED_USERS_LOGIN_DATA, ids=[u["username"] for u in ALLOWED_USERS_LOGIN_DATA])
    @allure.severity(allure.severity_level.TRIVIAL)
    @allure.tag('cart', 'smoke')
    def test_cart_item_count_visibility(self, user, pages):
        allure.dynamic.title(
            f'A Cart Page oldalon a termék darabszámai megjelenésének ellenőrzése ({user["username"]} felhasználó)')
        allure.dynamic.description(f'A teszteset célja annak ellenőrzése, hogy a {user["username"]} userrel '
                                   f'bejelentkezve, a bevásárló kosár bal szélén megjelenik-e a termék darabszám.')
        allure.dynamic.tag(f'{user["username"]}')
        cart_page = pages["cart_page"]

        assert cart_page.get_cart_item_quantities()[0].is_displayed()
        assert cart_page.get_cart_item_quantities()[0].text == CART_TESTDATA["cart_item_1"]["quantity"]
        assert cart_page.get_cart_item_quantities()[1].is_displayed()
        assert cart_page.get_cart_item_quantities()[1].text == CART_TESTDATA["cart_item_1"]["quantity"]

    @pytest.mark.parametrize("user", ALLOWED_USERS_LOGIN_DATA, ids=[u["username"] for u in ALLOWED_USERS_LOGIN_DATA])
    @allure.severity(allure.severity_level.TRIVIAL)
    @allure.tag('cart', 'smoke')
    def test_cart_item_names_visibility(self, user, pages):
        allure.dynamic.title(f'A Cart Page oldalon a termék nevek megjelenésének ellenőrzése ({user["username"]} '
                             f'felhasználó)')
        allure.dynamic.description(f'A teszteset célja annak ellenőrzése, hogy {user["username"]} userrel bejelntkezve,'
                                   f' a bevásárló kosárban megjelennek-e a termékek nevei.')
        allure.dynamic.tag(f'{user["username"]}')
        cart_page = pages["cart_page"]

        assert cart_page.get_cart_item_names()[0].is_displayed()
        assert cart_page.get_cart_item_names()[0].text == CART_TESTDATA["cart_item_1"]["name"]
        assert cart_page.get_cart_item_names()[1].is_displayed()
        assert cart_page.get_cart_item_names()[1].text == CART_TESTDATA["cart_item_2"]["name"]

    @pytest.mark.parametrize("user", ALLOWED_USERS_LOGIN_DATA, ids=[u["username"] for u in ALLOWED_USERS_LOGIN_DATA])
    @allure.severity(allure.severity_level.TRIVIAL)
    @allure.tag('cart', 'smoke')
    def test_cart_item_description_visibility(self, user, pages):
        allure.dynamic.title(f'A Cart Page oldalon a termékek leírásai megjelenésének ellenőrzése ({user["username"]} '
                             f'felhasználó)')
        allure.dynamic.description(
            f'A teszteset célja annak ellenőrzése, hogy {user["username"]} userrel bejelntkezve, '
            f'a bevásárló kosárban megjelennek-e a termékek leírásai.')
        allure.dynamic.tag(f'{user["username"]}')
        cart_page = pages["cart_page"]

        assert cart_page.get_cart_item_descriptions()[0].is_displayed()
        assert cart_page.get_cart_item_descriptions()[0].text == CART_TESTDATA["cart_item_1"]["description"]
        assert cart_page.get_cart_item_descriptions()[1].is_displayed()
        assert cart_page.get_cart_item_descriptions()[1].text == CART_TESTDATA["cart_item_2"]["description"]

    @pytest.mark.parametrize("user", ALLOWED_USERS_LOGIN_DATA, ids=[u["username"] for u in ALLOWED_USERS_LOGIN_DATA])
    @allure.severity(allure.severity_level.TRIVIAL)
    @allure.tag('cart', 'smoke')
    def test_cart_item_price_visibility(self, user, pages):
        allure.dynamic.title(f'A Cart Page oldalon a termékek árai megjelenésének ellenőrzése ({user["username"]})')
        allure.dynamic.description(f'A teszteset célja annak ellenőrzése, hogy {user["username"]} userrel '
                                   f'bejelentkezve, a bevásárló kosárban megjelennek-e a termékek árai.')
        allure.dynamic.tag(f'{user["username"]}')
        cart_page = pages["cart_page"]

        assert cart_page.get_cart_item_prices()[0].is_displayed()
        assert cart_page.get_cart_item_prices()[0].text == CART_TESTDATA["cart_item_1"]["price"]
        assert cart_page.get_cart_item_prices()[1].is_displayed()
        assert cart_page.get_cart_item_prices()[1].text == CART_TESTDATA["cart_item_2"]["price"]

    @pytest.mark.parametrize("user", ALLOWED_USERS_LOGIN_DATA, ids=[u["username"] for u in ALLOWED_USERS_LOGIN_DATA])
    @allure.severity(allure.severity_level.TRIVIAL)
    @allure.tag('cart', 'smoke')
    def test_cart_item_remove_button__visibility(self, user, pages):
        allure.dynamic.title(
            f'A Cart Page oldalon a "Remove" gombok megjelenésének ellenőrzése ({user["username"]} felhasználó)')
        allure.dynamic.description(f'A teszteset célja annak ellenőrzése, hogy {user["username"]} userrel belépve,'
                                   f' a bevásárló kosárban megjelennek-e a termékek mellett a "Remove" gombok.')
        allure.dynamic.tag(f'{user["username"]}')
        cart_page = pages["cart_page"]

        assert cart_page.get_cart_item_remove_buttons()[0].is_displayed()
        assert cart_page.get_cart_item_remove_buttons()[0].is_enabled()
        assert cart_page.get_cart_item_remove_buttons()[1].is_displayed()
        assert cart_page.get_cart_item_remove_buttons()[1].is_enabled()

    @pytest.mark.parametrize("user", ALLOWED_USERS_LOGIN_DATA, ids=[u["username"] for u in ALLOWED_USERS_LOGIN_DATA])
    @allure.severity(allure.severity_level.TRIVIAL)
    @allure.tag('cart', 'smoke')
    def test_cart_continue_shopping_button_visibility(self, user, pages):
        allure.dynamic.title(f'A Cart Page oldalon a "Continue Shopping" gomb megjelenésének ellenőrzése '
                             f'({user["username"]} felhasználó)')
        allure.dynamic.description(f'A teszteset célja annak ellenőrzése, hogy a {user["username"]} userrel belépve, a'
                                   f' bevásárló kosár alján megjelenik-e a "Continue Shopping" gomb.')
        allure.dynamic.tag(f'{user["username"]}')
        cart_page = pages["cart_page"]

        assert cart_page.get_button_continue_shopping().is_displayed()
        assert cart_page.get_button_continue_shopping().is_enabled()

    @pytest.mark.parametrize("user", ALLOWED_USERS_LOGIN_DATA, ids=[u["username"] for u in ALLOWED_USERS_LOGIN_DATA])
    @allure.severity(allure.severity_level.TRIVIAL)
    @allure.tag('cart', 'smoke')
    def test_cart_checkout_button_visibility(self, user, pages):
        allure.dynamic.title(f'A Cart Page oldalon a "Checkout" gomb megjelenésének ellenőrzése ({user["username"]} '
                             f'felhasználó)')
        allure.dynamic.description(f'A teszteset célja annak ellenőrzése, hogy {user["username"]} userrel belépve, '
                                   f'a bevásárló kosár alján megjelenik-e a "Checkout" gomb.')
        allure.dynamic.tag(f'{user["username"]}')
        cart_page = pages["cart_page"]

        assert cart_page.get_button_checkout().is_displayed()
        assert cart_page.get_button_checkout().is_enabled()
