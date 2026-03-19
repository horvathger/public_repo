import allure

from POM_Python.Data.cart_testdata import CART_TESTDATA, CART_PAGE_HEADER_TESTDATA
from POM_Python.Data.user_testdata import STANDARD_USER_LOGIN_DATA
from POM_Python.Pages.CartPage import CartPage
from POM_Python.Utils.create_driver import create_preconfigured_chrome_driver


@allure.parent_suite("UI Tests")
@allure.suite("Cart page smoke tests")
@allure.sub_suite("Test cases")
class TestCartPageSmoke:
    def setup_method(self):
        browser = create_preconfigured_chrome_driver()
        self.cart_page = CartPage(browser)

    def teardown_method(self):
        self.cart_page.quit()

    @allure.title('A Cart Page oldal fejszövegének ellenőrzése')
    @allure.description('A teszteset célja annak ellenőrzése, hogy a bevásárló kosár fejszövege megjelenik-e.')
    @allure.severity(allure.severity_level.TRIVIAL)
    @allure.tag('cart', 'smoke', 'standard_user')
    def test_cart_page_header_visibility(self):
        self.cart_page.goto_cart_page_with_two_items(STANDARD_USER_LOGIN_DATA["username"],
                                                     STANDARD_USER_LOGIN_DATA["password"])
        assert self.cart_page.get_page_header().is_displayed()
        assert self.cart_page.get_page_header().text == CART_PAGE_HEADER_TESTDATA
        assert self.cart_page.get_current_url() == self.cart_page.url

    @allure.title('A Cart Page oldalon a termék darabszámai megjelenésének ellenőrzése')
    @allure.description('A teszteset célja annak ellenőrzése, hogy a bevásárló kosár bal szélén megjelenik-e a '
                        'termék darabszám.')
    @allure.severity(allure.severity_level.TRIVIAL)
    @allure.tag('cart', 'smoke', 'standard_user')
    def test_cart_item_count_visibility(self):
        self.cart_page.goto_cart_page_with_two_items(STANDARD_USER_LOGIN_DATA["username"],
                                                     STANDARD_USER_LOGIN_DATA["password"])
        assert self.cart_page.get_cart_item_quantities()[0].is_displayed()
        assert self.cart_page.get_cart_item_quantities()[0].text == CART_TESTDATA["cart_item_1"]["quantity"]
        assert self.cart_page.get_cart_item_quantities()[1].is_displayed()
        assert self.cart_page.get_cart_item_quantities()[1].text == CART_TESTDATA["cart_item_1"]["quantity"]

    @allure.title('A Cart Page oldalon a termék nevek megjelenésének ellenőrzése')
    @allure.description('A teszteset célja annak ellenőrzése, hogy a bevásárló kosárban megjelennek-e '
                        'a termékek nevei.')
    @allure.severity(allure.severity_level.TRIVIAL)
    @allure.tag('cart', 'smoke', 'standard_user')
    def test_cart_item_names_visibility(self):
        self.cart_page.goto_cart_page_with_two_items(STANDARD_USER_LOGIN_DATA["username"],
                                                     STANDARD_USER_LOGIN_DATA["password"])
        assert self.cart_page.get_cart_item_names()[0].is_displayed()
        assert self.cart_page.get_cart_item_names()[0].text == CART_TESTDATA["cart_item_1"]["name"]
        assert self.cart_page.get_cart_item_names()[1].is_displayed()
        assert self.cart_page.get_cart_item_names()[1].text == CART_TESTDATA["cart_item_2"]["name"]

    @allure.title('A Cart Page oldalon a termékek leírásai megjelenésének ellenőrzése')
    @allure.description('A teszteset célja annak ellenőrzése, hogy a bevásárló kosárban megjelennek-e '
                        'a termékek leírásai.')
    @allure.severity(allure.severity_level.TRIVIAL)
    @allure.tag('cart', 'smoke', 'standard_user')
    def test_cart_item_description_visibility(self):
        self.cart_page.goto_cart_page_with_two_items(STANDARD_USER_LOGIN_DATA["username"],
                                                     STANDARD_USER_LOGIN_DATA["password"])
        assert self.cart_page.get_cart_item_descriptions()[0].is_displayed()
        assert self.cart_page.get_cart_item_descriptions()[0].text == CART_TESTDATA["cart_item_1"]["description"]
        assert self.cart_page.get_cart_item_descriptions()[1].is_displayed()
        assert self.cart_page.get_cart_item_descriptions()[1].text == CART_TESTDATA["cart_item_2"]["description"]

    @allure.title('A Cart Page oldalon a termékek árai megjelenésének ellenőrzése')
    @allure.description('A teszteset célja annak ellenőrzése, hogy a bevásárló kosárban megjelennek-e '
                        'a termékek árai.')
    @allure.severity(allure.severity_level.TRIVIAL)
    @allure.tag('cart', 'smoke', 'standard_user')
    def test_cart_item_price_visibility(self):
        self.cart_page.goto_cart_page_with_two_items(STANDARD_USER_LOGIN_DATA["username"],
                                                     STANDARD_USER_LOGIN_DATA["password"])
        assert self.cart_page.get_cart_item_prices()[0].is_displayed()
        assert self.cart_page.get_cart_item_prices()[0].text == CART_TESTDATA["cart_item_1"]["price"]
        assert self.cart_page.get_cart_item_prices()[1].is_displayed()
        assert self.cart_page.get_cart_item_prices()[1].text == CART_TESTDATA["cart_item_2"]["price"]

    @allure.title('A Cart Page oldalon a "Remove" gombok megjelenésének ellenőrzése')
    @allure.description('A teszteset célja annak ellenőrzése, hogy a bevásárló kosárban megjelennek-e '
                        'a termékek mellett a "Remove" gombok.')
    @allure.severity(allure.severity_level.TRIVIAL)
    @allure.tag('cart', 'smoke', 'standard_user')
    def test_cart_item_remove_button__visibility(self):
        self.cart_page.goto_cart_page_with_two_items(STANDARD_USER_LOGIN_DATA["username"],
                                                     STANDARD_USER_LOGIN_DATA["password"])
        assert self.cart_page.get_cart_item_remove_buttons()[0].is_displayed()
        assert self.cart_page.get_cart_item_remove_buttons()[0].is_enabled()
        assert self.cart_page.get_cart_item_remove_buttons()[1].is_displayed()
        assert self.cart_page.get_cart_item_remove_buttons()[1].is_enabled()

    @allure.title('A Cart Page oldalon a "Continue Shopping" gomb megjelenésének ellenőrzése')
    @allure.description('A teszteset célja annak ellenőrzése, hogy a bevásárló kosár alján megjelenik-e '
                        'a "Continue Shopping" gomb.')
    @allure.severity(allure.severity_level.TRIVIAL)
    @allure.tag('cart', 'smoke', 'standard_user')
    def test_cart_continue_shopping_button_visibility(self):
        self.cart_page.goto_cart_page_with_two_items(STANDARD_USER_LOGIN_DATA["username"],
                                                     STANDARD_USER_LOGIN_DATA["password"])
        assert self.cart_page.get_button_continue_shopping().is_displayed()
        assert self.cart_page.get_button_continue_shopping().is_enabled()

    @allure.title('A Cart Page oldalon a "Checkout" gomb megjelenésének ellenőrzése')
    @allure.description('A teszteset célja annak ellenőrzése, hogy a bevásárló kosár alján megjelenik-e '
                        'a "Checkout" gomb.')
    @allure.severity(allure.severity_level.TRIVIAL)
    @allure.tag('cart', 'smoke', 'standard_user')
    def test_cart_checkout_button_visibility(self):
        self.cart_page.goto_cart_page_with_two_items(STANDARD_USER_LOGIN_DATA["username"],
                                                     STANDARD_USER_LOGIN_DATA["password"])
        assert self.cart_page.get_button_checkout().is_displayed()
        assert self.cart_page.get_button_checkout().is_enabled()
