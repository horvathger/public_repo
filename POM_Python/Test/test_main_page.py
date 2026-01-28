import allure

from POM_Python.Pages.MainPage import MainPage
from POM_Python.Pages.LoggedInPage  import LoggedInPage
from POM_Python.Util.create_driver import create_preconfigured_chrome_driver
from POM_Python.Data.user_testdata import STANDARD_USER_LOGIN_DATA, LOCKED_OUT_USER_LOGIN_DATA, PROBLEM_USER_LOGIN_DATA, \
    PERFORMANCE_GLITCH_USER_LOGIN_DATA, ERROR_USER_LOGIN_DATA, VISUAL_USER_LOGIN_DATA

class TestMainPage:
    def setup_method(self):
        browser = create_preconfigured_chrome_driver()
        self.main_page = MainPage(browser)
        self.logged_in_page = LoggedInPage(browser)

    def teardown_method(self):
        pass  # self.main_page.quit()

    @allure.title('Belépés standard felhasználóként')
    @allure.description('A teszteset célja annak ellenőrzése, hogy a standard_user be tud-e lépni.')
    @allure.severity(allure.severity_level.TRIVIAL)
    @allure.tag('login', 'standard_user')
    def test_login_standard_user(self):
        self.main_page.do_login(STANDARD_USER_LOGIN_DATA["username"], STANDARD_USER_LOGIN_DATA["password"])
        assert self.logged_in_page.get_page_header().text == 'Swag Labs'
        assert self.logged_in_page.get_current_url() == self.logged_in_page.url

