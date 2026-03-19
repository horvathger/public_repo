import allure

from POM_Python.Data.cart_testdata import CART_TESTDATA
from POM_Python.Data.user_testdata import STANDARD_USER_LOGIN_DATA
from POM_Python.Pages.CartPage import CartPage
from POM_Python.Pages.CheckoutStepOnePage import CheckoutStepOnePage
from POM_Python.Pages.LoggedInPage import LoggedInPage
from POM_Python.Utils.create_driver import create_preconfigured_chrome_driver


@allure.parent_suite("UI Tests")
@allure.suite("Cart page UI tests")
@allure.sub_suite("Test cases")
class TestCartPage:
    def setup_method(self):
        browser = create_preconfigured_chrome_driver()
        self.cart_page = CartPage(browser)
        self.logged_in_page = LoggedInPage(browser)
        self.checkout_step_one_page = CheckoutStepOnePage(browser)

    def teardown_method(self):
        self.cart_page.quit()

    @allure.title('A Cart Page oldalon a termék törlése funkció ellenőrzése')
    @allure.description('A teszteset célja annak ellenőrzése, hogy a bevásárló kosárban a termékek melletti "Remove" '
                        'gombbal törölhetők-e a termékek.')
    @allure.severity(allure.severity_level.NORMAL)
    @allure.tag('cart', 'standard_user')
    def test_cart_page_remove_item_button(self):
        self.cart_page.goto_cart_page_with_two_items(STANDARD_USER_LOGIN_DATA["username"],
                                                     STANDARD_USER_LOGIN_DATA["password"])
        item_count_before_removal = len(self.cart_page.get_cart_items())
        self.cart_page.get_cart_item_remove_buttons()[0].click()
        item_count_after_removal = len(self.cart_page.get_cart_items())
        assert item_count_before_removal - 1 == item_count_after_removal

    @allure.title('A Cart Page oldalon a "Continue Shopping" gomb működésének ellenőrzése')
    @allure.description(
        'A teszteset célja annak ellenőrzése, hogy a bevásárló kosárban a "Continue Shopping" gomb megnyomásával '
        'visszajutunk-e a termékek oldalára.')
    @allure.severity(allure.severity_level.NORMAL)
    @allure.tag('cart', 'standard_user')
    def test_cart_page_continue_shopping_button(self):
        self.cart_page.goto_cart_page_with_two_items(STANDARD_USER_LOGIN_DATA["username"],
                                                     STANDARD_USER_LOGIN_DATA["password"])
        self.cart_page.get_button_continue_shopping().click()
        assert self.cart_page.get_current_url() == self.logged_in_page.url
        assert self.logged_in_page.get_number_of_items_in_cart() == len(CART_TESTDATA)

    @allure.title('A Cart Page oldalon a "Checkout" gomb működésének ellenőrzése')
    @allure.description(
        'A teszteset célja annak ellenőrzése, hogy a bevásárló kosárban a "Checkout" gomb megnyomásával továbbjutunk-e '
        'a checkout formra.')
    @allure.severity(allure.severity_level.NORMAL)
    @allure.tag('cart', 'standard_user')
    def test_cart_page_checkout_button(self):
        self.cart_page.goto_cart_page_with_two_items(STANDARD_USER_LOGIN_DATA["username"],
                                                     STANDARD_USER_LOGIN_DATA["password"])
        self.cart_page.get_button_checkout().click()
        assert self.cart_page.get_current_url() == self.checkout_step_one_page.url
        assert self.checkout_step_one_page.get_page_header().text == 'Checkout: Your Information'
