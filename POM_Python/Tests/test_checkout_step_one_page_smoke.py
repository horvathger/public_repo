import allure
import pytest

from POM_Python.Data.checkout_step_one_testdata import (CHECKOUT_STEP_ONE_URL, CHECKOUT_STEP_ONE_PAGE_HEADER)
from POM_Python.Data.user_testdata import ALLOWED_USERS_LOGIN_DATA
from POM_Python.Pages.CheckoutStepOnePage import CheckoutStepOnePage
from POM_Python.Utils.create_driver import create_preconfigured_chrome_driver


@pytest.fixture
def driver():
    driver = create_preconfigured_chrome_driver()
    yield driver
    driver.quit()


@pytest.fixture
def pages(driver):
    checkout_step_one_page = CheckoutStepOnePage(driver)

    return {
        "checkout_step_one_page": checkout_step_one_page
    }


@pytest.fixture
def user(request):
    return request.param


@allure.parent_suite("UI Tests")
@allure.suite("Checkout Step One page smoke tests")
@allure.sub_suite("Test cases")
class TestCheckoutStepOnePageSmoke:
    @pytest.mark.parametrize("user", ALLOWED_USERS_LOGIN_DATA, ids=[u["username"] for u in ALLOWED_USERS_LOGIN_DATA],
                             indirect=True)
    @allure.severity(allure.severity_level.TRIVIAL)
    @allure.tag('checkout_step_one', 'smoke')
    def test_checkout_step_one_page_header_visibility(self, user, pages):
        allure.dynamic.title(f'A Checkout Step One Page oldal fejszövegének ellenőrzése ({user["username"]} '
                             f'felhasználó)')
        allure.dynamic.description(f'A teszteset célja annak ellenőrzése, hogy {user["username"]} userrel '
                                   f'bejelentkezve, a Checkout Step One Page fejszövege megjelenik-e.')
        allure.dynamic.tag(f'{user["username"]}')
        checkout_step_one_page = pages["checkout_step_one_page"]

        checkout_step_one_page.goto_checkout_step_one_page(user['username'], user['password'])

        assert checkout_step_one_page.get_page_header().is_displayed()
        assert checkout_step_one_page.get_page_header().text == CHECKOUT_STEP_ONE_PAGE_HEADER
        assert checkout_step_one_page.get_current_url() == CHECKOUT_STEP_ONE_URL

    @pytest.mark.parametrize("user", ALLOWED_USERS_LOGIN_DATA, ids=[u["username"] for u in ALLOWED_USERS_LOGIN_DATA],
                             indirect=True)
    @allure.severity(allure.severity_level.TRIVIAL)
    @allure.tag('checkout_step_one', 'smoke')
    def test_checkout_step_one_page_input_firstname_visibility(self, user, pages):
        allure.dynamic.title(f'A Checkout Step One oldal firstname mezőjének ellenőrzése ({user["username"]} '
                             f'felhasználó)')
        allure.dynamic.description(f'A teszteset célja annak ellenőrzése, hogy a {user["username"]} userrel belépve, '
                                   f'a Checkout Step One Page-en megjelenik-e a firstname input mező és interaktív-e.')
        allure.dynamic.tag(f'{user["username"]}')
        checkout_step_one_page = pages["checkout_step_one_page"]

        checkout_step_one_page.goto_checkout_step_one_page(user['username'], user['password'])

        assert checkout_step_one_page.get_input_first_name().is_displayed()
        assert checkout_step_one_page.get_input_first_name().is_enabled()

    @pytest.mark.parametrize("user", ALLOWED_USERS_LOGIN_DATA, ids=[u["username"] for u in ALLOWED_USERS_LOGIN_DATA],
                             indirect=True)
    @allure.severity(allure.severity_level.TRIVIAL)
    @allure.tag('checkout_step_one', 'smoke')
    def test_checkout_step_one_page_input_lastname_visibility(self, user, pages):
        allure.dynamic.title(f'A Checkout Step One oldal lastname mezőjének ellenőrzése ({user["username"]} '
                             f'felhasználó)')
        allure.dynamic.description(f'A teszteset célja annak ellenőrzése, hogy {user["username"]} userrel belépve, '
                                   f'a Checkout Step One Page-en megjelenik-e a lastname mező és interaktív-e.')
        allure.dynamic.tag(f'{user["username"]}')
        checkout_step_one_page = pages["checkout_step_one_page"]

        checkout_step_one_page.goto_checkout_step_one_page(user['username'], user['password'])

        assert checkout_step_one_page.get_input_last_name().is_displayed()
        assert checkout_step_one_page.get_input_last_name().is_enabled()

    @pytest.mark.parametrize("user", ALLOWED_USERS_LOGIN_DATA, ids=[u["username"] for u in ALLOWED_USERS_LOGIN_DATA],
                             indirect=True)
    @allure.severity(allure.severity_level.TRIVIAL)
    @allure.tag('checkout_step_one', 'smoke')
    def test_checkout_step_one_page_input_zip_postal_code_visibility(self, user, pages):
        allure.dynamic.title(f'A Checkout Step One oldal zip/postal code mezőjének ellenőrzése ({user["username"]} '
                             f'felhasználó)')
        allure.dynamic.description(f'A teszteset célja annak ellenőrzése, hogy {user["username"]} userrel belépve, '
                                   f'a Checkout Step One Page-en megjelenik-e a zip/postal code mező és interaktív-e.')
        allure.dynamic.tag(f'{user["username"]}')
        checkout_step_one_page = pages["checkout_step_one_page"]

        checkout_step_one_page.goto_checkout_step_one_page(user['username'], user['password'])

        assert checkout_step_one_page.get_input_postal_code().is_displayed()
        assert checkout_step_one_page.get_input_postal_code().is_enabled()

    @pytest.mark.parametrize("user", ALLOWED_USERS_LOGIN_DATA, ids=[u["username"] for u in ALLOWED_USERS_LOGIN_DATA],
                             indirect=True)
    @allure.severity(allure.severity_level.TRIVIAL)
    @allure.tag('checkout_step_one', 'smoke')
    def test_checkout_step_one_page_button_cancel_visibility(self, user, pages):
        allure.dynamic.title(f'A Checkout Step One oldalon a Cancel gomb ellenőrzése ({user["username"]} ')
        allure.dynamic.description(f'A teszteset célja annak ellenőrzése, hogy {user["username"]} userrel belépve, '
                                   f'a Checkout Step One Page-en megjelenik-e a Cancel gomb és interaktív-e.')
        allure.dynamic.tag(f'{user["username"]}')
        checkout_step_one_page = pages["checkout_step_one_page"]

        checkout_step_one_page.goto_checkout_step_one_page(user['username'], user['password'])

        assert checkout_step_one_page.get_button_cancel().is_displayed()
        assert checkout_step_one_page.get_button_cancel().is_enabled()

    @pytest.mark.parametrize("user", ALLOWED_USERS_LOGIN_DATA, ids=[u["username"] for u in ALLOWED_USERS_LOGIN_DATA],
                             indirect=True)
    @allure.severity(allure.severity_level.TRIVIAL)
    @allure.tag('checkout_step_one', 'smoke')
    def test_checkout_step_one_page_button_continue_visibility(self, user, pages):
        allure.dynamic.title(f'A Checkout Step One oldalon a Continue gomb ellenőrzése ({user["username"]} '
                             f'felhasználó)')
        allure.dynamic.description(f'A teszteset célja annak ellenőrzése, hogy {user["username"]} userrel belépve, '
                                   f'a Checkout Step One Page-en megjelenik-e a Continue gomb és interaktív-e.')
        allure.dynamic.tag(f'{user["username"]}')
        checkout_step_one_page = pages["checkout_step_one_page"]

        checkout_step_one_page.goto_checkout_step_one_page(user['username'], user['password'])

        assert checkout_step_one_page.get_button_continue().is_displayed()
        assert checkout_step_one_page.get_button_continue().is_enabled()
