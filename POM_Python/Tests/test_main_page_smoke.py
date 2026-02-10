import allure

from POM_Python.Pages.MainPage import MainPage
from POM_Python.Utils.create_driver import create_preconfigured_chrome_driver


@allure.parent_suite("UI Tests")
@allure.suite("Main page smoke tests")
@allure.sub_suite("Test cases")
class TestMainPageSmoke:
    def setup_method(self):
        browser = create_preconfigured_chrome_driver()
        self.main_page = MainPage(browser)

    def teardown_method(self):
        self.main_page.quit()

    @allure.title('Oldal fejszövegének ellenőrzése')
    @allure.description('A teszteset célja annak ellenőrzése, hogy a főoldal megfelelően betöltődik-e.')
    @allure.severity(allure.severity_level.TRIVIAL)
    @allure.tag('smoke')
    def test_main_page_load(self):
        self.main_page.visit()
        self.main_page.wait_for_page_to_load()

        assert self.main_page.get_title() == 'Swag Labs'
        assert self.main_page.get_current_url() == self.main_page.url
        assert self.main_page.get_page_header().text == 'Swag Labs'

    @allure.title('A főoldalon lévő username mező ellenőrzése')
    @allure.description(
        'A teszteset célja annak ellenőrzése, hogy a főoldalon a username mező megjelenik és interaktív-e.')
    @allure.severity(allure.severity_level.TRIVIAL)
    @allure.tag('smoke')
    def test_main_page_username_visibility(self):
        self.main_page.visit()
        self.main_page.wait_for_page_to_load()

        assert self.main_page.get_input_username().is_displayed()
        assert self.main_page.get_input_username().is_enabled()

    @allure.title('A főoldalon lévő password mező ellenőrzése')
    @allure.description(
        'A teszteset célja annak ellenőrzése, hogy a főoldalon a password mező megjelenik és interaktív-e.')
    @allure.severity(allure.severity_level.TRIVIAL)
    @allure.tag('smoke')
    def test_main_page_password_visibility(self):
        self.main_page.visit()
        self.main_page.wait_for_page_to_load()

        assert self.main_page.get_input_password().is_displayed()
        assert self.main_page.get_input_password().is_enabled()

    @allure.title('A főoldalon lévő Login gomb ellenőrzése')
    @allure.description(
        'A teszteset célja annak ellenőrzése, hogy a főoldalon a Login gomb megjelenik és interaktív-e.')
    @allure.severity(allure.severity_level.TRIVIAL)
    @allure.tag('smoke')
    def test_main_page_login_button_visibility(self):
        self.main_page.visit()
        self.main_page.wait_for_page_to_load()

        assert self.main_page.get_button_login().is_displayed()
        assert self.main_page.get_button_login().is_enabled()
