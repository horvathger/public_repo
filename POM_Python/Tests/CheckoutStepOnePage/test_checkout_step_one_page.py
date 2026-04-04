import allure
import pytest

from POM_Python.Data.checkout_step_one_testdata import (CHECKOUT_STEP_ONE_INPUT_VALID_TESTDATA,
                                                        CHECKOUT_STEP_ONE_ERROR_MESSAGE_EMPTY_FIRSTNAME,
                                                        CHECKOUT_STEP_ONE_ERROR_MESSAGE_EMPTY_LASTNAME,
                                                        CHECKOUT_STEP_ONE_ERROR_MESSAGE_EMPTY_POSTALCODE)
from POM_Python.Data.url_testdata import CHECKOUT_STEP_TWO_PAGE_URL_TESTDATA
from POM_Python.Data.user_testdata import ALLOWED_USERS_LOGIN_DATA


@allure.parent_suite("SAUCE - 26 project")
@allure.suite("Check Out Step One UI tests")
@allure.sub_suite("Test Cycle - 004")
class TestCheckoutStepOnePage:

    @pytest.mark.parametrize("user", ALLOWED_USERS_LOGIN_DATA, ids=[u["username"] for u in ALLOWED_USERS_LOGIN_DATA],
                             indirect=True)
    @allure.severity(allure.severity_level.TRIVIAL)
    @allure.tag('checkout_step_one', 'positive')
    def test_checkout_step_one_page_positive(self, user, pages):
        allure.dynamic.title(f'A Checkout Step One Page form kitöltése pozitív ágon ({user["username"]} felhasználó)')
        allure.dynamic.description(f'A teszteset célja annak ellenőrzése, hogy {user["username"]} userrel belépve, '
                                   f'a Checkout Step One Page form kitöltésével tovább lehet-e lépni a Checkout '
                                   f'Step Two Page-re.')
        allure.dynamic.tag(f'{user["username"]}')
        checkout_step_one_page = pages["checkout_step_one_page"]

        checkout_step_one_page.goto_checkout_step_one_page(user['username'], user['password'])

        checkout_step_one_page.get_input_first_name().send_keys(CHECKOUT_STEP_ONE_INPUT_VALID_TESTDATA['first_name'])
        checkout_step_one_page.get_input_last_name().send_keys(CHECKOUT_STEP_ONE_INPUT_VALID_TESTDATA['last_name'])
        checkout_step_one_page.get_input_postal_code().send_keys(CHECKOUT_STEP_ONE_INPUT_VALID_TESTDATA['postal_code'])
        checkout_step_one_page.get_button_continue().click()

        # A "Continue" gomb megnyomása után ellenőrizzük, hogy a jelenlegi URL megegyezik-e
        # a Checkout Step Two page URL-jével.
        try:
            assert checkout_step_one_page.get_current_url() == CHECKOUT_STEP_TWO_PAGE_URL_TESTDATA
        except AssertionError:
            checkout_step_one_page.save_screenshot(f'step_one_positive_{user["username"]}')
            pytest.fail(f'A pozitív ágon kitöltött step one form után a Continuera kattintva nem lép tovább '
                        f'a step two page-re. ({user["username"]})')

    @pytest.mark.parametrize("user", ALLOWED_USERS_LOGIN_DATA, ids=[u["username"] for u in ALLOWED_USERS_LOGIN_DATA],
                             indirect=True)
    @allure.severity(allure.severity_level.TRIVIAL)
    @allure.tag('checkout_step_one', 'negatív')
    def test_checkout_step_one_page_empty_firstname(self, user, pages):
        allure.dynamic.title(f'A Checkout Step One Page form firstname nélküli kitöltése és továbblépés kísérlete '
                             f'({user["username"]} felhasználó)')
        allure.dynamic.description(f'A teszteset célja annak ellenőrzése, hogy {user["username"]} userrel belépve, '
                                   f'a Checkout Step One Page form kitöltése során a firstname mező üresen hagyását '
                                   f'követően tovább lehet-e lépni a Checkout Step Two Page-re.')
        allure.dynamic.tag(f'{user["username"]}')
        checkout_step_one_page = pages["checkout_step_one_page"]

        checkout_step_one_page.goto_checkout_step_one_page(user['username'], user['password'])

        checkout_step_one_page.get_input_last_name().send_keys(
            CHECKOUT_STEP_ONE_INPUT_VALID_TESTDATA['last_name'])
        checkout_step_one_page.get_input_postal_code().send_keys(
            CHECKOUT_STEP_ONE_INPUT_VALID_TESTDATA['postal_code'])
        checkout_step_one_page.get_button_continue().click()

        # A "Continue" gomb megnyomása után ellenőrizzük, hogy a felbukkanó hibaüzenet megegyezik-e a megfelelő
        # hibaüzenettel.
        try:
            assert checkout_step_one_page.get_error_message().text == CHECKOUT_STEP_ONE_ERROR_MESSAGE_EMPTY_FIRSTNAME
        except AssertionError:
            checkout_step_one_page.save_screenshot(f'step_one_without_firstname_{user["username"]}')
            pytest.fail(f'A firstname üresen hagyásával a Continuera kattintva nem megfelelő hibaüzenet jelenik meg. '
                        f'({user["username"]})')

    @pytest.mark.parametrize("user", ALLOWED_USERS_LOGIN_DATA, ids=[u["username"] for u in ALLOWED_USERS_LOGIN_DATA],
                             indirect=True)
    @allure.severity(allure.severity_level.TRIVIAL)
    @allure.tag('checkout_step_one', 'negatív')
    def test_checkout_step_one_page_empty_lastname(self, user, pages):
        allure.dynamic.title(f'A Checkout Step One Page form lastname nélküli kitöltése és továbblépés kísérlete '
                             f'({user["username"]} felhasználó)')
        allure.dynamic.description(f'A teszteset célja annak ellenőrzése, hogy {user["username"]} userrel belépve, '
                                   f'a Checkout Step One Page form kitöltése során a lastname mező üresen hagyását '
                                   f'követően tovább lehet-e lépni a Checkout Step Two Page-re.')
        allure.dynamic.tag(f'{user["username"]}')
        checkout_step_one_page = pages["checkout_step_one_page"]

        checkout_step_one_page.goto_checkout_step_one_page(user['username'], user['password'])

        checkout_step_one_page.get_input_first_name().send_keys(
            CHECKOUT_STEP_ONE_INPUT_VALID_TESTDATA['first_name'])
        checkout_step_one_page.get_input_postal_code().send_keys(
            CHECKOUT_STEP_ONE_INPUT_VALID_TESTDATA['postal_code'])
        checkout_step_one_page.get_button_continue().click()

        # A "Continue" gomb megnyomása után ellenőrizzük, hogy a jelenlegi URL nem egyezik-e meg a
        # Checkout Step Two page URL-jével, és hogy a felbukkanó hibaüzenet megegyezik-e a megfelelő hibaüzenettel.
        try:
            assert checkout_step_one_page.get_current_url() != CHECKOUT_STEP_TWO_PAGE_URL_TESTDATA
        except AssertionError:
            checkout_step_one_page.save_screenshot(f'step_one_form_validation_fail_{user["username"]}')
            pytest.fail(f'A lastname üresen hagyásával a Continue-ra kattintva továbblép a következő oldalra, a '
                        f'form validációja nélkül. ({user["username"]})')

        assert checkout_step_one_page.get_error_message().text == CHECKOUT_STEP_ONE_ERROR_MESSAGE_EMPTY_LASTNAME


    @pytest.mark.parametrize("user", ALLOWED_USERS_LOGIN_DATA, ids=[u["username"] for u in ALLOWED_USERS_LOGIN_DATA],
                             indirect=True)
    @allure.severity(allure.severity_level.TRIVIAL)
    @allure.tag('checkout_step_one', 'negatív')
    def test_checkout_step_one_page_empty_postal_code(self, user, pages):
        allure.dynamic.title(f'A Checkout Step One Page form postal code nélküli kitöltése és továbblépés kísérlete '
                             f'({user["username"]} felhasználó)')
        allure.dynamic.description(f'A teszteset célja annak ellenőrzése, hogy {user["username"]} userrel a Checkout '
                                   f'Step One Page form kitöltése során a postal code mező üresen hagyását követően '
                                   f'tovább lehet-e lépni a Checkout Step Two Page-re.')
        allure.dynamic.tag(f'{user["username"]}')
        checkout_step_one_page = pages["checkout_step_one_page"]

        checkout_step_one_page.goto_checkout_step_one_page(user['username'], user['password'])

        checkout_step_one_page.get_input_first_name().send_keys(
            CHECKOUT_STEP_ONE_INPUT_VALID_TESTDATA['first_name'])
        checkout_step_one_page.get_input_last_name().send_keys(
            CHECKOUT_STEP_ONE_INPUT_VALID_TESTDATA['last_name'])
        checkout_step_one_page.get_button_continue().click()

        # A "Continue" gomb megnyomása után ellenőrizzük, hogy a felbukkanó hibaüzenet megegyezik-e a megfelelő
        # hibaüzenettel.
        try:
            assert checkout_step_one_page.get_error_message().text == CHECKOUT_STEP_ONE_ERROR_MESSAGE_EMPTY_POSTALCODE
        except AssertionError:
            (checkout_step_one_page.save_screenshot
             (f'step_one_form_empty_postalcode_errormessage_{user["username"]}'))
            pytest.fail(f'A postalcode üresen hagyásával a Continue-ra kattintva nem a megfelelő hibaüzenet jelenik '
                        f'meg. ({user["username"]})')
