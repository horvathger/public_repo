import allure
import pytest

from POM_Python.Data.main_page_testdata import LOGGED_IN_PAGE_TITLE
from POM_Python.Pages.MainPage import MainPage
from POM_Python.Utils.create_driver import create_preconfigured_chrome_driver


@pytest.fixture
def driver():
    driver = create_preconfigured_chrome_driver()
    yield driver
    driver.quit()


@pytest.fixture
def pages(driver):
    main_page = MainPage(driver)

    main_page.visit()
    main_page.wait_for_page_to_load()

    return {
        "main_page": main_page
    }


@allure.parent_suite("SAUCE - 26 project")
@allure.suite("Main page smoke tests")
@allure.sub_suite("Test Cycle - 013")
class TestMainPageSmoke:

    @allure.title('Oldal fejszövegének ellenőrzése')
    @allure.description('A teszteset célja annak ellenőrzése, hogy a főoldal megfelelően betöltődik-e.')
    @allure.severity(allure.severity_level.TRIVIAL)
    @allure.tag('smoke')
    def test_main_page_load(self, pages):
        main_page = pages["main_page"]

        assert main_page.get_title() == LOGGED_IN_PAGE_TITLE
        assert main_page.get_current_url() == main_page.url
        assert main_page.get_page_header().text == LOGGED_IN_PAGE_TITLE

    @allure.title('A főoldalon lévő username mező ellenőrzése')
    @allure.description(
        'A teszteset célja annak ellenőrzése, hogy a főoldalon a username mező megjelenik és interaktív-e.')
    @allure.severity(allure.severity_level.TRIVIAL)
    @allure.tag('smoke')
    def test_main_page_username_visibility(self, pages):
        main_page = pages["main_page"]

        assert main_page.get_input_username().is_displayed()
        assert main_page.get_input_username().is_enabled()

    @allure.title('A főoldalon lévő password mező ellenőrzése')
    @allure.description(
        'A teszteset célja annak ellenőrzése, hogy a főoldalon a password mező megjelenik és interaktív-e.')
    @allure.severity(allure.severity_level.TRIVIAL)
    @allure.tag('smoke')
    def test_main_page_password_visibility(self, pages):
        main_page = pages["main_page"]

        assert main_page.get_input_password().is_displayed()
        assert main_page.get_input_password().is_enabled()

    @allure.title('A főoldalon lévő Login gomb ellenőrzése')
    @allure.description(
        'A teszteset célja annak ellenőrzése, hogy a főoldalon a Login gomb megjelenik és interaktív-e.')
    @allure.severity(allure.severity_level.TRIVIAL)
    @allure.tag('smoke')
    def test_main_page_login_button_visibility(self, pages):
        main_page = pages["main_page"]

        assert main_page.get_button_login().is_displayed()
        assert main_page.get_button_login().is_enabled()
