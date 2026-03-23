import allure
import pytest

from POM_Python.Data.social_media_testdata import TWITTER_TESTDATA, FACEBOOK_TESTDATA, LINKEDIN_TESTDATA
from POM_Python.Data.url_testdata import LOGGED_IN_URL_TESTDATA, MAIN_PAGE_URL_TESTDATA, ABOUT_URL_TESTDATA
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


@allure.parent_suite("UI Tests")
@allure.suite("Logged in page tests")
@allure.sub_suite("Test cases")
class TestLoggedInPageSmoke:

    @pytest.mark.parametrize("user", ALLOWED_USERS_LOGIN_DATA, ids=[u["username"] for u in ALLOWED_USERS_LOGIN_DATA])
    @allure.severity(allure.severity_level.TRIVIAL)
    @allure.tag('logged in', 'about', 'fail', 'BT-SAUCE-2026-1', 'SAUCE-US-1')
    def test_hamburger_menu_about_open(self, user, pages):
        allure.dynamic.title(f'A hamburger menüből az About oldal megnyitásának az ellenőrzése. ({user["username"]} '
                             f'felhasználó)')
        allure.dynamic.description(
            f'A teszteset célja, hogy {user["username"]} userrel ellenőrizzük a hamburger menüben található About '
            f'menüpont működik-e, új ablakban (tabon) megnyitja-e a saucelabs.com weboldalt.')
        allure.dynamic.tag(f'{user["username"]}')
        logged_in_page = pages["logged_in_page"]

        number_of_window_handles_before = logged_in_page.get_number_of_window_handles()
        logged_in_page.get_hamburger_menu_button().click()
        logged_in_page.wait_for_hamburger_menu_to_open()
        logged_in_page.get_hamburger_menu_about().click()
        number_of_window_handles_after = logged_in_page.get_number_of_window_handles()
        try:
            assert logged_in_page.get_current_url() == ABOUT_URL_TESTDATA
        except AssertionError:
            logged_in_page.save_screenshot(f'after_click_about_bad_url{user["username"]}.png')
            pytest.fail(f'Az Aboutra kattintva nem a saucelabs.com oldal nyílt meg, '
                        f'hanem a {logged_in_page.get_current_url()} url.')
        # Mivel a saucelabs.com nem új ablakban (tabon) nyílik meg, ezért a teszteset elbukik.
        # Üzleti érdek, hogy a webshop ablaka mindenképpen nyitva maradjon és a saucelabs.com egy új ablakban (tabon)
        # nyíljon meg, ezért a teszteset elbukása elfogadható. Amennyiben a saucelabs.com új ablakban (tabon)
        # nyílik meg, akkor a teszteset sikeres lesz.
        try:
            assert number_of_window_handles_before != number_of_window_handles_after
        except AssertionError:
            logged_in_page.save_screenshot(f'after_click_about_new_tab{user["username"]}.png')
            pytest.fail('A saucelabs.com oldal nem új ablakban (tabon) nyílt meg, '
                        'hanem ugyanabban az ablakban (tabon).')

    @pytest.mark.parametrize("user", ALLOWED_USERS_LOGIN_DATA, ids=[u["username"] for u in ALLOWED_USERS_LOGIN_DATA])
    @allure.severity(allure.severity_level.TRIVIAL)
    @allure.tag('logged in', 'logout')
    def test_hamburger_menu_logout_button(self, user, pages):
        allure.dynamic.title(f'A hamburger menüből a logout gomb ellenőrzése ({user["username"]}.')
        allure.dynamic.description(f'A teszteset célja, hogy ellenőrizzük {user["username"]} userrel, hogy a '
                                   f'hamburger menüben található Logout menüpont működik-e, valóban kilép-e a '
                                   f'bejelentkezett felhasználó, és visszavisz-e a főoldalra (login oldalra).')
        allure.dynamic.tag(f'{user["username"]}')
        main_page = pages["main_page"]
        logged_in_page = pages["logged_in_page"]

        assert logged_in_page.get_current_url() == LOGGED_IN_URL_TESTDATA
        logged_in_page.get_hamburger_menu_button().click()
        logged_in_page.wait_for_hamburger_menu_to_open()
        logged_in_page.get_hamburger_menu_logout().click()
        main_page.wait_for_page_to_load()
        assert main_page.get_current_url() == MAIN_PAGE_URL_TESTDATA

    # Ellenorizzuk, hogy a fooldal aljan talalhato kozossegi media ikonok a megfelelo platform ceges oldalara
    # mutatnak-e, es rakattintva uj tabon jelennek-e meg.
    @pytest.mark.parametrize("user", ALLOWED_USERS_LOGIN_DATA, ids=[u["username"] for u in ALLOWED_USERS_LOGIN_DATA])
    @allure.severity(allure.severity_level.NORMAL)
    @allure.tag('pozitív', 'X', 'Twitter', 'közösségi média', 'link')
    def test_x_twitter_icon(self, user, pages):
        allure.dynamic.title(f'A X - Twitter ikon tesztelése ({user["username"]} felhasználó)')
        allure.dynamic.description(f'A teszteset célja annak ellenőrzése, hogy {user["username"]} userrel belépve a '
                                   f'főoldal alján megjelenő közösségi média ikonok közül az X (Twitter) ikonra '
                                   f'kattintva, új ablakban jelenik-e meg a cég oldala.')
        allure.dynamic.tag(f'{user["username"]}')
        logged_in_page = pages["logged_in_page"]

        # - a social media ikonok teszteleset kiszerveztem egy fuggvenybe, mely parametere az elvart URL,
        # valamint a lap aljan levo sm ikonok xpath-a.
        # visszateresi erteke true, ha uj tab-on nyilik meg a sm oldal es az uj tab url-je megegyezik az elvart url-el
        assert logged_in_page.social_media_icon_check(TWITTER_TESTDATA['url'], TWITTER_TESTDATA['xpath_locator'])

    @pytest.mark.parametrize("user", ALLOWED_USERS_LOGIN_DATA, ids=[u["username"] for u in ALLOWED_USERS_LOGIN_DATA])
    @allure.severity(allure.severity_level.NORMAL)
    @allure.tag('pozitív', 'Facebook', 'közösségi média', 'link')
    def test_facebook_icon(self, user, pages):
        allure.dynamic.title(f'A Facebook ikon tesztelése ({user["username"]} felhasználó)')
        allure.dynamic.description(f'A teszteset célja annak ellenőrzése, hogy {user["username"]} userrel belépve a '
                                   f'főoldal alján megjelenő közösségi média ikonok közül a Facebook ikonra kattintva, '
                                   f'új ablakban jelenik-e meg a cég oldala.')
        allure.dynamic.tag(f'{user["username"]}')
        logged_in_page = pages["logged_in_page"]

        # - a social media ikonok teszteleset kiszerveztem egy fuggvenybe, mely parametere az elvart URL,
        # valamint a lap aljan levo sm ikonok xpath-a.
        # visszateresi erteke true, ha uj tab-on nyilik meg a sm oldal es az uj tab url-je megegyezik az elvart url-el
        assert logged_in_page.social_media_icon_check(FACEBOOK_TESTDATA['url'], FACEBOOK_TESTDATA['xpath_locator'])

    @pytest.mark.parametrize("user", ALLOWED_USERS_LOGIN_DATA, ids=[u["username"] for u in ALLOWED_USERS_LOGIN_DATA])
    @allure.severity(allure.severity_level.NORMAL)
    @allure.tag('pozitív', 'LinkedIn', 'közösségi média', 'link')
    def test_linkedin_icon(self, user, pages):
        allure.dynamic.title(f'A LinkedIn ikon tesztelése ({user["username"]} felhasználó)')
        allure.dynamic.description(f'A teszteset célja annak ellenőrzése, hogy {user["username"]} userrel belépve, '
                                   f'a főoldal alján megjelenő közösségi média ikonok közül a LinkedIn ikonra '
                                   f'kattintva, új ablakban jelenik-e meg a cég oldala.')
        allure.dynamic.tag(f'{user["username"]}')
        logged_in_page = pages["logged_in_page"]

        # - a social media ikonok teszteleset kiszerveztem egy fuggvenybe, mely parametere az elvart URL, valamint
        # a lap aljan levo sm ikonok xpath-a.
        # visszateresi erteke true, ha uj tab-on nyilik meg a sm oldal es az uj tab url-je megegyezik az elvart url-el
        assert logged_in_page.social_media_icon_check(LINKEDIN_TESTDATA['url'], LINKEDIN_TESTDATA['xpath_locator'])
