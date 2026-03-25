import pytest

from POM_Python.Pages.LoggedInPage import LoggedInPage
from POM_Python.Pages.MainPage import MainPage

@pytest.fixture
def pages(driver, user):
    main_page = MainPage(driver)
    logged_in_page = LoggedInPage(driver)

    main_page.do_login(user["username"], user["password"])

    return {
        "main_page": main_page,
        "logged_in_page": logged_in_page,
    }