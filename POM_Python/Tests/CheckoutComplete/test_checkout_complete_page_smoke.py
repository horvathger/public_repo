import allure
import pytest
from selenium.common import TimeoutException

from POM_Python.Data.checkout_complete_testdata import (CHECKOUT_COMPLETE_PAGE_HEADER_TESTDATA,
                                                        CHECKOUT_COMPLETE_PAGE_COMPLETE_MESSAGE_BODY_TESTDATA,
                                                        CHECKOUT_COMPLETE_PAGE_COMPLETE_MESSAGE_HEADER_TESTDATA)
from POM_Python.Data.checkout_step_one_testdata import CHECKOUT_STEP_ONE_INPUT_VALID_TESTDATA
from POM_Python.Data.url_testdata import CHECKOUT_COMPLETE_PAGE_URL_TESTDATA, LOGGED_IN_URL_TESTDATA
from POM_Python.Data.user_testdata import ALLOWED_USERS_LOGIN_DATA


@allure.parent_suite("SAUCE - 26 project")
@allure.suite("Checkout Complete page smoke tests")
@allure.sub_suite("Test Cycle - 003")
class TestCheckoutCompletePageSmoke:

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

        # A teszteset előfeltétele, hogy a Checkout Complete oldal elérhető legyen a megadott userrel, ezért amennyiben
        # a navigáció során TimeoutException keletkezik, úgy a teszteset meghiúsultnak tekintendő, és a teszt
        # sikertelen lesz.
        try:
            checkout_complete_page.goto_checkout_complete_page(
                user["username"],
                user["password"],
                CHECKOUT_STEP_ONE_INPUT_VALID_TESTDATA["first_name"],
                CHECKOUT_STEP_ONE_INPUT_VALID_TESTDATA["last_name"],
                CHECKOUT_STEP_ONE_INPUT_VALID_TESTDATA["postal_code"])
        except TimeoutException:
            pytest.fail(f'Az aktuális userrel a Checkout Complete oldal nem érhető el. ({user["username"]})')

        # A Checkout Complete oldal URL-jének ellenőrzése is megtörténik, így amennyiben az URL nem egyezik a várt
        # értékkel, úgy a teszteset szintén meghiúsultnak tekintendő, és a teszt sikertelen lesz, továbbá a hiba
        # okának megállapítását segítendő a teszt futtatása során egy screenshot is készül az aktuális állapotról.
        try:
            assert checkout_complete_page.get_current_url() == CHECKOUT_COMPLETE_PAGE_URL_TESTDATA
        except AssertionError:
            checkout_complete_page.save_screenshot(f'PH_ch_comp_page_url_check_{user["username"]}')
            pytest.fail(f'Az aktuális weboldal URL-je nem egyezik a Checkout Complete Page URL-jével.'
                        f' ({user["username"]})')

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

        # A teszteset előfeltétele, hogy a Checkout Complete oldal elérhető legyen a megadott userrel, ezért amennyiben
        # a navigáció során TimeoutException keletkezik, úgy a teszteset meghiúsultnak tekintendő, és a teszt
        # sikertelen lesz.
        try:
            checkout_complete_page.goto_checkout_complete_page(
                user["username"],
                user["password"],
                CHECKOUT_STEP_ONE_INPUT_VALID_TESTDATA["first_name"],
                CHECKOUT_STEP_ONE_INPUT_VALID_TESTDATA["last_name"],
                CHECKOUT_STEP_ONE_INPUT_VALID_TESTDATA["postal_code"])
        except TimeoutException:
            pytest.fail(f'Az aktuális userrel a Checkout Complete oldal nem érhető el. ({user["username"]})')

        try:
            assert checkout_complete_page.get_current_url() == CHECKOUT_COMPLETE_PAGE_URL_TESTDATA
        except AssertionError:
            checkout_complete_page.save_screenshot(f'MH_ch_comp_url_fail_{user["username"]}')
            pytest.fail(f'Az oldal URL-je nem egyezik meg a Checkout Complete oldal URL-jével. ({user["username"]})')

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

        try:
            checkout_complete_page.goto_checkout_complete_page(
                user["username"],
                user["password"],
                CHECKOUT_STEP_ONE_INPUT_VALID_TESTDATA["first_name"],
                CHECKOUT_STEP_ONE_INPUT_VALID_TESTDATA["last_name"],
                CHECKOUT_STEP_ONE_INPUT_VALID_TESTDATA["postal_code"])
        except TimeoutException:
            pytest.fail(f'Az aktuális userrel a Checkout Complete oldal nem érhető el. ({user["username"]})')

        # A Checkout Complete oldal URL-jének ellenőrzése is megtörténik, így amennyiben az URL nem egyezik a várt
        # értékkel, úgy a teszteset szintén meghiúsultnak tekintendő, és a teszt sikertelen lesz, továbbá a hiba
        # okának megállapítását segítendő a teszt futtatása során egy screenshot is készül az aktuális állapotról.
        try:
            assert checkout_complete_page.get_current_url() == CHECKOUT_COMPLETE_PAGE_URL_TESTDATA
        except AssertionError:
            checkout_complete_page.save_screenshot(f'MB_ch_comp_url_fail_{user["username"]}')
            pytest.fail(f'Az oldal URL-je nem egyezik meg a Checkout Complete oldal URL-jével. ({user["username"]})')

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

        try:
            checkout_complete_page.goto_checkout_complete_page(
                user["username"],
                user["password"],
                CHECKOUT_STEP_ONE_INPUT_VALID_TESTDATA["first_name"],
                CHECKOUT_STEP_ONE_INPUT_VALID_TESTDATA["last_name"],
                CHECKOUT_STEP_ONE_INPUT_VALID_TESTDATA["postal_code"])
        except TimeoutException:
            pytest.fail(f'Az aktuális userrel a Checkout Complete oldal nem érhető el. ({user["username"]})')

        try:
            assert checkout_complete_page.get_current_url() == CHECKOUT_COMPLETE_PAGE_URL_TESTDATA
        except AssertionError:
            checkout_complete_page.save_screenshot(f'BH_vis_ch_comp_url_fail_{user["username"]}')
            pytest.fail(f'Az oldal URL-je nem egyezik meg a Checkout Complete oldal URL-jével. ({user["username"]})')

        # A "Back Home" gomb megjelenésének és interaktivitásának ellenőrzése is megtörténik, így amennyiben a gomb
        # nem jelenik meg, vagy nem interaktív, úgy a teszteset meghiúsultnak tekintendő, és a teszt sikertelen lesz.
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

        try:
            checkout_complete_page.goto_checkout_complete_page(
                user["username"],
                user["password"],
                CHECKOUT_STEP_ONE_INPUT_VALID_TESTDATA["first_name"],
                CHECKOUT_STEP_ONE_INPUT_VALID_TESTDATA["last_name"],
                CHECKOUT_STEP_ONE_INPUT_VALID_TESTDATA["postal_code"])
        except TimeoutException:
            pytest.fail(f'Az aktuális userrel a Checkout Complete oldal nem érhető el. ({user["username"]})')

        try:
            assert checkout_complete_page.get_current_url() == CHECKOUT_COMPLETE_PAGE_URL_TESTDATA
        except AssertionError:
            checkout_complete_page.save_screenshot(f'BH_funk_ch_comp_url_fail_{user["username"]}')
            pytest.fail(f'Az oldal URL-je nem egyezik meg a Checkout Complete oldal URL-jével. ({user["username"]})')

        # A "Back Home" gomb megnyomása után a visszajutás ellenőrzése is megtörténik, így amennyiben a visszajutás
        # nem sikerül, úgy a teszteset meghiúsultnak tekintendő, és a teszt sikertelen lesz, továbbá a hiba okának
        # megállapítását segítendő a teszt futtatása során egy screenshot is készül az aktuális állapotról.
        url_before_click = checkout_complete_page.get_current_url()
        checkout_complete_page.get_back_home_button().click()
        url_after_click = logged_in_page.get_current_url()
        assert url_before_click != url_after_click
        assert url_before_click == CHECKOUT_COMPLETE_PAGE_URL_TESTDATA
        assert url_after_click == LOGGED_IN_URL_TESTDATA
