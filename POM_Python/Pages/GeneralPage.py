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
        self.browser.save_screenshot(filename)

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
