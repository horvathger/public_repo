import allure
import pytest

from POM_Python.Data.error_messages import LOGIN_ERROR_MESSAGE
from POM_Python.Data.main_page_testdata import LOGGED_IN_PAGE_TITLE
from POM_Python.Data.user_testdata import (ALL_USERS_LOGIN_DATA)


@allure.parent_suite("SAUCE - 26 project")
@allure.suite("Main page UI tests")
@allure.sub_suite("Test Cycle - 012")
class TestMainPage:

    @pytest.mark.parametrize("user", ALL_USERS_LOGIN_DATA, ids=[u["username"] for u in ALL_USERS_LOGIN_DATA])
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.tag('login')
    def test_login_every_user(self, user, pages):
        allure.dynamic.title(f'Belépés {user["username"]} felhasználóval')
        allure.dynamic.description(f'A teszteset célja annak ellenőrzése, hogy a {user["username"]} user be tud-e '
                                   f'lépni.')
        allure.dynamic.tag(f'{user["username"]}')

        logged_in_page = pages["logged_in_page"]
        main_page = pages["main_page"]

        main_page.do_login(user["username"], user["password"])

        if user["username"] == "locked_out_user":
            assert main_page.get_login_error_message().text == LOGIN_ERROR_MESSAGE
        else:
            logged_in_page.wait_for_page_to_load()
            assert logged_in_page.get_page_header().text == LOGGED_IN_PAGE_TITLE
            assert logged_in_page.get_current_url() == logged_in_page.url
