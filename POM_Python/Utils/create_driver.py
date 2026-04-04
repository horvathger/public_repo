from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def create_preconfigured_chrome_driver():
    options = Options()
    options.add_experimental_option("detach", True)
    options.add_argument('--guest')
    options.add_argument("--headless=new") # letiltja a böngészőablak megjelenítését.
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    # options.add_argument("--window-size=1920,1080") # belállítja a böngésző ablak méretét.
    # options.add_argument("--disable-features=Translate")
    browser = webdriver.Chrome(options=options)
    browser.maximize_window()   # maximalizálja a böngésző ablakot, hogy a tesztek során minden elem látható legyen.
    return browser
