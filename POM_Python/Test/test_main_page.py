import allure

from POM_Python.Data.user_testdata import STANDARD_USER_LOGIN_DATA, LOCKED_OUT_USER_LOGIN_DATA, \
    PROBLEM_USER_LOGIN_DATA, PERFORMANCE_GLITCH_USER_LOGIN_DATA, ERROR_USER_LOGIN_DATA, VISUAL_USER_LOGIN_DATA
from POM_Python.Data.error_messages import LOGIN_ERROR_MESSAGE
from POM_Python.Pages.LoggedInPage import LoggedInPage
from POM_Python.Pages.MainPage import MainPage
from POM_Python.Util.create_driver import create_preconfigured_chrome_driver


class TestMainPage:
    def setup_method(self):
        browser = create_preconfigured_chrome_driver()
        self.main_page = MainPage(browser)
        self.logged_in_page = LoggedInPage(browser)

    def teardown_method(self):
        self.main_page.quit()

    @allure.title('Belépés standard felhasználóként')
    @allure.description('A teszteset célja annak ellenőrzése, hogy a standard_user be tud-e lépni.')
    @allure.severity(allure.severity_level.TRIVIAL)
    @allure.tag('login', 'standard_user')
    def test_login_standard_user(self):
        self.main_page.do_login(STANDARD_USER_LOGIN_DATA["username"], STANDARD_USER_LOGIN_DATA["password"])
        self.logged_in_page.wait_for_page_to_load()
        assert self.logged_in_page.get_page_header().text == 'Swag Labs'
        assert self.logged_in_page.get_current_url() == self.logged_in_page.url

    @allure.title('Belépés megkísérlése locked out felhasználóként')
    @allure.description('A teszteset célja annak ellenőrzése, hogy a locked out user be tud-e lépni.')
    @allure.severity(allure.severity_level.TRIVIAL)
    @allure.tag('login', 'locked_out_user')
    def test_login_locked_out_user(self):
        self.main_page.do_login(LOCKED_OUT_USER_LOGIN_DATA["username"], LOCKED_OUT_USER_LOGIN_DATA["password"])
        assert self.main_page.get_login_error_message().text == LOGIN_ERROR_MESSAGE

    @allure.title('Belépés megkísérlése problem user felhasználóként')
    @allure.description('A teszteset célja annak ellenőrzése, hogy a problem user be tud-e lépni.')
    @allure.severity(allure.severity_level.TRIVIAL)
    @allure.tag('login', 'problem_user')
    def test_login_problem_user(self):
        self.main_page.do_login(PROBLEM_USER_LOGIN_DATA["username"], PROBLEM_USER_LOGIN_DATA["password"])
        assert self.logged_in_page.get_page_header().text == 'Swag Labs'
        assert self.logged_in_page.get_current_url() == self.logged_in_page.url

    @allure.title('Belépés megkísérlése performance_glitch_user felhasználóként')
    @allure.description('A teszteset célja annak ellenőrzése, hogy a performance_glitch_user be tud-e lépni.')
    @allure.severity(allure.severity_level.TRIVIAL)
    @allure.tag('login', 'performance_glitch_user')
    def test_login_performance_glitch_user(self):
        self.main_page.do_login(PERFORMANCE_GLITCH_USER_LOGIN_DATA["username"],
                                PERFORMANCE_GLITCH_USER_LOGIN_DATA["password"])
        assert self.logged_in_page.get_page_header().text == 'Swag Labs'
        assert self.logged_in_page.get_current_url() == self.logged_in_page.url

    @allure.title('Belépés megkísérlése error_user felhasználóként')
    @allure.description('A teszteset célja annak ellenőrzése, hogy a error_user be tud-e lépni.')
    @allure.severity(allure.severity_level.TRIVIAL)
    @allure.tag('login', 'error_user')
    def test_login_error_user(self):
        self.main_page.do_login(ERROR_USER_LOGIN_DATA["username"], ERROR_USER_LOGIN_DATA["password"])
        assert self.logged_in_page.get_page_header().text == 'Swag Labs'
        assert self.logged_in_page.get_current_url() == self.logged_in_page.url

    @allure.title('Belépés megkísérlése visual_user felhasználóként')
    @allure.description('A teszteset célja annak ellenőrzése, hogy a visual_user be tud-e lépni.')
    @allure.severity(allure.severity_level.TRIVIAL)
    @allure.tag('login', 'visual_user')
    def test_login_visual_user(self):
        self.main_page.do_login(VISUAL_USER_LOGIN_DATA["username"], VISUAL_USER_LOGIN_DATA["password"])
        assert self.logged_in_page.get_page_header().text == 'Swag Labs'
        assert self.logged_in_page.get_current_url() == self.logged_in_page.url
