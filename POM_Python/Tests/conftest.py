import pytest

from POM_Python.Utils.create_driver import create_preconfigured_chrome_driver

@pytest.fixture
def driver():
    driver = create_preconfigured_chrome_driver()
    yield driver
    driver.quit()