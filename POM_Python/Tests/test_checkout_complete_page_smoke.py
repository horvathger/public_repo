import allure
import pytest

from POM_Python.Data.checkout_complete_testdata import (CHECKOUT_COMPLETE_PAGE_HEADER_TESTDATA,
                                                        CHECKOUT_COMPLETE_PAGE_COMPLETE_MESSAGE_BODY_TESTDATA,
                                                        CHECKOUT_COMPLETE_PAGE_COMPLETE_MESSAGE_HEADER_TESTDATA)
from POM_Python.Data.checkout_step_one_testdata import CHECKOUT_STEP_ONE_INPUT_VALID_TESTDATA
from POM_Python.Data.url_testdata import CHECKOUT_COMPLETE_PAGE_URL_TESTDATA, LOGGED_IN_URL_TESTDATA
from POM_Python.Data.user_testdata import ALLOWED_USERS_LOGIN_DATA
from POM_Python.Pages.CheckoutCompletePage import CheckoutCompletePage
from POM_Python.Pages.CheckoutStepOnePage import CheckoutStepOnePage
from POM_Python.Pages.CheckoutStepTwoPage import CheckoutStepTwoPage
from POM_Python.Pages.LoggedInPage import LoggedInPage
from POM_Python.Pages.MainPage import MainPage
from POM_Python.Utils.create_driver import create_preconfigured_chrome_driver


@pytest.fixture
def driver():
    driver = create_preconfigured_chrome_driver()
    yield driver
    driver.quit()


@pytest.fixture
def pages(driver):
    checkout_step_one_page = CheckoutStepOnePage(driver)
    checkout_step_two_page = CheckoutStepTwoPage(driver)
    logged_in_page = LoggedInPage(driver)
    checkout_complete_page = CheckoutCompletePage(driver)
    main_page = MainPage(driver)

    return {
        "logged_in_page": logged_in_page,
        "checkout_complete_page": checkout_complete_page,
        "main_page": main_page,
        "checkout_step_one_page": checkout_step_one_page,
        "checkout_step_two_page": checkout_step_two_page

    }


@pytest.fixture
def user(request):
    return request.param


