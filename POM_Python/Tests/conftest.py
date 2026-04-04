# A conftest.py-ba szervezett pytest.fixture hozza létre a browsert minden teszt előtt, majd a tesztek után
# bezárja a böngészőt.
import pytest

from POM_Python.Utils.create_driver import create_preconfigured_chrome_driver

@pytest.fixture
def driver():
    driver = create_preconfigured_chrome_driver()
    yield driver
    driver.quit()