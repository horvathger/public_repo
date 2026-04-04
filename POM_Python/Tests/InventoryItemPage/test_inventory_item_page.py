import allure
import pytest

from POM_Python.Data.user_testdata import ALLOWED_USERS_LOGIN_DATA


@allure.parent_suite("SAUCE - 26 project")
@allure.suite("Inventory item page tests")
@allure.sub_suite("Test Cycle - 008")
class TestInventoryItemPage:
    @pytest.mark.parametrize("user", ALLOWED_USERS_LOGIN_DATA, ids=[u["username"] for u in ALLOWED_USERS_LOGIN_DATA])
    @allure.severity(allure.severity_level.TRIVIAL)
    @allure.tag('inventory item', 'item name', 'fail', 'BT-SAUCE-2026-2', 'SAUCE-US-2')
    def test_inventory_item_page_and_logged_in_page_product_name_comparison(self, user, pages):
        allure.dynamic.title(f'Az Inventory item page-en és a Logged in page-en a termékek neveinek összehasonlítása '
                             f'({user["username"]} felhasználó)')
        allure.dynamic.description(f'A teszteset célja, hogy {user["username"]} userrel ellenőrizzük hogy a főoldalon '
                                   f'és a Logged in pagen a termékek nevei megegyeznek-e.')
        allure.dynamic.tag(f'{user["username"]}')

        logged_in_page = pages["logged_in_page"]
        inventory_item_page = pages["inventory_item_page"]

        # A termékek nevének eltárolása egy listában a Logged in page-en
        product_names = [el.text for el in logged_in_page.get_product_name_list()]

        # A termékek nevének összehasonlítása a Logged in page-en és az Inventory item page-en úgy, hogy minden egyes
        # termékre rákattintunk és megvizsgáljuk a nevét az Inventory item page-en
        for name in product_names:
            products = logged_in_page.get_product_name_list()

            for product in products:
                if product.text == name:
                    product.click()
                    break

            item_name_inventory_item_page = inventory_item_page.get_item_name().text
            try:
                assert name == item_name_inventory_item_page
            except AssertionError:
                pytest.fail(f'A termék neve az Inventory item page-en nem egyezik meg a Logged in page-en '
                            f'szereplő névvel. ({user["username"]} felhasználó esetén)')

            inventory_item_page.get_back_to_products_button().click()

    @pytest.mark.parametrize("user", ALLOWED_USERS_LOGIN_DATA, ids=[u["username"] for u in ALLOWED_USERS_LOGIN_DATA])
    @allure.severity(allure.severity_level.TRIVIAL)
    @allure.tag('inventory item', 'item image', 'fail', 'BT-SAUCE-2026-2', 'SAUCE-US-2')
    def test_inventory_item_page_and_logged_in_page_product_image_comparison(self, user, pages):
        allure.dynamic.title(f'Az Inventory item page-en és a Logged in page-en a termékek képeinek összehasonlítása '
                             f'({user["username"]} felhasználó)')
        allure.dynamic.description(f'A teszteset célja, hogy {user["username"]} userrel ellenőrizzük hogy a főoldalon '
                                   f'és a Logged in pagen a termékek képei megegyeznek-e.')
        allure.dynamic.tag(f'{user["username"]}')
        logged_in_page = pages["logged_in_page"]
        inventory_item_page = pages["inventory_item_page"]

        # A termékek képeinek összehasonlítása a Logged in page-en és az Inventory item page-en úgy, hogy minden egyes
        # termékre rákattintunk és megvizsgáljuk a képét az Inventory item page-en
        for item in range(len(logged_in_page.get_product_img_list())):
            item_image_main_page = logged_in_page.get_product_img_list()[item].get_attribute("src")
            logged_in_page.get_product_img_list()[item].click()
            item_image_inventory_item_page = inventory_item_page.get_item_image().get_attribute("src")
            try:
                assert item_image_main_page == item_image_inventory_item_page
            except AssertionError:
                pytest.fail(f'Az Inventory Item Page-en és a Logged In Page-en a termék képe nem egyezik meg. '
                            f'({user["username"]} felhasználó)')
            inventory_item_page.get_back_to_products_button().click()

    @pytest.mark.parametrize("user", ALLOWED_USERS_LOGIN_DATA, ids=[u["username"] for u in ALLOWED_USERS_LOGIN_DATA])
    @allure.severity(allure.severity_level.TRIVIAL)
    @allure.tag('inventory item', 'item description', 'fail', 'BT-SAUCE-2026-2', 'SAUCE-US-2')
    def test_inventory_item_page_and_logged_in_page_product_description_comparison(self, user, pages):
        allure.dynamic.title(f'Az Inventory item page-en és a Logged in page-en a termékek leírásainak '
                             f'összehasonlítása ({user["username"]} felhasználó)')
        allure.dynamic.description(f'A teszteset célja, hogy {user["username"]} userrel ellenőrizzük hogy a '
                                   f'főoldalon és a Logged in pagen a termékek leírásai megegyeznek-e.')
        allure.dynamic.tag(f'{user["username"]}')
        logged_in_page = pages["logged_in_page"]
        inventory_item_page = pages["inventory_item_page"]

        # A termékek leírásainak összehasonlítása a Logged in page-en és az Inventory item page-en úgy, hogy minden egyes
        # termékre rákattintunk és megvizsgáljuk a leírását az Inventory item page-en
        for item in range(len(logged_in_page.get_product_description_list())):
            item_description_main_page = logged_in_page.get_product_description_list()[item].text
            logged_in_page.get_product_img_list()[item].click()
            item_description_inventory_item_page = inventory_item_page.get_item_description().text
            try:
                assert item_description_main_page == item_description_inventory_item_page
            except AssertionError:
                pytest.fail(f'A termék leírása az Inventory item page-en nem egyezik meg a Logged in page-en '
                            f'szereplő leírással. ({user["username"]} felhasználó esetén)')
            inventory_item_page.get_back_to_products_button().click()

    @pytest.mark.parametrize("user", ALLOWED_USERS_LOGIN_DATA, ids=[u["username"] for u in ALLOWED_USERS_LOGIN_DATA])
    @allure.severity(allure.severity_level.TRIVIAL)
    @allure.tag('inventory item', 'item price', 'fail', 'BT-SAUCE-2026-2', 'SAUCE-US-2')
    def test_inventory_item_page_and_logged_in_page_product_price_comparison(self, user, pages):
        allure.dynamic.title(f'Az Inventory item page-en és a Logged in page-en a termékek árainak összehasonlítása '
                             f'({user["username"]} felhasználó)')
        allure.dynamic.description(f'A teszteset célja, hogy ellenőrizzük, hogy {user["username"]} userrel a '
                                   f'főoldalon és a Logged in pagen a termékek árai megegyeznek-e.')
        allure.dynamic.tag(f'{user["username"]}')
        logged_in_page = pages["logged_in_page"]
        inventory_item_page = pages["inventory_item_page"]

        # A termékek árainak összehasonlítása a Logged in page-en és az Inventory item page-en úgy, hogy minden egyes
        # termékre rákattintunk és megvizsgáljuk az árát az Inventory item page-en
        for item in range(len(logged_in_page.get_product_price_list())):
            item_price_main_page = logged_in_page.get_product_price_list()[item].text
            logged_in_page.get_product_img_list()[item].click()
            item_price_inventory_item_page = inventory_item_page.get_item_price().text
            try:
                assert item_price_main_page == item_price_inventory_item_page
            except AssertionError:
                pytest.fail(f'A termék ára az Inventory item page-en nem egyezik meg a Logged in page-en '
                            f'szereplő árral. ({user["username"]} felhasználó esetén)')
            inventory_item_page.get_back_to_products_button().click()