@allure.parent_suite("UI Tests")
@allure.suite("Checkout Step Two page smoke tests")
@allure.sub_suite("Test cases")
class TestCheckoutStepTwoPageSmoke:

    @pytest.mark.parametrize("user", ALLOWED_USERS_LOGIN_DATA, ids=[u["username"] for u in ALLOWED_USERS_LOGIN_DATA],
                             indirect=True)
    @allure.severity(allure.severity_level.TRIVIAL)
    @allure.tag('checkout_complete', 'smoke')
    def test_checkout_complete_page_header_visibility(self, user, pages):
        allure.dynamic.title(f'A Checkout Complete oldal fejszövegének ellenőrzése ({user["username"]} felhasználó)')
        allure.dynamic.description(f'A teszteset célja annak ellenőrzése, hogy {user["username"]} userrel belépve, '
                                   f'a Checkout Complete Page fejszövege megjelenik-e.')
        allure.dynamic.tag(f'{user["username"]}')
        checkout_complete_page = pages["checkout_complete_page"]

        checkout_complete_page.goto_checkout_complete_page(
            user["username"],
            user["password"],
            CHECKOUT_STEP_ONE_INPUT_VALID_TESTDATA["first_name"],
            CHECKOUT_STEP_ONE_INPUT_VALID_TESTDATA["last_name"],
            CHECKOUT_STEP_ONE_INPUT_VALID_TESTDATA["postal_code"])

        assert checkout_complete_page.get_page_header().is_displayed()
        assert checkout_complete_page.get_page_header().text == CHECKOUT_COMPLETE_PAGE_HEADER_TESTDATA

    @pytest.mark.parametrize("user", ALLOWED_USERS_LOGIN_DATA, ids=[u["username"] for u in ALLOWED_USERS_LOGIN_DATA],
                             indirect=True)
    @allure.severity(allure.severity_level.TRIVIAL)
    @allure.tag('checkout_complete', 'smoke')
    def test_checkout_complete_message_header_visibility(self, user, pages):
        allure.dynamic.title(f'A Checkout Complete oldalon az üzenet fejszövegének ellenőrzése ({user["username"]} '
                             f'felhasználó)')
        allure.dynamic.description(f'A teszteset célja annak ellenőrzése, hogy {user["username"]} userrel belépve, '
                                   f'a Checkout Complete Page oldalon az üzenet fejszövege megjelenik-e.')
        allure.dynamic.tag(f'{user["username"]}')
        checkout_complete_page = pages["checkout_complete_page"]


        checkout_complete_page.goto_checkout_complete_page(
            user["username"],
            user["password"],
            CHECKOUT_STEP_ONE_INPUT_VALID_TESTDATA["first_name"],
            CHECKOUT_STEP_ONE_INPUT_VALID_TESTDATA["last_name"],
            CHECKOUT_STEP_ONE_INPUT_VALID_TESTDATA["postal_code"])

        assert checkout_complete_page.get_message_header().is_displayed()
        assert (checkout_complete_page.get_message_header().text ==
                CHECKOUT_COMPLETE_PAGE_COMPLETE_MESSAGE_HEADER_TESTDATA)

    @pytest.mark.parametrize("user", ALLOWED_USERS_LOGIN_DATA, ids=[u["username"] for u in ALLOWED_USERS_LOGIN_DATA],
                             indirect=True)
    @allure.severity(allure.severity_level.TRIVIAL)
    @allure.tag('checkout_complete', 'smoke')
    def test_checkout_complete_message_body_visibility(self, user, pages):
        allure.dynamic.title(f'A Checkout Complete oldalon az üzenet tartalmának ellenőrzése ({user["username"]} '
                             f'felhasználó)')
        allure.dynamic.description(f'A teszteset célja annak ellenőrzése, hogy {user["username"]} userrel belépve, '
                                   f'a Checkout Complete Page oldalon az üzenet tartalma megjelenik-e.')
        allure.dynamic.tag(f'{user["username"]}')
        checkout_complete_page = pages["checkout_complete_page"]

        checkout_complete_page.goto_checkout_complete_page(
            user["username"],
            user["password"],
            CHECKOUT_STEP_ONE_INPUT_VALID_TESTDATA["first_name"],
            CHECKOUT_STEP_ONE_INPUT_VALID_TESTDATA["last_name"],
            CHECKOUT_STEP_ONE_INPUT_VALID_TESTDATA["postal_code"])

        assert checkout_complete_page.get_message_text().is_displayed()
        assert (checkout_complete_page.get_message_text().text ==
                CHECKOUT_COMPLETE_PAGE_COMPLETE_MESSAGE_BODY_TESTDATA)

    @pytest.mark.parametrize("user", ALLOWED_USERS_LOGIN_DATA, ids=[u["username"] for u in ALLOWED_USERS_LOGIN_DATA],
                             indirect=True)
    @allure.severity(allure.severity_level.TRIVIAL)
    @allure.tag('checkout_complete', 'smoke')
    def test_checkout_complete_button_back_home_visibility(self, user, pages):
        allure.dynamic.title(f'A Checkout Complete oldalon a "Back Home" gomb ellenőrzése ({user["username"]} '
                             f'felhasználó)')
        allure.dynamic.description(f'A teszteset célja annak ellenőrzése, hogy {user["username"]} userrel belépve, '
                                   f'a Checkout Complete Page oldalon a "Back Home" gomb megjelenik-e és interaktív-e.')
        allure.dynamic.tag(f'{user["username"]}')
        checkout_complete_page = pages["checkout_complete_page"]

        checkout_complete_page.goto_checkout_complete_page(
            user["username"],
            user["password"],
            CHECKOUT_STEP_ONE_INPUT_VALID_TESTDATA["first_name"],
            CHECKOUT_STEP_ONE_INPUT_VALID_TESTDATA["last_name"],
            CHECKOUT_STEP_ONE_INPUT_VALID_TESTDATA["postal_code"])

        assert checkout_complete_page.get_back_home_button().is_displayed()
        assert checkout_complete_page.get_back_home_button().is_enabled()

    @pytest.mark.parametrize("user", ALLOWED_USERS_LOGIN_DATA, ids=[u["username"] for u in ALLOWED_USERS_LOGIN_DATA],
                             indirect=True)
    @allure.severity(allure.severity_level.TRIVIAL)
    @allure.tag('checkout_complete', 'smoke')
    def test_checkout_complete_button_back_home_functionality(self, user, pages):
        allure.dynamic.title(f'A Checkout Complete oldalon a "Back Home" gomb működésének az ellenőrzése '
                             f'({user["username"]} felhasználó)')
        allure.dynamic.description(f'A teszteset célja annak ellenőrzése, hogy {user["username"]} userrel belépve, '
                                   f'a Checkout Complete Page oldalon a "Back Home" gomb megnyomásával '
                                   f'visszajutunk-e a főoldalra.')
        allure.dynamic.tag(f'{user["username"]}')
        checkout_complete_page = pages["checkout_complete_page"]

        logged_in_page = pages["logged_in_page"]


        checkout_complete_page.goto_checkout_complete_page(
            user["username"],
            user["password"],
            CHECKOUT_STEP_ONE_INPUT_VALID_TESTDATA["first_name"],
            CHECKOUT_STEP_ONE_INPUT_VALID_TESTDATA["last_name"],
            CHECKOUT_STEP_ONE_INPUT_VALID_TESTDATA["postal_code"])

        url_before_click = checkout_complete_page.get_current_url()
        checkout_complete_page.get_back_home_button().click()
        url_after_click = logged_in_page.get_current_url()
        assert url_before_click != url_after_click
        assert url_before_click == CHECKOUT_COMPLETE_PAGE_URL_TESTDATA
        assert url_after_click == LOGGED_IN_URL_TESTDATA
