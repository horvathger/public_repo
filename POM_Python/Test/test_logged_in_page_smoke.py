import allure

from POM_Python.Pages.MainPage import MainPage
from POM_Python.Pages.LoggedInPage  import LoggedInPage
from POM_Python.Util.create_driver import create_preconfigured_chrome_driver
from POM_Python.Data.user_testdata import STANDARD_USER_LOGIN_DATA, LOCKED_OUT_USER_LOGIN_DATA, PROBLEM_USER_LOGIN_DATA, \
    PERFORMANCE_GLITCH_USER_LOGIN_DATA, ERROR_USER_LOGIN_DATA, VISUAL_USER_LOGIN_DATA

class TestLoggedInPageSmoke:
    def setup_method(self):
        browser = create_preconfigured_chrome_driver()
        self.main_page = MainPage(browser)
        self.logged_in_page = LoggedInPage(browser)

    def teardown_method(self):
        pass  # self.main_page.quit()

    @allure.title('')
    @allure.description('')
    @allure.severity(allure.severity_level.TRIVIAL)
    @allure.tag('logged in', 'standard_user')
    def test_sort_items_a_z_smoke(self):
        self.main_page.do_login(STANDARD_USER_LOGIN_DATA["username"], STANDARD_USER_LOGIN_DATA["password"])
        self.logged_in_page.select_az_sorting_options()

    @allure.title('')
    @allure.description('')
    @allure.severity(allure.severity_level.TRIVIAL)
    @allure.tag('logged in', 'standard_user')
    def test_sort_items_z_a_smoke(self):
        self.main_page.do_login(STANDARD_USER_LOGIN_DATA["username"], STANDARD_USER_LOGIN_DATA["password"])
        self.logged_in_page.select_za_sorting_options()

    @allure.title('')
    @allure.description('')
    @allure.severity(allure.severity_level.TRIVIAL)
    @allure.tag('logged in', 'standard_user')
    def test_sort_items_by_price_low_to_high_smoke(self):
        self.main_page.do_login(STANDARD_USER_LOGIN_DATA["username"], STANDARD_USER_LOGIN_DATA["password"])
        self.logged_in_page.select_price_low_to_high_sorting_options()

    @allure.title('')
    @allure.description('')
    @allure.severity(allure.severity_level.TRIVIAL)
    @allure.tag('logged in', 'standard_user')
    def test_sort_items_by_price_high_to_low_smoke(self):
        self.main_page.do_login(STANDARD_USER_LOGIN_DATA["username"], STANDARD_USER_LOGIN_DATA["password"])
        self.logged_in_page.select_price_hig_to_low_sorting_options()

