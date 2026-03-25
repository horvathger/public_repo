import pytest

from POM_Python.Pages.CheckoutStepOnePage import CheckoutStepOnePage

@pytest.fixture
def pages(driver):
    checkout_step_one_page = CheckoutStepOnePage(driver)

    return {
        "checkout_step_one_page": checkout_step_one_page
    }


@pytest.fixture
def user(request):
    return request.param
