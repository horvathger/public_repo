import allure
import pytest

from POM_Python.Data.url_testdata import INVENTORY_ITEM_PAGE_URL_TESTDATA
from POM_Python.Data.user_testdata import ALLOWED_USERS_LOGIN_DATA


@allure.parent_suite("SAUCE - 26 project")
@allure.suite("Inventory item page smoke tests")
@allure.sub_suite("Test Cycle - 009")
class TestInventoryItemPageSmoke:
    @pytest.mark.parametrize("user", ALLOWED_USERS_LOGIN_DATA, ids=[u["username"] for u in ALLOWED_USERS_LOGIN_DATA])
    @allure.severity(allure.severity_level.TRIVIAL)
    @allure.tag('inventory item', 'smoke')
    def test_back_to_products_button_visibility(self, user, pages):
        allure.dynamic.title(
            f'Az Inventory item page "Back to products" gombjának láthatósága. ({user["username"]} felhasználó)')
        allure.dynamic.description(
            f'A teszteset célja, hogy {user["username"]} userrel ellenőrizzük hogy a "Back to products" gomb '
            f'látható és használható-e az Inventory item oldalon.')
        allure.dynamic.tag(f'{user["username"]}')
        logged_in_page = pages["logged_in_page"]
        inventory_item_page = pages["inventory_item_page"]

        logged_in_page.get_product_name_list()[0].click()

        assert INVENTORY_ITEM_PAGE_URL_TESTDATA in logged_in_page.get_current_url()
        assert inventory_item_page.get_back_to_products_button().is_displayed()
        assert inventory_item_page.get_back_to_products_button().is_enabled()

    @pytest.mark.parametrize("user", ALLOWED_USERS_LOGIN_DATA, ids=[u["username"] for u in ALLOWED_USERS_LOGIN_DATA])
    @allure.severity(allure.severity_level.TRIVIAL)
    @allure.tag('inventory item', 'smoke')
    def test_inventory_item_page_add_to_cart_button_visibility(self, user, pages):
        allure.dynamic.title(
            f'Az Inventory item page "Add to cart" gombjának láthatósága ({user["username"]} felhasználó)')
        allure.dynamic.description(
            f'A teszteset célja, hogy {user["username"]} userrel ellenőrizzük hogy a "Add to cart" gomb látható és '
            'használható-e az Inventory item oldalon.')
        allure.dynamic.tag(f'{user["username"]}')
        logged_in_page = pages["logged_in_page"]
        inventory_item_page = pages["inventory_item_page"]

        logged_in_page.get_product_name_list()[0].click()

        assert INVENTORY_ITEM_PAGE_URL_TESTDATA in logged_in_page.get_current_url()
        assert inventory_item_page.get_add_to_cart_button().is_displayed()
        assert inventory_item_page.get_add_to_cart_button().is_enabled()

    @pytest.mark.parametrize("user", ALLOWED_USERS_LOGIN_DATA, ids=[u["username"] for u in ALLOWED_USERS_LOGIN_DATA])
    @allure.severity(allure.severity_level.TRIVIAL)
    @allure.tag('inventory item', 'smoke')
    def test_inventory_item_page_image_visibility(self, user, pages):
        allure.dynamic.title(
            f'Az Inventory item page-en megjelenő termék kép láthatóságának ellenőrzése ({user["username"]} '
            f'felhasználó)')
        allure.dynamic.description(
            f'A teszteset célja, hogy {user["username"]} userrel ellenőrizzük hogy a termék képe megjelenik-e'
            ' az Inventory item oldalon.')
        allure.dynamic.tag(f'{user["username"]}')
        inventory_item_page = pages["inventory_item_page"]
        logged_in_page = pages["logged_in_page"]

        logged_in_page.get_product_name_list()[0].click()

        assert inventory_item_page.get_item_image().is_displayed()

    @pytest.mark.parametrize("user", ALLOWED_USERS_LOGIN_DATA, ids=[u["username"] for u in ALLOWED_USERS_LOGIN_DATA])
    @allure.severity(allure.severity_level.TRIVIAL)
    @allure.tag('inventory item', 'smoke')
    def test_inventory_item_page_name_visibility(self, user, pages):
        allure.dynamic.title(
            f'Az Inventory item page-en megjelenő termék név láthatóságának ellenőrzése ({user["username"]} '
            f'felhasználó)')
        allure.dynamic.description(
            f'A teszteset célja, hogy {user["username"]} userrel ellenőrizzük hogy a termék neve megjelenik-e'
            ' az Inventory item oldalon.')
        allure.dynamic.tag(f'{user["username"]}')
        inventory_item_page = pages["inventory_item_page"]
        logged_in_page = pages["logged_in_page"]

        logged_in_page.get_product_name_list()[0].click()

        assert inventory_item_page.get_item_name().is_displayed()

    @pytest.mark.parametrize("user", ALLOWED_USERS_LOGIN_DATA, ids=[u["username"] for u in ALLOWED_USERS_LOGIN_DATA])
    @allure.severity(allure.severity_level.TRIVIAL)
    @allure.tag('inventory item', 'smoke')
    def test_inventory_item_page_description_visibility(self, user, pages):
        allure.dynamic.title(
            f'Az Inventory item page-en megjelenő termék leírás láthatóságának ellenőrzése ({user["username"]} '
            f'felhasználó)')
        allure.dynamic.description(
            f'A teszteset célja, hogy {user["username"]} userrel ellenőrizzük hogy a termék leírása megjelenik-e'
            ' az Inventory item oldalon.')
        allure.dynamic.tag(f'{user["username"]}')
        inventory_item_page = pages["inventory_item_page"]

        logged_in_page = pages["logged_in_page"]

        logged_in_page.get_product_name_list()[0].click()

        assert inventory_item_page.get_item_description().is_displayed()

    @pytest.mark.parametrize("user", ALLOWED_USERS_LOGIN_DATA, ids=[u["username"] for u in ALLOWED_USERS_LOGIN_DATA])
    @allure.severity(allure.severity_level.TRIVIAL)
    @allure.tag('inventory item', 'smoke')
    def test_inventory_item_page_price_visibility(self, user, pages):
        allure.dynamic.title(
            f'Az Inventory item page-en megjelenő termék ár láthatóságának ellenőrzése ({user["username"]} '
            f'felhasználó)')
        allure.dynamic.description(
            f'A teszteset célja, hogy {user["username"]} userrel ellenőrizzük hogy a termék ára megjelenik-e'
            ' az Inventory item oldalon.')
        allure.dynamic.tag(f'{user["username"]}')
        inventory_item_page = pages["inventory_item_page"]
        logged_in_page = pages["logged_in_page"]

        logged_in_page.get_product_name_list()[0].click()

        assert inventory_item_page.get_item_price().is_displayed()
