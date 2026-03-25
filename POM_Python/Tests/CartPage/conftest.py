import pytest

from POM_Python.Pages.CartPage import CartPage
from POM_Python.Pages.CheckoutStepOnePage import CheckoutStepOnePage
from POM_Python.Pages.LoggedInPage import LoggedInPage

@pytest.fixture
def pages(driver, user):
    cart_page = CartPage(driver)
    logged_in_page = LoggedInPage(driver)
    checkout_step_one_page = CheckoutStepOnePage(driver)

    cart_page.goto_cart_page_with_two_items(user["username"], user["password"])

    return {
        "cart_page": cart_page,
        "logged_in_page": logged_in_page,
        "checkout_step_one_page": checkout_step_one_page,
    }