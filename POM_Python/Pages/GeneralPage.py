import os

import allure

from POM_Python.Utils.create_driver import create_preconfigured_chrome_driver


class GeneralPage(object):

    def __init__(self, browser, url):
        self.url = url
        if browser is None:
            self.browser = create_preconfigured_chrome_driver()
        else:
            self.browser = browser

    def visit(self):
        self.browser.get(self.url)

    def quit(self):
        self.browser.quit()

    def save_screenshot(self, filename):
        # A képernyőképek egy "Screenshots" nevű könyvtárba lesznek elmentve, amely a Tests mappában jön létre,
        # ha még nem létezik.
        folder = "Screenshots"
        os.makedirs(folder, exist_ok=True)
        self.browser.save_screenshot(f"{folder}/{filename}.png")

        # Az Allure jelentésben is csatoljuk a képernyőképet, hogy könnyen megtekinthető legyen a tesztesetek futása
        # során.
        allure.attach(
            self.browser.get_screenshot_as_png(),
            name=filename,
            attachment_type=allure.attachment_type.PNG
        )

    def get_title(self):
        return self.browser.title

    def get_current_url(self):
        return self.browser.current_url

    def refresh_page(self):
        return self.browser.refresh()

    def set_window_size(self, width, height):
        self.browser.set_window_size(width, height)

    def get_window_handle(self):
        return self.browser.current_window_handle

    def get_list_of_window_handles(self):
        return self.browser.window_handles

    def get_number_of_window_handles(self):
        return len(self.browser.window_handles)
