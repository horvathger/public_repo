import pytest

from POM_Python.Pages.MainPage import MainPage
from POM_Python.Pages.LoggedInPage import LoggedInPage

@pytest.fixture
def pages(driver):
    main_page = MainPage(driver)
    logged_in_page = LoggedInPage(driver)
    main_page.visit()
    main_page.wait_for_page_to_load()

    return {
        "main_page": main_page,
        "logged_in_page": logged_in_page,
    }