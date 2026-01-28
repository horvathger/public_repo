from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def create_preconfigured_chrome_driver():
    options = Options()
    options.add_experimental_option("detach", True)
    options.add_argument('--guest')  # helyi teszteléshez kell
    # options.add_argument("--headless=new")  # CI/CD-hez kell
    options.add_argument("--no-sandbox")  # CI/CD-hez kell
    options.add_argument("--disable-dev-shm-usage")  # CI/CD-hez kell
    # options.add_argument("--window-size=1920,1080")  # CI/CD-hez kell
    # options.add_argument("--disable-features=Translate")
    # Ez a sor elméletileg kikapcsolja a jobb felső sarokban felugró nyelvválasztó kis ablakot.
    browser = webdriver.Chrome(options=options)
    browser.maximize_window()  # helyi teszteléshez kell
    return browser
