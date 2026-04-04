import allure
import pytest

from POM_Python.Data.checkout_step_one_testdata import CHECKOUT_STEP_ONE_INPUT_VALID_TESTDATA
from POM_Python.Data.checkout_step_two_testdata import (CHECKOUT_STEP_TWO_PAGE_ITEM_TOTAL_TESTDATA,
                                                        CHECKOUT_STEP_TWO_PAGE_TOTAL_TESTDATA)
from POM_Python.Data.url_testdata import CHECKOUT_STEP_TWO_PAGE_URL_TESTDATA, LOGGED_IN_URL_TESTDATA
from POM_Python.Data.user_testdata import STANDARD_USER_LOGIN_DATA, ALLOWED_USERS_LOGIN_DATA



@allure.parent_suite("SAUCE - 26 project")
@allure.suite("Checkout Step Two page UI tests")
@allure.sub_suite("Test Cycle - 006")
class TestCheckoutStepTwoPage:

    @pytest.mark.parametrize("user", ALLOWED_USERS_LOGIN_DATA, ids=[u["username"] for u in ALLOWED_USERS_LOGIN_DATA],
                             indirect=True)
    @allure.severity(allure.severity_level.TRIVIAL)
    @allure.tag('checkout_step_two', 'price')
    def test_checkout_step_two_page_item_price_summary(self, user, pages):
        allure.dynamic.title(f'A Checkout Step Two Page oldalon a termékek összértékének ellenőrzése '
                             f'({user["username"]} userrel).')
        allure.dynamic.description(f'A teszteset célja annak ellenőrzése, hogy a {user["username"]} userrel belépve, '
                                   f'a Checkout Step Two Page-en az egyes termékek árainak összege megegyezik-e az '
                                   f'"Item total:" mezőben szereplő összeggel.')
        allure.dynamic.tag(f'{user["username"]}')
        checkout_step_two_page = pages["checkout_step_two_page"]

        checkout_step_two_page.goto_checkout_step_two_page(STANDARD_USER_LOGIN_DATA["username"],
                                                           STANDARD_USER_LOGIN_DATA["password"],
                                                           CHECKOUT_STEP_ONE_INPUT_VALID_TESTDATA["first_name"],
                                                           CHECKOUT_STEP_ONE_INPUT_VALID_TESTDATA["last_name"],
                                                           CHECKOUT_STEP_ONE_INPUT_VALID_TESTDATA["postal_code"])

        # Az egyes termékek árának és mennyiségének lekérése a Checkout Step Two Page-en, majd az egyes termékek árának
        # és mennyiségének összeszorzása és az így kapott értékek összeadása egy változóban, végül pedig ennek a
        # változónak az értékét összehasonlítjuk az "Item total:" mezőben szereplő összeggel.

        number_of_items = len(checkout_step_two_page.get_items_list())
        items_total = None
        for index in range(number_of_items):
            item_price = checkout_step_two_page.get_item_price_list()[index].text
            item_price = float(item_price.replace("$", ""))
            item_quantity = checkout_step_two_page.get_items_quantity_list()[index].text
            item_quantity = int(item_quantity)
            item_total_price = item_price * item_quantity
            if items_total is None:
                items_total = item_total_price
            else:
                items_total += item_total_price

        assert items_total == float(CHECKOUT_STEP_TWO_PAGE_ITEM_TOTAL_TESTDATA.replace("Item total: $", ""))

        item_total_numeric = float(checkout_step_two_page.get_item_total().text.replace("Item total: $", ""))

        assert item_total_numeric == float(CHECKOUT_STEP_TWO_PAGE_ITEM_TOTAL_TESTDATA.replace
                                           ("Item total: $", ""))

    @pytest.mark.parametrize("user", ALLOWED_USERS_LOGIN_DATA, ids=[u["username"] for u in ALLOWED_USERS_LOGIN_DATA],
                             indirect=True)
    @allure.severity(allure.severity_level.TRIVIAL)
    @allure.tag('checkout_step_two', 'price')
    def test_checkout_step_two_page_items_price_plus_total_eqv_total(self, user, pages):
        allure.dynamic.title(f'Checkout Step Two Page oldalon a termékek '
                             f'összértéke + adó egyenlő-e a végösszeggel. ({user["username"]} felhasználó)')
        allure.dynamic.description(f'A teszteset célja annak ellenőrzése, hogy {user["username"]} userrel '
                                   f'belépve, a Checkout Step Two Page-en az egyes termékek árainak összegéhez ha '
                                   f'hozzá adjuk az adó összegét, akkor megkapjuk-e a számla végösszegét.')
        allure.dynamic.tag(f'{user["username"]}')
        checkout_step_two_page = pages["checkout_step_two_page"]

        checkout_step_two_page.goto_checkout_step_two_page(STANDARD_USER_LOGIN_DATA["username"],
                                                           STANDARD_USER_LOGIN_DATA["password"],
                                                           CHECKOUT_STEP_ONE_INPUT_VALID_TESTDATA["first_name"],
                                                           CHECKOUT_STEP_ONE_INPUT_VALID_TESTDATA["last_name"],
                                                           CHECKOUT_STEP_ONE_INPUT_VALID_TESTDATA["postal_code"])

        # Az "Item total:" mezőben szereplő összeg lekérése és a "$" jel eltávolítása után float típusra konvertálása
        # egy változóban, majd a "Tax:" mezőben szereplő összeg lekérése és a "$" jel eltávolítása után float típusra
        # konvertálása egy változóban, végül pedig az "Item total:" mezőben szereplő összeg és a "Tax:" mezőben
        # szereplő összeg összeadása és az így kapott érték összehasonlítása a "Total:" mezőben szereplő összeggel,
        # amelyből szintén eltávolítjuk a "$" jelet és float típusra konvertáljuk.
        item_total_numeric = float(checkout_step_two_page.get_item_total().text.replace("Item total: $", ""))
        tax_numeric = float(checkout_step_two_page.get_tax().text.replace("Tax: $", ""))
        total_numeric = float(checkout_step_two_page.get_total().text.replace("Total: $", ""))

        assert item_total_numeric + tax_numeric == total_numeric
        assert total_numeric == float(CHECKOUT_STEP_TWO_PAGE_TOTAL_TESTDATA.replace("Total: $", ""))

    @pytest.mark.parametrize("user", ALLOWED_USERS_LOGIN_DATA, ids=[u["username"] for u in ALLOWED_USERS_LOGIN_DATA],
                             indirect=True)
    @allure.severity(allure.severity_level.TRIVIAL)
    @allure.tag('checkout_step_two', 'price')
    def test_checkout_step_two_page_button_cancel_functionality(self, user, pages):
        allure.dynamic.title(f'A Checkout Step Two Page oldalon a Cancel gomb működésének ellenőrzése '
                             f'({user["username"]} felhasználó).')
        allure.dynamic.description(f'A teszteset célja annak ellenőrzése, hogy {user["username"]} userrel belépve, '
                                   f'a Checkout Step Two Page-en a Cancel gomb megnyomásával visszajutunk-e az előző'
                                   f' oldalra.')
        allure.dynamic.tag(f'{user["username"]}')
        checkout_step_two_page = pages["checkout_step_two_page"]
        logged_in_page = pages["logged_in_page"]

        checkout_step_two_page.goto_checkout_step_two_page(STANDARD_USER_LOGIN_DATA["username"],
                                                           STANDARD_USER_LOGIN_DATA["password"],
                                                           CHECKOUT_STEP_ONE_INPUT_VALID_TESTDATA["first_name"],
                                                           CHECKOUT_STEP_ONE_INPUT_VALID_TESTDATA["last_name"],
                                                           CHECKOUT_STEP_ONE_INPUT_VALID_TESTDATA["postal_code"])

        # A "Cancel" gomb megnyomása előtt eltároljuk a jelenlegi URL-t egy változóban, majd megnyomjuk a "Cancel"
        # gombot, és ezután eltároljuk a jelenlegi URL-t egy másik változóban. Végül pedig összehasonlítjuk a "Cancel"
        # gomb megnyomása előtt eltárolt URL-t a "Cancel" gomb megnyomása után eltárolt URL-lel úgy, hogy ezek ne
        # legyenek egyenlőek, és hogy a "Cancel" gomb megnyomása után eltárolt URL megegyezzen a Logged in page
        # URL-jével, míg a "Cancel" gomb megnyomása előtt eltárolt URL megegyezzen a Checkout Step Two page URL-jével.
        url_before_cancel = checkout_step_two_page.get_current_url()
        checkout_step_two_page.get_button_cancel().click()
        url_after_cancel = logged_in_page.get_current_url()

        assert url_before_cancel != url_after_cancel
        assert url_after_cancel == LOGGED_IN_URL_TESTDATA
        assert url_before_cancel == CHECKOUT_STEP_TWO_PAGE_URL_TESTDATA
