import pytest

from POM_Python.Pages.CheckoutCompletePage import CheckoutCompletePage
from POM_Python.Pages.CheckoutStepOnePage import CheckoutStepOnePage
from POM_Python.Pages.CheckoutStepTwoPage import CheckoutStepTwoPage
from POM_Python.Pages.LoggedInPage import LoggedInPage
from POM_Python.Pages.MainPage import MainPage



@pytest.fixture
def pages(driver):
    checkout_step_one_page = CheckoutStepOnePage(driver)
    checkout_step_two_page = CheckoutStepTwoPage(driver)
    logged_in_page = LoggedInPage(driver)
    checkout_complete_page = CheckoutCompletePage(driver)
    main_page = MainPage(driver)

    return {
        "logged_in_page": logged_in_page,
        "checkout_complete_page": checkout_complete_page,
        "main_page": main_page,
        "checkout_step_one_page": checkout_step_one_page,
        "checkout_step_two_page": checkout_step_two_page

    }


@pytest.fixture
def user(request):
    return request.param
