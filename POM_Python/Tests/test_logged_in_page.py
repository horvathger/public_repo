import allure
import pytest

from POM_Python.Data.social_media_testdata import TWITTER_TESTDATA, FACEBOOK_TESTDATA, LINKEDIN_TESTDATA
from POM_Python.Data.url_testdata import LOGGED_IN_URL_TESTDATA, MAIN_PAGE_URL_TESTDATA, ABOUT_URL_TESTDATA
from POM_Python.Data.user_testdata import STANDARD_USER_LOGIN_DATA, ALLOWED_USERS_LOGIN_DATA
from POM_Python.Pages.LoggedInPage import LoggedInPage
from POM_Python.Pages.MainPage import MainPage
from POM_Python.Utils.create_driver import create_preconfigured_chrome_driver


@allure.parent_suite("UI Tests")
@allure.suite("Logged in page tests")
@allure.sub_suite("Test cases")
class TestLoggedInPageSmoke:
    def setup_method(self):
        browser = create_preconfigured_chrome_driver()
        self.main_page = MainPage(browser)
        self.logged_in_page = LoggedInPage(browser)

    def teardown_method(self):
        self.main_page.quit()

    @pytest.mark.parametrize("user", ALLOWED_USERS_LOGIN_DATA, ids=[u["username"] for u in ALLOWED_USERS_LOGIN_DATA])
    @allure.title('A hamburger menüből az About oldal megnyitásának az ellenőrzése.')
    @allure.description('A teszteset célja, hogy ellenőrizzük a hamburger menüben található About menüpont működik-e,'
                        ' új ablakban (tabon) megnyitja-e a saucelabs.com weboldalt.')
    @allure.severity(allure.severity_level.TRIVIAL)
    @allure.tag('logged in', 'about', 'standard_user', 'fail', 'BT-SAUCE-2026-1', 'SAUCE-US-1')
    def test_hamburger_menu_about_open(self, user):
        allure.dynamic.title(f'A hamburger menüből az About oldal megnyitásának az ellenőrzése. ({user["username"]} '
                             f'felhasználó)')
        allure.dynamic.description(
            f'A teszteset célja, hogy {user["username"]} userrel ellenőrizzük a hamburger menüben található About '
            f'menüpont működik-e, új ablakban (tabon) megnyitja-e a saucelabs.com weboldalt.')
        allure.dynamic.tag(f'{user["username"]}')
        self.main_page.do_login(user["username"], user["password"])
        number_of_window_handles_before = self.logged_in_page.get_number_of_window_handles()
        self.logged_in_page.get_hamburger_menu_button().click()
        self.logged_in_page.wait_for_hamburger_menu_to_open()
        # A teszteset során képernyőképeket készítünk a hamburger menüre kattintás előtt és után, hogy dokumentáljuk
        # a teszteset futását, és megkönnyítsük a hibakeresést, amennyiben a teszteset elbukik.
        self.logged_in_page.get_hamburger_menu_about().click()
        number_of_window_handles_after = self.logged_in_page.get_number_of_window_handles()
        try:
            assert self.logged_in_page.get_current_url() == ABOUT_URL_TESTDATA
        except AssertionError:
            self.logged_in_page.save_screenshot(f'after_click_about_bad_url{user["username"]}.png')
            pytest.fail(f'Az Aboutra kattintva nem a saucelabs.com oldal nyílt meg, '
                        f'hanem a {self.logged_in_page.get_current_url()} url.')
        # Mivel a saucelabs.com nem új ablakban (tabon) nyílik meg, ezért a teszteset elbukik.
        # Üzleti érdek, hogy a webshop ablaka mindenképpen nyitva maradjon és a saucelabs.com egy új ablakban (tabon)
        # nyíljon meg, ezért a teszteset elbukása elfogadható. Amennyiben a saucelabs.com új ablakban (tabon)
        # nyílik meg, akkor a teszteset sikeres lesz.
        try:
            assert number_of_window_handles_before != number_of_window_handles_after
        except AssertionError:
            self.logged_in_page.save_screenshot(f'after_click_about_new_tab{user["username"]}.png')
            pytest.fail('A saucelabs.com oldal nem új ablakban (tabon) nyílt meg, '
                        'hanem ugyanabban az ablakban (tabon).')


    @allure.title('A hamburger menüből a logout gomb ellenőrzése.')
    @allure.description('A teszteset célja, hogy ellenőrizzük a hamburger menüben található Logout menüpont működik-e,'
                        ' valóban kilép-e a bejelentkezett felhasználó, és visszavisz-e a főoldalra (login oldalra).')
    @allure.severity(allure.severity_level.TRIVIAL)
    @allure.tag('logged in', 'logout', 'standard_user')
    def test_hamburger_menu_logout_button(self):
        self.main_page.do_login(STANDARD_USER_LOGIN_DATA["username"], STANDARD_USER_LOGIN_DATA["password"])
        assert self.logged_in_page.get_current_url() == LOGGED_IN_URL_TESTDATA
        self.logged_in_page.get_hamburger_menu_button().click()
        self.logged_in_page.wait_for_hamburger_menu_to_open()
        self.logged_in_page.get_hamburger_menu_logout().click()
        self.main_page.wait_for_page_to_load()
        assert self.main_page.get_current_url() == MAIN_PAGE_URL_TESTDATA

    # Ellenorizzuk, hogy a fooldal aljan talalhato kozossegi media ikonok a megfelelo platform ceges oldalara
    # mutatnak-e, es rakattintva uj tabon jelennek-e meg.
    @allure.title('A X - Twitter ikon tesztelése')
    @allure.description('A teszteset célja annak ellenőrzése, hogy a főoldal alján megjelenő közösségi média ikonok '
                        'közül az X (Twitter) ikonra kattintva, új ablakban jelenik-e meg a cég oldala.')
    @allure.severity(allure.severity_level.NORMAL)
    @allure.tag('pozitív', 'X', 'Twitter', 'közösségi média', 'link')
    def test_x_twitter_icon(self):
        # - bejelentkezek
        self.main_page.do_login(STANDARD_USER_LOGIN_DATA["username"], STANDARD_USER_LOGIN_DATA["password"])

        # - a social media ikonok teszteleset kiszerveztem egy fuggvenybe, mely parametere az elvart URL,
        # valamint a lap aljan levo sm ikonok xpath-a.
        # visszateresi erteke true, ha uj tab-on nyilik meg a sm oldal es az uj tab url-je megegyezik az elvart url-el
        assert self.logged_in_page.social_media_icon_check(TWITTER_TESTDATA['url'], TWITTER_TESTDATA['xpath_locator'])

    @allure.title('A Facebook ikon tesztelése')
    @allure.description(
        'A teszteset célja annak ellenőrzése, hogy a főoldal alján megjelenő közösségi média ikonok közül a '
        'Facebook ikonra kattintva, új ablakban jelenik-e meg a cég oldala.')
    @allure.severity(allure.severity_level.NORMAL)
    @allure.tag('pozitív', 'Facebook', 'közösségi média', 'link')
    def test_facebook_icon(self):
        # - bejelentkezek
        self.main_page.do_login(STANDARD_USER_LOGIN_DATA["username"], STANDARD_USER_LOGIN_DATA["password"])

        # - a social media ikonok teszteleset kiszerveztem egy fuggvenybe, mely parametere az elvart URL,
        # valamint a lap aljan levo sm ikonok xpath-a.
        # visszateresi erteke true, ha uj tab-on nyilik meg a sm oldal es az uj tab url-je megegyezik az elvart url-el
        assert self.logged_in_page.social_media_icon_check(FACEBOOK_TESTDATA['url'], FACEBOOK_TESTDATA['xpath_locator'])

    @allure.title('A LinkedIn ikon tesztelése')
    @allure.description(
        'A teszteset célja annak ellenőrzése, hogy a főoldal alján megjelenő közösségi média ikonok közül a '
        'LinkedIn ikonra kattintva, új ablakban jelenik-e meg a cég oldala.')
    @allure.severity(allure.severity_level.NORMAL)
    @allure.tag('pozitív', 'LinkedIn', 'közösségi média', 'link')
    def test_linkedin_icon(self):
        # - bejelentkezek
        self.main_page.do_login(STANDARD_USER_LOGIN_DATA["username"], STANDARD_USER_LOGIN_DATA["password"])

        # - a social media ikonok teszteleset kiszerveztem egy fuggvenybe, mely parametere az elvart URL, valamint
        # a lap aljan levo sm ikonok xpath-a.
        # visszateresi erteke true, ha uj tab-on nyilik meg a sm oldal es az uj tab url-je megegyezik az elvart url-el
        assert self.logged_in_page.social_media_icon_check(LINKEDIN_TESTDATA['url'], LINKEDIN_TESTDATA['xpath_locator'])
