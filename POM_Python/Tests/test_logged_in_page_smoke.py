import allure
import pytest
from selenium.common import UnexpectedAlertPresentException

from POM_Python.Data.user_testdata import ALLOWED_USERS_LOGIN_DATA
from POM_Python.Pages.LoggedInPage import LoggedInPage
from POM_Python.Pages.MainPage import MainPage
from POM_Python.Utils.create_driver import create_preconfigured_chrome_driver

@pytest.fixture
def driver():
    driver = create_preconfigured_chrome_driver()
    yield driver
    driver.quit()

@pytest.fixture
def pages(driver, user):
    main_page = MainPage(driver)
    logged_in_page = LoggedInPage(driver)

    main_page.do_login(user["username"], user["password"])

    return {
        "main_page": main_page,
        "logged_in_page": logged_in_page,
    }

@allure.parent_suite("SAUCE - 26 project")
@allure.suite("Logged in page smoke tests")
@allure.sub_suite("Test Cycle - 011")
class TestLoggedInPageSmoke:

    @pytest.mark.parametrize("user", ALLOWED_USERS_LOGIN_DATA, ids=[u["username"] for u in ALLOWED_USERS_LOGIN_DATA])
    @allure.severity(allure.severity_level.TRIVIAL)
    @allure.tag('logged in')
    def test_hamburger_menu_content(self, user, pages):
        allure.dynamic.title(f'A hamburger menü megnyitásának és tartalmának ellenőrzése, '
                             f'{user["username"]} felhasználóval.')
        allure.dynamic.description(
            f'A teszteset célja, hogy {user['username']} userrel belépveellenőrizze a hamburger menü megnyitását '
            f'és a benne található elemek '
            'elérhetőségét egy standard felhasználóval történő bejelentkezés után.')
        allure.dynamic.tag(f'{user["username"]}')

        logged_in_page = pages["logged_in_page"]

        logged_in_page.get_hamburger_menu_button().click()
        logged_in_page.wait_for_hamburger_menu_to_open()
        assert logged_in_page.get_hamburger_menu_close_button().is_displayed()
        assert logged_in_page.get_hamburger_menu_close_button().is_enabled()
        assert logged_in_page.get_hamburger_menu_about().is_displayed()
        assert logged_in_page.get_hamburger_menu_about().is_enabled()
        assert logged_in_page.get_hamburger_menu_logout().is_displayed()
        assert logged_in_page.get_hamburger_menu_logout().is_enabled()

    @pytest.mark.parametrize("user", ALLOWED_USERS_LOGIN_DATA, ids=[u["username"] for u in ALLOWED_USERS_LOGIN_DATA])
    @allure.severity(allure.severity_level.TRIVIAL)
    @allure.tag('logged in')
    def test_shopping_cart(self, user, pages):
        allure.dynamic.title(f'A shopping cart ellenőrzése, {user["username"]} felhasználóval.')
        allure.dynamic.description(f'A teszteset célja, hogy {user["username"]} userrel belépve, ellenőrizze a '
                                   f'shopping cart megjelenik-e az oldalon.')
        allure.dynamic.tag(f'{user["username"]}')

        logged_in_page = pages["logged_in_page"]

        assert logged_in_page.get_shopping_cart_button().is_displayed()
        assert logged_in_page.get_shopping_cart_button().is_enabled()

    @pytest.mark.parametrize("user", ALLOWED_USERS_LOGIN_DATA, ids=[u["username"] for u in ALLOWED_USERS_LOGIN_DATA])
    @allure.severity(allure.severity_level.TRIVIAL)
    @allure.tag('logged in')
    def test_product_images_visibility(self, user, pages):
        allure.dynamic.title(f'A termékek képeinek ellenőrzése, {user["username"]} felhasználóval.')
        allure.dynamic.description(f'A teszteset célja, hogy {user['username']} userrel belépve, ellenőrizze a '
                                   f'termékek képe megjelenik-e az oldalon.')
        allure.dynamic.tag(f'{user["username"]}')

        logged_in_page = pages["logged_in_page"]

        for product_image in logged_in_page.get_product_img_list():
            assert product_image.is_displayed()

    @pytest.mark.parametrize("user", ALLOWED_USERS_LOGIN_DATA, ids=[u["username"] for u in ALLOWED_USERS_LOGIN_DATA])
    @allure.severity(allure.severity_level.TRIVIAL)
    @allure.tag('logged in')
    def test_product_descriptions_visibility(self, user, pages):
        allure.dynamic.title(f'A termékek leírásainak ellenőrzése, {user["username"]} felhasználóval.')
        allure.dynamic.description(f'A teszteset célja, hogy {user["username"]} userrel belépve ellenőrizze a termékek '
                           f'leírása megjelenik-e az oldalon.')
        allure.dynamic.tag(f'{user["username"]}')

        logged_in_page = pages["logged_in_page"]

        for product_description in logged_in_page.get_product_description_list():
            assert product_description.is_displayed()

    @pytest.mark.parametrize("user", ALLOWED_USERS_LOGIN_DATA, ids=[u["username"] for u in ALLOWED_USERS_LOGIN_DATA])
    @allure.severity(allure.severity_level.TRIVIAL)
    @allure.tag('logged in')
    def test_product_names_visibility(self, user, pages):
        allure.dynamic.title(f'A termékek neveinek ellenőrzése, {user["username"]} felhasználóval.')
        allure.dynamic.description(f'A teszteset célja, hogy {user["username"]} userrel belépve ellenőrizze a termékek neve '
                           f'megjelenik-e az oldalon.')
        allure.dynamic.tag(f'{user["username"]}')

        logged_in_page = pages["logged_in_page"]

        for product_name in logged_in_page.get_product_name_list():
            assert product_name.is_displayed()

    @pytest.mark.parametrize("user", ALLOWED_USERS_LOGIN_DATA, ids=[u["username"] for u in ALLOWED_USERS_LOGIN_DATA])
    @allure.severity(allure.severity_level.TRIVIAL)
    @allure.tag('logged in')
    def test_product_prices_visibility(self, user, pages):
        allure.dynamic.title(f'A termékek árainak ellenőrzése, {user["username"]} felhasználóval.')
        allure.dynamic.description(f'A teszteset célja, hogy {user["username"]} userrel belépve ellenőrizze a '
                                   f'termékek ára megjelenik-e az oldalon.')
        allure.dynamic.tag(f'{user["username"]}')

        logged_in_page = pages["logged_in_page"]

        for product_price in logged_in_page.get_product_price_list():
            assert product_price.is_displayed()

    @pytest.mark.parametrize("user", ALLOWED_USERS_LOGIN_DATA, ids=[u["username"] for u in ALLOWED_USERS_LOGIN_DATA])
    @allure.severity(allure.severity_level.TRIVIAL)
    @allure.tag('logged in')
    def test_product_add_to_cart_buttons_visibility(self, user, pages):
        allure.dynamic.title(f'A termékeknél található "Add To Cart" gombok ellenőrzése, {user["username"]} felhasználóval.')
        allure.dynamic.description(f'A teszteset célja, hogy {user["username"]} userrel belépve ellenőrizze a '
                                   f'termékek mellett található "Add To Cart" gomb megjelenik-e az oldalon.')
        allure.dynamic.tag(f'{user["username"]}')

        logged_in_page = pages["logged_in_page"]

        for product_add_to_cart_button in logged_in_page.get_add_to_cart_button_list():
            assert product_add_to_cart_button.is_displayed()
            assert product_add_to_cart_button.is_enabled()

    @pytest.mark.parametrize("user", ALLOWED_USERS_LOGIN_DATA, ids=[u["username"] for u in ALLOWED_USERS_LOGIN_DATA])
    @allure.severity(allure.severity_level.TRIVIAL)
    @allure.tag('logged in')
    def test_sort_items_a_z_smoke(self, user, pages):
        allure.dynamic.title(f'A termékek A-Z szerinti rendezésének ellenőrzése, {user["username"]} felhasználóval.')
        allure.dynamic.description(f'A teszteset célja, hogy {user["username"]} userrel belépve ellenőrizze a '
                                   f'termékek A-Z szerinti rendezésének működését.')
        allure.dynamic.tag(f'{user["username"]}')

        logged_in_page = pages["logged_in_page"]

        logged_in_page.select_az_sorting_options()
        list_of_names = []
        for product_name in logged_in_page.get_product_name_list():
            list_of_names.append(product_name.text)
        sorted_list_of_names = sorted(list_of_names)
        assert list_of_names == sorted_list_of_names

    @pytest.mark.parametrize("user", ALLOWED_USERS_LOGIN_DATA, ids=[u["username"] for u in ALLOWED_USERS_LOGIN_DATA])
    @allure.severity(allure.severity_level.TRIVIAL)
    @allure.tag('logged in')
    def test_sort_items_z_a_smoke(self, user, pages):
        allure.dynamic.title(f'A termékek Z-A szerinti rendezésének ellenőrzése, {user["username"]} felhasználóval.')
        allure.dynamic.description(f'A teszteset célja, hogy {user["username"]} userrel belépve ellenőrizze a '
                                   f'termékek Z-A szerinti rendezésének működését.')
        allure.dynamic.tag(f'{user["username"]}')

        logged_in_page = pages["logged_in_page"]

        try:
            logged_in_page.select_za_sorting_options()
            list_of_names = []
            for product_name in logged_in_page.get_product_name_list():
                list_of_names.append(product_name.text)
            sorted_list_of_names = sorted(list_of_names, reverse=True)
            assert list_of_names == sorted_list_of_names
        except UnexpectedAlertPresentException:
            logged_in_page.save_screenshot(f'after_sort_za_{user["username"]}.png')
            pytest.fail("Alert üzenet jelent meg a rendezés során, ami megakadályozta a teszteset végrehajtását.")
        except AssertionError:
            logged_in_page.save_screenshot(f'after_sort_za_{user["username"]}.png')
            pytest.fail("A termékek Z-A szerinti rendezése nem működik megfelelően, "
                        "a megjelenített sorrend nem helyes.")

    @pytest.mark.parametrize("user", ALLOWED_USERS_LOGIN_DATA, ids=[u["username"] for u in ALLOWED_USERS_LOGIN_DATA])
    @allure.severity(allure.severity_level.TRIVIAL)
    @allure.tag('logged in')
    def test_sort_items_by_price_low_to_high_smoke(self, user, pages):
        allure.dynamic.title(f'A termékek ár szerinti növekvő rendezésének ellenőrzése, {user["username"]} '
                             f'felhasználóval.')
        allure.dynamic.description(f'A teszteset célja, hogy {user["username"]} userrel ellenőrizze a termékek ár '
                                   f'szerinti növekvő rendezésének működését.')
        allure.dynamic.tag(f'{user["username"]}')

        logged_in_page = pages["logged_in_page"]

        try:
            logged_in_page.select_price_low_to_high_sorting_options()
            list_of_prices = []
            for product_price in logged_in_page.get_product_price_list():
                price_as_float = float(product_price.text.replace('$', ''))
                list_of_prices.append(price_as_float)
            sorted_list_of_prices = sorted(list_of_prices)
            assert list_of_prices == sorted_list_of_prices
        except UnexpectedAlertPresentException:
            logged_in_page.save_screenshot(f'after_sort_price_low_high_{user["username"]}.png')
            pytest.fail("Alert üzenet jelent meg a rendezés során, ami megakadályozta a teszteset végrehajtását.")
        except AssertionError:
            logged_in_page.save_screenshot(f'after_sort_price_low_high_{user["username"]}.png')
            pytest.fail("A termékek ár szerinti növekvő rendezése nem működik megfelelően, "
                        "a megjelenített sorrend nem helyes.")

    @pytest.mark.parametrize("user", ALLOWED_USERS_LOGIN_DATA, ids=[u["username"] for u in ALLOWED_USERS_LOGIN_DATA])
    @allure.severity(allure.severity_level.TRIVIAL)
    @allure.tag('logged in')
    def test_sort_items_by_price_high_to_low_smoke(self, user, pages):
        allure.dynamic.title(f'A termékek ár szerinti csökkenő rendezésének ellenőrzése, {user["username"]} '
                             f'felhasználóval.')
        allure.dynamic.description(f'A teszteset célja, hogy {user["username"]} userrel ellenőrizze a termékek ár '
                                   f'szerinti csökkenő rendezésének működését.')
        allure.dynamic.tag(f'{user["username"]}')

        logged_in_page = pages["logged_in_page"]

        try:
            logged_in_page.select_price_hig_to_low_sorting_options()
            list_of_prices = []
            for product_price in logged_in_page.get_product_price_list():
                price_as_float = float(product_price.text.replace('$', ''))
                list_of_prices.append(price_as_float)
            sorted_list_of_prices = sorted(list_of_prices, reverse=True)
            assert list_of_prices == sorted_list_of_prices
        except UnexpectedAlertPresentException:
            logged_in_page.save_screenshot(f'after_sort_high_low_{user["username"]}.png')
            pytest.fail("Alert üzenet jelent meg a rendezés során, ami megakadályozta a teszteset végrehajtását.")
        except AssertionError:
            logged_in_page.save_screenshot(f'after_sort_high_low_{user["username"]}.png')
            pytest.fail("A termékek ár szerinti csökkenő rendezése nem működik megfelelően, "
                        "a megjelenített sorrend nem helyes.")

    @pytest.mark.parametrize("user", ALLOWED_USERS_LOGIN_DATA, ids=[u["username"] for u in ALLOWED_USERS_LOGIN_DATA])
    @allure.severity(allure.severity_level.TRIVIAL)
    @allure.tag('logged in')
    def test_footer_twitter_icon_visibility(self, user, pages):
        allure.dynamic.title(f'A weboldal alján lévő Twitter ikon ellenőrzése, {user["username"]} felhasználóval.')
        allure.dynamic.description(f'A teszteset célja, hogy {user["username"]} userrel ellenőrizze a weboldal alján '
                                   f'található Twitter ikon megjelenését.')
        allure.dynamic.tag(f'{user["username"]}')

        logged_in_page = pages["logged_in_page"]

        assert logged_in_page.get_footer_twitter_icon().is_enabled()
        assert logged_in_page.get_footer_twitter_icon().is_displayed()

    @pytest.mark.parametrize("user", ALLOWED_USERS_LOGIN_DATA, ids=[u["username"] for u in ALLOWED_USERS_LOGIN_DATA])
    @allure.severity(allure.severity_level.TRIVIAL)
    @allure.tag('logged in', 'standard_user')
    def test_footer_facebook_icon_visibility(self, user, pages):
        allure.dynamic.title(f'A weboldal alján lévő Facebook ikon ellenőrzése, {user["username"]} felhasználóval.')
        allure.dynamic.description(f'A teszteset célja, hogy {user["username"]} userrel bejelnetkezve ellenőrizze a '
                                   f'weboldal alján található Facebook ikon megjelenését.')
        allure.dynamic.tag(f'{user["username"]}')

        logged_in_page = pages["logged_in_page"]

        assert logged_in_page.get_footer_facebook_icon().is_enabled()
        assert logged_in_page.get_footer_facebook_icon().is_displayed()

    @pytest.mark.parametrize("user", ALLOWED_USERS_LOGIN_DATA, ids=[u["username"] for u in ALLOWED_USERS_LOGIN_DATA])
    @allure.severity(allure.severity_level.TRIVIAL)
    @allure.tag('logged in', 'standard_user')
    def test_footer_linkedin_icon_visibility(self, user, pages):
        allure.dynamic.title(f'A weboldal alján lévő LinkedIn ikon ellenőrzése, {user["username"]} felhasználóval.')
        allure.dynamic.description(f'A teszteset célja, hogy {user["username"]} userrel bejelentkezve ellenőrizze a '
                                   f'weboldal alján található LinkedIn ikon megjelenését.')
        allure.dynamic.tag(f'{user["username"]}')

        logged_in_page = pages["logged_in_page"]

        assert logged_in_page.get_footer_linkedin_icon().is_enabled()
        assert logged_in_page.get_footer_linkedin_icon().is_displayed()
