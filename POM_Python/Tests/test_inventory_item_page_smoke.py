import allure

from POM_Python.Data.url_testdata import INVENTORY_ITEM_PAGE_URL_TESTDATA
from POM_Python.Data.user_testdata import STANDARD_USER_LOGIN_DATA
from POM_Python.Pages.InventoryItemPage import InventoryItemPage
from POM_Python.Pages.LoggedInPage import LoggedInPage
from POM_Python.Pages.MainPage import MainPage
from POM_Python.Utils.create_driver import create_preconfigured_chrome_driver


@allure.parent_suite("UI Tests")
@allure.suite("Inventory item page smoke tests")
@allure.sub_suite("Test cases")
class TestInventoryItemPageSmoke:
    def setup_method(self):
        browser = create_preconfigured_chrome_driver()
        self.main_page = MainPage(browser)
        self.logged_in_page = LoggedInPage(browser)
        self.inventory_item_page = InventoryItemPage(browser)

    def teardown_method(self):
        pass  # self.main_page.quit()

    @allure.title('Az Inventory item page "Back to products" gombjának láthatósága')
    @allure.description('A teszteset célja, hogy ellenőrizzük hogy a "Back to products" gomb látható és '
                        'használható-e az Inventory item oldalon.')
    @allure.severity(allure.severity_level.TRIVIAL)
    @allure.tag('inventory item', 'standard_user', 'smoke')
    def test_back_to_products_button_visibility(self):
        self.main_page.do_login(STANDARD_USER_LOGIN_DATA["username"], STANDARD_USER_LOGIN_DATA["password"])
        self.logged_in_page.get_product_name_list()[0].click()
        assert INVENTORY_ITEM_PAGE_URL_TESTDATA in self.logged_in_page.get_current_url()
        assert self.inventory_item_page.get_back_to_products_button().is_displayed()
        assert self.inventory_item_page.get_back_to_products_button().is_enabled()

    @allure.title('Az Inventory item page "Add to cart" gombjának láthatósága')
    @allure.description('A teszteset célja, hogy ellenőrizzük hogy a "Add to cart" gomb látható és '
                        'használható-e az Inventory item oldalon.')
    @allure.severity(allure.severity_level.TRIVIAL)
    @allure.tag('inventory item', 'standard_user', 'smoke')
    def test_inventory_item_page_add_to_cart_button_visibility(self):
        self.main_page.do_login(STANDARD_USER_LOGIN_DATA["username"], STANDARD_USER_LOGIN_DATA["password"])
        self.logged_in_page.get_product_name_list()[0].click()
        assert INVENTORY_ITEM_PAGE_URL_TESTDATA in self.logged_in_page.get_current_url()
        assert self.inventory_item_page.get_add_to_cart_button().is_displayed()
        assert self.inventory_item_page.get_add_to_cart_button().is_enabled()

    @allure.title('Az Inventory item page-en megjelenő termék kép láthatóságának ellenőrzése')
    @allure.description('A teszteset célja, hogy ellenőrizzük hogy a termék képe megjelenik-e'
                        ' az Inventory item oldalon.')
    @allure.severity(allure.severity_level.TRIVIAL)
    @allure.tag('inventory item', 'standard_user', 'smoke')
    def test_inventory_item_page_image_visibility(self):
        self.main_page.do_login(STANDARD_USER_LOGIN_DATA["username"], STANDARD_USER_LOGIN_DATA["password"])
        self.logged_in_page.get_product_name_list()[0].click()
        assert self.inventory_item_page.get_item_image().is_displayed()

    @allure.title('Az Inventory item page-en megjelenő termék név láthatóságának ellenőrzése')
    @allure.description('A teszteset célja, hogy ellenőrizzük hogy a termék neve megjelenik-e'
                        ' az Inventory item oldalon.')
    @allure.severity(allure.severity_level.TRIVIAL)
    @allure.tag('inventory item', 'standard_user', 'smoke')
    def test_inventory_item_page_name_visibility(self):
        self.main_page.do_login(STANDARD_USER_LOGIN_DATA["username"], STANDARD_USER_LOGIN_DATA["password"])
        self.logged_in_page.get_product_name_list()[0].click()
        assert self.inventory_item_page.get_item_name().is_displayed()

    @allure.title('Az Inventory item page-en megjelenő termék leírás láthatóságának ellenőrzése')
    @allure.description('A teszteset célja, hogy ellenőrizzük hogy a termék leírása megjelenik-e'
                        ' az Inventory item oldalon.')
    @allure.severity(allure.severity_level.TRIVIAL)
    @allure.tag('inventory item', 'standard_user', 'smoke')
    def test_inventory_item_page_description_visibility(self):
        self.main_page.do_login(STANDARD_USER_LOGIN_DATA["username"], STANDARD_USER_LOGIN_DATA["password"])
        self.logged_in_page.get_product_name_list()[0].click()
        assert self.inventory_item_page.get_item_description().is_displayed()

    @allure.title('Az Inventory item page-en megjelenő termék ár láthatóságának ellenőrzése')
    @allure.description('A teszteset célja, hogy ellenőrizzük hogy a termék ára megjelenik-e'
                        ' az Inventory item oldalon.')
    @allure.severity(allure.severity_level.TRIVIAL)
    @allure.tag('inventory item', 'standard_user', 'smoke')
    def test_inventory_item_page_price_visibility(self):
        self.main_page.do_login(STANDARD_USER_LOGIN_DATA["username"], STANDARD_USER_LOGIN_DATA["password"])
        self.logged_in_page.get_product_name_list()[0].click()
        assert self.inventory_item_page.get_item_price().is_displayed()
