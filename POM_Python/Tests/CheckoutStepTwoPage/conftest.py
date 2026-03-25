import pytest

from POM_Python.Pages.CheckoutStepTwoPage import CheckoutStepTwoPage
from POM_Python.Pages.LoggedInPage import LoggedInPage



@pytest.fixture
def pages(driver):
    checkout_step_two_page = CheckoutStepTwoPage(driver)
    logged_in_page = LoggedInPage(driver)

    return {
        "checkout_step_two_page": checkout_step_two_page,
        "logged_in_page": logged_in_page
    }


@pytest.fixture
def user(request):
    return request.param