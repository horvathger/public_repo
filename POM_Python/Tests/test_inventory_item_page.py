import allure

from POM_Python.Data.user_testdata import STANDARD_USER_LOGIN_DATA
from POM_Python.Pages.InventoryItemPage import InventoryItemPage
from POM_Python.Pages.LoggedInPage import LoggedInPage
from POM_Python.Pages.MainPage import MainPage
from POM_Python.Utils.create_driver import create_preconfigured_chrome_driver


@allure.parent_suite("UI Tests")
@allure.suite("Inventory item page tests")
@allure.sub_suite("Test cases")
class TestInventoryItemPage:
    def setup_method(self):
        browser = create_preconfigured_chrome_driver()
        self.main_page = MainPage(browser)
        self.logged_in_page = LoggedInPage(browser)
        self.inventory_item_page = InventoryItemPage(browser)

    def teardown_method(self):
        self.main_page.quit()

    @allure.title('Az Inventory item page-en és a Logged in page-en a termékek neveinek összehasonlítása')
    @allure.description('A teszteset célja, hogy ellenőrizzük hogy a főoldalon és a Logged in pagen a termékek nevei '
                        'megegyeznek-e.')
    @allure.severity(allure.severity_level.TRIVIAL)
    @allure.tag('inventory item', 'standard_user', 'item name')
    def test_inventory_item_page_and_logged_in_page_product_name_comparison(self):
        self.main_page.do_login(STANDARD_USER_LOGIN_DATA["username"], STANDARD_USER_LOGIN_DATA["password"])
        for item in range(len(self.logged_in_page.get_product_name_list())):
            item_name_main_page = self.logged_in_page.get_product_name_list()[item].text
            self.logged_in_page.get_product_name_list()[item].click()
            item_name_inventory_item_page = self.inventory_item_page.get_item_name().text
            assert item_name_main_page == item_name_inventory_item_page
            self.inventory_item_page.get_back_to_products_button().click()

    @allure.title('Az Inventory item page-en és a Logged in page-en a termékek képeinek összehasonlítása')
    @allure.description('A teszteset célja, hogy ellenőrizzük hogy a főoldalon és a Logged in pagen a termékek képei '
                        'megegyeznek-e.')
    @allure.severity(allure.severity_level.TRIVIAL)
    @allure.tag('inventory item', 'standard_user', 'item image')
    def test_inventory_item_page_and_logged_in_page_product_image_comparison(self):
        self.main_page.do_login(STANDARD_USER_LOGIN_DATA["username"], STANDARD_USER_LOGIN_DATA["password"])
        for item in range(len(self.logged_in_page.get_product_img_list())):
            item_image_main_page = self.logged_in_page.get_product_img_list()[item].text
            self.logged_in_page.get_product_img_list()[item].click()
            item_image_inventory_item_page = self.inventory_item_page.get_item_image().text
            assert item_image_main_page == item_image_inventory_item_page
            self.inventory_item_page.get_back_to_products_button().click()

    @allure.title('Az Inventory item page-en és a Logged in page-en a termékek leírásainak összehasonlítása')
    @allure.description('A teszteset célja, hogy ellenőrizzük hogy a főoldalon és a Logged in pagen a termékek '
                        'leírásai megegyeznek-e.')
    @allure.severity(allure.severity_level.TRIVIAL)
    @allure.tag('inventory item', 'standard_user', 'item description')
    def test_inventory_item_page_and_logged_in_page_product_description_comparison(self):
        self.main_page.do_login(STANDARD_USER_LOGIN_DATA["username"], STANDARD_USER_LOGIN_DATA["password"])
        for item in range(len(self.logged_in_page.get_product_description_list())):
            item_description_main_page = self.logged_in_page.get_product_description_list()[item].text
            self.logged_in_page.get_product_img_list()[item].click()
            item_description_inventory_item_page = self.inventory_item_page.get_item_description().text
            assert item_description_main_page == item_description_inventory_item_page
            self.inventory_item_page.get_back_to_products_button().click()

    @allure.title('Az Inventory item page-en és a Logged in page-en a termékek árainak összehasonlítása')
    @allure.description('A teszteset célja, hogy ellenőrizzük hogy a főoldalon és a Logged in pagen a termékek '
                        'árai megegyeznek-e.')
    @allure.severity(allure.severity_level.TRIVIAL)
    @allure.tag('inventory item', 'standard_user', 'item price')
    def test_inventory_item_page_and_logged_in_page_product_price_comparison(self):
        self.main_page.do_login(STANDARD_USER_LOGIN_DATA["username"], STANDARD_USER_LOGIN_DATA["password"])
        for item in range(len(self.logged_in_page.get_product_price_list())):
            item_price_main_page = self.logged_in_page.get_product_price_list()[item].text
            self.logged_in_page.get_product_img_list()[item].click()
            item_price_inventory_item_page = self.inventory_item_page.get_item_price().text
            assert item_price_main_page == item_price_inventory_item_page
            self.inventory_item_page.get_back_to_products_button().click()
