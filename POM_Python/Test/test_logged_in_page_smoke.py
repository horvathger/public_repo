import allure

from POM_Python.Data.user_testdata import STANDARD_USER_LOGIN_DATA
from POM_Python.Pages.LoggedInPage import LoggedInPage
from POM_Python.Pages.MainPage import MainPage
from POM_Python.Util.create_driver import create_preconfigured_chrome_driver


class TestLoggedInPageSmoke:
    def setup_method(self):
        browser = create_preconfigured_chrome_driver()
        self.main_page = MainPage(browser)
        self.logged_in_page = LoggedInPage(browser)

    def teardown_method(self):
        self.main_page.quit()

    @allure.title('A hamburger menü megnyitásának és tartalmának ellenőrzése.')
    @allure.description('A teszteset célja, hogy ellenőrizze a hamburger menü megnyitását és a benne található elemek '
                        'elérhetőségét egy standard felhasználóval történő bejelentkezés után.')
    @allure.severity(allure.severity_level.TRIVIAL)
    @allure.tag('logged in', 'standard_user')
    def test_hamburger_menu_content(self):
        self.main_page.do_login(STANDARD_USER_LOGIN_DATA["username"], STANDARD_USER_LOGIN_DATA["password"])
        self.logged_in_page.get_hamburger_menu_button().click()
        self.logged_in_page.wait_for_hamburger_menu_to_open()
        assert self.logged_in_page.get_hamburger_menu_close_button().is_displayed()
        assert self.logged_in_page.get_hamburger_menu_close_button().is_enabled()
        assert self.logged_in_page.get_hamburger_menu_about().is_displayed()
        assert self.logged_in_page.get_hamburger_menu_about().is_enabled()
        assert self.logged_in_page.get_hamburger_menu_logout().is_displayed()
        assert self.logged_in_page.get_hamburger_menu_logout().is_enabled()

    @allure.title('A shopping cart ellenőrzése.')
    @allure.description('A teszteset célja, hogy ellenőrizze a shopping cart megjelenik-e az oldalon.')
    @allure.severity(allure.severity_level.TRIVIAL)
    @allure.tag('logged in', 'standard_user')
    def test_shopping_cart(self):
        self.main_page.do_login(STANDARD_USER_LOGIN_DATA["username"], STANDARD_USER_LOGIN_DATA["password"])
        assert self.logged_in_page.get_shopping_cart_button().is_displayed()
        assert self.logged_in_page.get_shopping_cart_button().is_enabled()

    @allure.title('A termékek képeinek ellenőrzése.')
    @allure.description('A teszteset célja, hogy ellenőrizze a termékek képe megjelenik-e az oldalon.')
    @allure.severity(allure.severity_level.TRIVIAL)
    @allure.tag('logged in', 'standard_user')
    def test_product_images_visibility(self):
        self.main_page.do_login(STANDARD_USER_LOGIN_DATA["username"], STANDARD_USER_LOGIN_DATA["password"])
        for product_image in self.logged_in_page.get_product_img_list():
            assert product_image.is_displayed()

    @allure.title('A termékek leírásainak ellenőrzése.')
    @allure.description('A teszteset célja, hogy ellenőrizze a termékek leírása megjelenik-e az oldalon.')
    @allure.severity(allure.severity_level.TRIVIAL)
    @allure.tag('logged in', 'standard_user')
    def test_product_descriptions_visibility(self):
        self.main_page.do_login(STANDARD_USER_LOGIN_DATA["username"], STANDARD_USER_LOGIN_DATA["password"])
        for product_description in self.logged_in_page.get_product_description_list():
            assert product_description.is_displayed()

    @allure.title('A termékek neveinek ellenőrzése.')
    @allure.description('A teszteset célja, hogy ellenőrizze a termékek neve megjelenik-e az oldalon.')
    @allure.severity(allure.severity_level.TRIVIAL)
    @allure.tag('logged in', 'standard_user')
    def test_product_names_visibility(self):
        self.main_page.do_login(STANDARD_USER_LOGIN_DATA["username"], STANDARD_USER_LOGIN_DATA["password"])
        for product_name in self.logged_in_page.get_product_name_list():
            assert product_name.is_displayed()

    @allure.title('A termékek árainak ellenőrzése.')
    @allure.description('A teszteset célja, hogy ellenőrizze a termékek ára megjelenik-e az oldalon.')
    @allure.severity(allure.severity_level.TRIVIAL)
    @allure.tag('logged in', 'standard_user')
    def test_product_prices_visibility(self):
        self.main_page.do_login(STANDARD_USER_LOGIN_DATA["username"], STANDARD_USER_LOGIN_DATA["password"])
        for product_price in self.logged_in_page.get_product_price_list():
            assert product_price.is_displayed()

    @allure.title('A termékeknél található "Add To Cart" gombok ellenőrzése.')
    @allure.description(
        'A teszteset célja, hogy ellenőrizze a termékek mellett található "Add To Cart" gomb megjelenik-e az oldalon.')
    @allure.severity(allure.severity_level.TRIVIAL)
    @allure.tag('logged in', 'standard_user')
    def test_product_add_to_cart_buttons_visibility(self):
        self.main_page.do_login(STANDARD_USER_LOGIN_DATA["username"], STANDARD_USER_LOGIN_DATA["password"])
        for product_add_to_cart_button in self.logged_in_page.get_add_to_cart_button_list():
            assert product_add_to_cart_button.is_displayed()
            assert product_add_to_cart_button.is_enabled()

    @allure.title('A termékek A-Z szerinti rendezésének ellenőrzése.')
    @allure.description('A teszteset célja, hogy ellenőrizze a termékek A-Z szerinti rendezésének működését egy '
                        'standard felhasználóval ')
    @allure.severity(allure.severity_level.TRIVIAL)
    @allure.tag('logged in', 'standard_user')
    def test_sort_items_a_z_smoke(self):
        self.main_page.do_login(STANDARD_USER_LOGIN_DATA["username"], STANDARD_USER_LOGIN_DATA["password"])
        self.logged_in_page.select_az_sorting_options()
        list_of_names = []
        for product_name in self.logged_in_page.get_product_name_list():
            list_of_names.append(product_name.text)
        sorted_list_of_names = sorted(list_of_names)
        assert list_of_names == sorted_list_of_names

    @allure.title('A termékek Z-A szerinti rendezésének ellenőrzése.')
    @allure.description('A teszteset célja, hogy ellenőrizze a termékek Z-A szerinti rendezésének működését standard '
                        'felhasználóval ')
    @allure.severity(allure.severity_level.TRIVIAL)
    @allure.tag('logged in', 'standard_user')
    def test_sort_items_z_a_smoke(self):
        self.main_page.do_login(STANDARD_USER_LOGIN_DATA["username"], STANDARD_USER_LOGIN_DATA["password"])
        self.logged_in_page.select_za_sorting_options()
        list_of_names = []
        for product_name in self.logged_in_page.get_product_name_list():
            list_of_names.append(product_name.text)
        sorted_list_of_names = sorted(list_of_names, reverse=True)
        assert list_of_names == sorted_list_of_names

    @allure.title('A termékek ár szerinti növekvő rendezésének ellenőrzése.')
    @allure.description('A teszteset célja, hogy ellenőrizze a termékek ár szerinti növekvő rendezésének működését '
                        'standard felhasználóval.')
    @allure.severity(allure.severity_level.TRIVIAL)
    @allure.tag('logged in', 'standard_user')
    def test_sort_items_by_price_low_to_high_smoke(self):
        self.main_page.do_login(STANDARD_USER_LOGIN_DATA["username"], STANDARD_USER_LOGIN_DATA["password"])
        self.logged_in_page.select_price_low_to_high_sorting_options()
        list_of_prices = []
        for product_price in self.logged_in_page.get_product_price_list():
            price_as_float = float(product_price.text.replace('$', ''))
            list_of_prices.append(price_as_float)
        sorted_list_of_prices = sorted(list_of_prices)
        assert list_of_prices == sorted_list_of_prices

    @allure.title('A termékek ár szerinti csökkenő rendezésének ellenőrzése.')
    @allure.description('A teszteset célja, hogy ellenőrizze a termékek ár szerinti csökkenő rendezésének működését '
                        'standard user felhasználóval.')
    @allure.severity(allure.severity_level.TRIVIAL)
    @allure.tag('logged in', 'standard_user')
    def test_sort_items_by_price_high_to_low_smoke(self):
        self.main_page.do_login(STANDARD_USER_LOGIN_DATA["username"], STANDARD_USER_LOGIN_DATA["password"])
        self.logged_in_page.select_price_hig_to_low_sorting_options()
        list_of_prices = []
        for product_price in self.logged_in_page.get_product_price_list():
            price_as_float = float(product_price.text.replace('$', ''))
            list_of_prices.append(price_as_float)
        sorted_list_of_prices = sorted(list_of_prices, reverse=True)
        assert list_of_prices == sorted_list_of_prices

    @allure.title('A weboldal alján lévő Twitter ikon ellenőrzése.')
    @allure.description('A teszteset célja, hogy ellenőrizze a weboldal alján található Twitter ikon megjelenését.')
    @allure.severity(allure.severity_level.TRIVIAL)
    @allure.tag('logged in', 'standard_user')
    def test_footer_twitter_icon_visibility(self):
        self.main_page.do_login(STANDARD_USER_LOGIN_DATA["username"], STANDARD_USER_LOGIN_DATA["password"])
        assert self.logged_in_page.get_footer_twitter_icon().is_enabled()
        assert self.logged_in_page.get_footer_twitter_icon().is_displayed()

    @allure.title('A weboldal alján lévő Facebook ikon ellenőrzése.')
    @allure.description('A teszteset célja, hogy ellenőrizze a weboldal alján található Facebook ikon megjelenését.')
    @allure.severity(allure.severity_level.TRIVIAL)
    @allure.tag('logged in', 'standard_user')
    def test_footer_facebook_icon_visibility(self):
        self.main_page.do_login(STANDARD_USER_LOGIN_DATA["username"], STANDARD_USER_LOGIN_DATA["password"])
        assert self.logged_in_page.get_footer_facebook_icon().is_enabled()
        assert self.logged_in_page.get_footer_facebook_icon().is_displayed()

    @allure.title('A weboldal alján lévő LinkedIn ikon ellenőrzése.')
    @allure.description('A teszteset célja, hogy ellenőrizze a weboldal alján található LinkedIn ikon megjelenését.')
    @allure.severity(allure.severity_level.TRIVIAL)
    @allure.tag('logged in', 'standard_user')
    def test_footer_linkedin_icon_visibility(self):
        self.main_page.do_login(STANDARD_USER_LOGIN_DATA["username"], STANDARD_USER_LOGIN_DATA["password"])
        assert self.logged_in_page.get_footer_linkedin_icon().is_enabled()
        assert self.logged_in_page.get_footer_linkedin_icon().is_displayed()
