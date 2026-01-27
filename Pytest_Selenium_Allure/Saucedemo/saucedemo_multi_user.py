import time

import allure
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait

URL = 'https://www.saucedemo.com'

USER = ['standard_user', 'locked_out_user', 'problem_user', 'error_user']
PASS = 'secret_sauce'

expected_error_message = 'Epic sadface: Sorry, this user has been locked out.'

twitter_url = 'https://x.com/saucelabs'
twitter_xpath = '//a[@data-test="social-twitter"]'

facebook_url = 'https://www.facebook.com/saucelabs'
facebook_xpath = '//a[@data-test="social-facebook"]'

linkedin_url = 'https://www.linkedin.com/company/sauce-labs/'
linkedin_xpath = '//a[@data-test="social-linkedin"]'

sort_by_value = ('lohi', 'hilo')
sort_by_name = ('az', 'za')

class TestSauceDemo(object):
    def setup_method(self):
        options = Options()
        options.add_experimental_option("detach", True)
        options.add_argument('--guest')
        self.browser = webdriver.Chrome(options=options)
        self.browser.maximize_window()
        # betoltom az oldalt
        self.browser.get(URL)

    def teardown_method(self):
        self.browser.quit()

    # KISZERVEZETT FUGGVENYEK:  ***************************************

    # mivel minden teszteset elejen be kell lepni  a megnyitott oldalra ezert magat a belepest kiszervezem egy fuggvenybe.
    def login(self, username = USER[0], password = PASS):
        # - bejelentkezek
        WebDriverWait(self.browser, 5).until(EC.element_to_be_clickable((By.ID, 'user-name'))).send_keys(username)
        time.sleep(1)
        WebDriverWait(self.browser, 5).until(EC.element_to_be_clickable((By.ID, 'password'))).send_keys(password)
        WebDriverWait(self.browser, 5).until(EC.element_to_be_clickable((By.ID, 'login-button'))).click()

        try:
            WebDriverWait(self.browser, 5).until(
            EC.visibility_of_element_located((By.XPATH, '//a[@data-test="shopping-cart-link"]'))).is_displayed()
        except Exception:
            return False
        return True




    # a fuggvenyt a belepes utan, fooldalon meghivva megnyitja a fooldal bal oldalan levo hamburgermenut.
    def hamburger_menu(self):
        button_hamburger_menu = WebDriverWait(self.browser, 5).until(
            EC.element_to_be_clickable((By.XPATH, '//button[@id="react-burger-menu-btn"]')))
        button_hamburger_menu.click()

    def logout(self):
        # - megnyitom a hamburgermenut
        self.hamburger_menu()

        # - megkeresem es raklikkelek a logout gombra
        button_logout = WebDriverWait(self.browser, 5).until(EC.element_to_be_clickable((By.ID, 'logout_sidebar_link')))
        button_logout.click()

    # a fuggvenyt a belepes utan, a fooldalon meghívva a fooldal aljara gorget a footerig.
    def go_to_footer(self):
        footer = WebDriverWait(self.browser, 5).until(
            EC.presence_of_element_located((By.XPATH, '//footer[@data-test="footer"]')))
        action = ActionChains(self.browser)
        action.scroll_to_element(footer)
        action.perform()

    # a fuggvenyt a belepes utan, a fooldalon meghivva, lemegy a lap aljara, megnyitja a social media ikonokat es ellenorzi, hogy uj tabon nyilnak-e meg,
    # valamint ellenorzi, hogy az elvart oldal nyilik-e meg. Bemeneti parametere az elvart url, illetve a sm ikonra mutato xpath.
    def social_media_icon_check(self, url, xpath_string):
        # - az aktualisan nyitott ablakok szamat elmentem egy valtozoba (ez ertelemszeruen egy lesz)
        number_of_open_tabs = len(self.browser.window_handles)

        # - legorgetek a lap aljara es megkeresem a megfelelo sm ikont majd rakattintok
        self.go_to_footer()

        WebDriverWait(self.browser, 5).until(EC.element_to_be_clickable((By.XPATH, f'{xpath_string}'))).click()

        # ellenorzom, hogy uj ablakban nyilt-e meg a sm oldal
        assert len(self.browser.window_handles) == number_of_open_tabs + 1

        # atvaltok a sm ablakara es ellenorzom, hogy az url megfelelo-e
        original_window = self.browser.window_handles[0]
        new_tab = self.browser.window_handles[1]

        self.browser.switch_to.window(new_tab)
        return self.browser.current_url == url

    def picture_compare(self):
        # - lekerem az elso termek kepet a fooldalon es a kep url-et elmentem egy valtozoba
        first_product_image_main = WebDriverWait(self.browser, 5).until(
            EC.visibility_of_element_located((By.XPATH, '(//div[@class="inventory_item_img"]/a/img)[1]')))
        first_product_image_url = first_product_image_main.get_attribute('src')

        # - belepek a termeklapra a kep megklikkelesevel, majd lekerem a termeklapon talalhato kep URL-jet
        first_product_image_main.click()

        first_product_image_inside = WebDriverWait(self.browser, 5).until(
            EC.visibility_of_element_located((By.XPATH, '//img[@data-test="item-sauce-labs-backpack-img"]')))
        first_product_image_inside_url = first_product_image_inside.get_attribute('src')

        # - ellenorzom, hogy a ket url megegyezik-e
        if first_product_image_inside_url == first_product_image_inside_url:
            return True
        else:
            return False

    def about_window(self):
        # - megnyitom a hamburgermenut
        self.hamburger_menu()

        # - az aktualisan nyitott ablakok szamat elmentem egy valtozoba (ez ertelemszeruen egy lesz)
        number_of_open_tabs = len(self.browser.window_handles)

        # - rakattintok az About gombra.
        WebDriverWait(self.browser, 5).until(EC.element_to_be_clickable((By.ID, 'about_sidebar_link'))).click()

        # - ellenorzom, hogy uj ablakban nyilt-e meg.
        if len(self.browser.window_handles) == number_of_open_tabs + 1:
            return True
        else:
            return False

    # TESZTESETEK:  ***************************************

    # Locked_out user eseten ellenorizzuk le, hogy a megfelelo hibauzenet jelenik-e meg.
    @allure.title('Kizárt felhasználó belépési kísérletének ellenőrzése')
    @allure.description('A teszteset célja annak ellenőrzése, hogy a locked-out státuszú felhasználóval történő belépési kísérlet során a belpés elutasítésra kerül-e és a megfelelő hibaüzenet jelenik-e meg a képernyőn.')
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.tag('negatív', 'kitiltott felhasználó', 'hibaüzenet', 'locked_out_user')
    def test_login_with_locked_out_user(self):
        # - beirom a locked_out_user felhasznalonevet a felhasznalonev mezobe
        # - beirom a secret_sauce jelszot a jelszo mezobe
        # - megnyomom a Login gombot
        if not self.login(USER[1], PASS):
            header_error = WebDriverWait(self.browser,5).until(EC.visibility_of_element_located((By.XPATH, '//h3[@data-test="error"]')))
            assert header_error.text == expected_error_message

    # Jelentkezzunk be az oldalra, majd ellenorizzuk ennek a sikeresseget.
    @allure.title('Normál belépési folyamat ellenőrzése (standard_user)')
    @allure.description('A teszteset célja normál, engedélyezett felhasználóval történő bejelentkezés sikerességének az ellenőrzése.')
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.tag('pozitív', 'login', 'bejelentkezés')
    def test_login_standard_u(self):
        # - bejelentkezek

        assert self.login(USER[0], PASS)

    @allure.title('Belépési folyamat ellenőrzése (problem_user)')
    @allure.description('A teszteset célja normál, engedélyezett felhasználóval történő bejelentkezés sikerességének az ellenőrzése.')
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.tag('pozitív', 'login', 'bejelentkezés', 'problem_user')
    def test_login_problem_u(self):
        # - bejelentkezek

        assert self.login(USER[2], PASS)

    @allure.title('Belépési folyamat ellenőrzése (error_user)')
    @allure.description('A teszteset célja normál, engedélyezett felhasználóval történő bejelentkezés sikerességének az ellenőrzése.')
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.tag('pozitív', 'login', 'bejelentkezés', 'error_user')
    def test_login_error_u(self):
        # - bejelentkezek

        assert self.login(USER[3], PASS)

    # Bejelentkezes utan ellenorizzuk, hogy a bal oldali hamburger menuben talalhato Logout gombbal ki tudunk-e lepni.
    @allure.title('Kijelentkezés tesztelése (standard_user)')
    @allure.description('A teszteset célja annak ellenőrzése, hogy a bejelentkezett felhasználó a bal oldali hamburgermenü Logout menüpontjának használatával ki tud-e jelenkezni.')
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.tag('pozitív', 'logout', 'kijelentkezés', 'standard_user')
    def test_logout_standard(self):
        # - bejelentkezek
        self.login(USER[0], PASS)

        # - megnyitom a hamburgermenut
        self.logout()

        # ellenorzom, hogy a kilepes megtortent-e
        button_login = WebDriverWait(self.browser, 5).until((EC.visibility_of_element_located((By.ID, 'login-button'))))
        assert button_login.is_displayed()

    @allure.title('Kijelentkezés tesztelése (problem_user)')
    @allure.description('A teszteset célja annak ellenőrzése, hogy a bejelentkezett felhasználó a bal oldali hamburgermenü Logout menüpontjának használatával ki tud-e jelenkezni.')
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.tag('pozitív', 'logout', 'kijelentkezés', 'problem_user')
    def test_logout_problem_u(self):
        # - bejelentkezek
        self.login(USER[2], PASS)

        # - megnyitom a hamburgermenut
        self.logout()

        # ellenorzom, hogy a kilepes megtortent-e
        button_login = WebDriverWait(self.browser, 5).until((EC.visibility_of_element_located((By.ID, 'login-button'))))
        assert button_login.is_displayed()

    @allure.title('Kijelentkezés tesztelése (error_user)')
    @allure.description('A teszteset célja annak ellenőrzése, hogy a bejelentkezett felhasználó a bal oldali hamburgermenü Logout menüpontjának használatával ki tud-e jelenkezni.')
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.tag('pozitív', 'logout', 'kijelentkezés', 'error_user')
    def test_logout_error_u(self):
        # - bejelentkezek
        self.login(USER[3], PASS)

        # - megnyitom a hamburgermenut
        self.logout()

        # ellenorzom, hogy a kilepes megtortent-e
        button_login = WebDriverWait(self.browser, 5).until((EC.visibility_of_element_located((By.ID, 'login-button'))))
        assert button_login.is_displayed()


    # Bejelentkezes utan ellenorizzuk le, hogy a szuro mezo 4 db opciot tartalmaz.
    @allure.title('Szűrőmező hosszának ellenőrzése (standard_user')
    @allure.description('A teszteset célja annak ellenőrzése, hogy bejelentkezés után a jobb oldali szűrő- rendező listának négy eleme van-e.')
    @allure.severity(allure.severity_level.NORMAL)
    @allure.tag('pozitív', 'szűrés', 'rendezés', 'legördülő menü', 'standard_user')
    def test_product_sort_container_length(self):
        # - bejelentkezek
        self.login(USER[0], PASS)

        # - lekerem a legordulomenu elemeit tartalmazo webelementet
        legordulo_menu = WebDriverWait(self.browser, 5).until(
            EC.presence_of_all_elements_located((By.XPATH, '//select[@data-test="product-sort-container"]/option')))

        # - ellenorzom, hogy a legordulo menu 4db webelementet tartalmaz.
        assert len(legordulo_menu) == 4


    # ABC alapjan csokkeno sorrendbe rendezes funkcio mukodik-e
    # ABC alapjan novekvo sorrendbe rendezes funkcio mukodik-e
    @allure.title('Termékek név szerint növekvő és csökkenő sorrendbe rendezése (standard_user')
    @allure.description('A teszteset célja annak ellenőrzése, hogy a jobb felső részen található legördülő menüvel név szerint növekvő, illetve csökkenő rendbe rendezhetőek-e a termékek.')
    @allure.severity(allure.severity_level.MINOR)
    @allure.tag('pozitív', 'rendezés', 'név szerint', 'standard_user')
    def test_sort_by_name(self):
        # - bejelentkezek
        self.login(USER[0], PASS)

        for sort_by in sort_by_name:
            # - a valaszteklistabol kivalasztom az ar szerint novekvo illetve a csokeno rendbe rendezest
            select_sort = Select(WebDriverWait(self.browser, 5).until(
                EC.element_to_be_clickable((By.XPATH, '//select[@data-test="product-sort-container"]'))))
            select_sort.select_by_value(sort_by)

            # - kigyujtom a termekek arait egy webelement listaba, majd for ciklussal vegig megyek, az elso karaktert ($) levagom, a tobbi karaktert tortszamma konvertalva hozzaadom az eredmenylistahoz.
            osszes_nev = self.browser.find_elements(By.XPATH, '//div[@data-test="inventory-item-name"]')
            termeknevek_listaja = []
            for nev in osszes_nev:
                termeknevek_listaja.append(nev.text)

            # - ellenorzom, hogy a kinyert arlista megegyezik-e ugyanezen lista novekvobe rendezett formajaval
            if sort_by == 'az':
                assert termeknevek_listaja == sorted(termeknevek_listaja)
            elif sort_by == 'za':
                assert termeknevek_listaja == sorted(termeknevek_listaja, reverse=True)


    # Az ar alapjan csokkeno sorrendbe rendezes funkcio mukodik-e
    # Az ar alapjan novekvo sorrendbe rendezes funkcio mukodik-e
    @allure.title('Termékek ár szerint növekvő és csökkenő sorrendbe rendezése (standard_user')
    @allure.description('A teszteset célja annak ellenőrzése, hogy a jobb felső részen található legördülő menüvel ár szerint növekvő, illetve csökkenő rendbe rendezhetőek-e a termékek.')
    @allure.severity(allure.severity_level.MINOR)
    @allure.tag('pozitív', 'rendezés', 'ár szerint', 'standard_user')
    def test_sort_by_price(self):
        # - bejelentkezek
        self.login(USER[0], PASS)

        for sort_by in sort_by_value:
            # - a valaszteklistabol kivalasztom az ar szerint novekvo illetve a csokeno rendbe rendezest
            select_sort = Select(WebDriverWait(self.browser, 5).until(
                EC.element_to_be_clickable((By.XPATH, '//select[@data-test="product-sort-container"]'))))
            select_sort.select_by_value(sort_by)

            # - kigyujtom a termekek arait egy webelement listaba, majd for ciklussal vegig megyek, az elso karaktert ($) levagom, a tobbi karaktert tortszamma konvertalva hozzaadom az eredmenylistahoz.
            arak_szovegesen = self.browser.find_elements(By.XPATH, '//div[@data-test="inventory-item-price"]')
            arak_szammal = []
            for ar in arak_szovegesen:
                arak_szammal.append(float(ar.text[1:]))

        # - a biztonsag kedveert ellenorzom, hogy nincs nulla, vagy negativ erteku ar-e a lista elejen.
                assert arak_szammal[0] > 0

        # - ellenorzom, hogy a kinyert arlista megegyezik-e ugyanezen lista novekvobe rendezett formajaval
        if sort_by == 'lohi':
            assert arak_szammal == sorted(arak_szammal)
        elif sort_by == 'hilo':
            assert arak_szammal == sorted(arak_szammal, reverse=True)

    # Helyezzunk termekeket a kosarunkba, és ellenorizzuk le, hogy a kosar melletti ikon a termekek szamat mutatja-e.
    @allure.title('Termékek kosárba helyezése és a kosár számlálójának ellenőrzése (standard_user)')
    @allure.description('A teszteset célja annak ellenőrzése, hogy ha termékeket helyezünk a bevásárlókosárba, akkor a jobb fölső sarokban található kosáron a kosárba helyezett termékek számának megfelelő szám jelenik-e meg.')
    @allure.severity(allure.severity_level.NORMAL)
    @allure.tag('pozitív', 'kosár', 'termék', 'standard_user')
    def test_shopping_cart_badge(self):
        # - bejelentkezek
        self.login(USER[0], PASS)

        # - megkeresem a listaban az elso harom termek Add to cart gombjat es raklikkelek. Ellenorzom, hogy a bevasarlokosar ikonon megjelenik-e a termekek darabszama.
        for i in range(1, 4):
            WebDriverWait(self.browser, 5).until(
                EC.element_to_be_clickable((By.XPATH, f'(//div[@class="pricebar"]/button)[{i}]'))).click()
            shopping_cart_badge_number = WebDriverWait(self.browser, 5).until(
            EC.visibility_of_element_located((By.XPATH, '//span[@data-test="shopping-cart-badge"]')))
            assert int(shopping_cart_badge_number.text) == i


    # Ellenőrizzük le, hogy minden ár dollárban van-e megadva.
    @allure.title('Valuta ellenőrzése (standard_user)')
    @allure.description('A teszteset célja annak ellenőrzése, hogy a honalpon a termékek ára mindenhol dollárban van-e megjelenítve.')
    @allure.severity(allure.severity_level.NORMAL)
    @allure.tag('pozitív', 'ár', 'valuta', 'standard_user')
    def test_all_price_dollar(self):
        # - bejelentkezek
        self.login(USER[0], PASS)

        # - megkeresem az arakat tartalmazo webelementeket es egy for ciklussal vegig megyek rajtuk. Minden iteracioban megvizsgalom, hogy az ar elso karaktere ($) jel-e.
        # ha igen, akkor egy bool valtozohoz, amie alapbol True hozza and-elek egy True-t. Ha nem, akkor pedig egy False-ot. Ha egyetlen iteraciora is False, hogy az elso
        # karakter $, akkor a bool valtozo erteke False lesz a vegen.
        arak = self.browser.find_elements(By.XPATH, '//div[@data-test="inventory-item-price"]')
        mind_dollar = True
        for ar in arak:
            if ar.text[0] == '$':
                mind_dollar = mind_dollar and True
            else:
                mind_dollar = mind_dollar and False

        # kiertekelem a kapott eredmenyt
        assert mind_dollar == True


    # Ellenőrizzük le, hogy a listában megjelenő kép forrása (src) megegyezik a terméklapon megjelenő kép forrásával (egy konkrét termék esetén).
    @allure.title('A termék képének ellenőrzése a főoldalon és a terméklapon. (standard_user)')
    @allure.description('A teszteset célja annak ellenőrzése, hogy a termék képe a főoldalon megegyezik-e a terméklapon szereplő képpel.')
    @allure.severity(allure.severity_level.NORMAL)
    @allure.tag('pozitív', 'kép', 'termék', 'standard_user')
    def test_product_image_url_standard_u(self):
        # - bejelentkezek
        self.login(USER[0], PASS)

        # - ellenorzom, hogy a ket url megegyezik-e
        assert self.picture_compare()

    #Elbuko teszteset, mert a fooldalon a termek kepe helyett egy kutyus latszik.
    @allure.title('A termék képének ellenőrzése a főoldalon és a terméklapon. (problem_user)')
    @allure.description('A teszteset célja annak ellenőrzése, hogy a termék képe a főoldalon megegyezik-e a terméklapon szereplő képpel.')
    @allure.severity(allure.severity_level.NORMAL)
    @allure.tag('pozitív', 'kép', 'termék', 'problem_user')
    def test_product_image_url(self):
        # - bejelentkezek
        self.login(USER[2], PASS)

        # - ellenorzom, hogy a ket url megegyezik-e
        assert self.picture_compare()

    @allure.title('A termék képének ellenőrzése a főoldalon és a terméklapon. (error_user)')
    @allure.description('A teszteset célja annak ellenőrzése, hogy a termék képe a főoldalon megegyezik-e a terméklapon szereplő képpel.')
    @allure.severity(allure.severity_level.NORMAL)
    @allure.tag('pozitív', 'kép', 'termék', 'error_user')
    def test_product_image_url(self):
        # - bejelentkezek
        self.login(USER[3], PASS)

        # - ellenorzom, hogy a ket url megegyezik-e
        assert self.picture_compare()


    # Ellenorizzuk le, hogy a hamburgermenuben az About gombra kattintva a swaglabs.com uj tab-on jelenik-e meg.
    # ELBUKÓ TESZTESET, mert nem nyit uj tabot az oldal betoltesekor, pedig uzleti szempontbol indokolt lenne, hogy a webshop oldala nyitva maradjon.
    @allure.title('About menüpont ellenőrzése (standard_user)')
    @allure.description('A teszteset célja annak ellenőrzése, hogy a hamburger menü, About menüpontjára kattintva a https://saucelabs.com/ URL új tab-on jelenik-e meg.')
    @allure.severity(allure.severity_level.NORMAL)
    @allure.tag('pozitív', 'about', 'új ablak', 'standard_user')
    def test_about_on_new_tab_standard_u(self):
        # - bejelentkezek
        self.login(USER[0], PASS)

        # - ellenorzom, hogy uj ablakban nyilt-e meg.
        assert self.about_window()

    @allure.title('About menüpont ellenőrzése (problem_user)')
    @allure.description('A teszteset célja annak ellenőrzése, hogy a hamburger menü, About menüpontjára kattintva a https://saucelabs.com/ URL új tab-on jelenik-e meg.')
    @allure.severity(allure.severity_level.NORMAL)
    @allure.tag('pozitív', 'about', 'új ablak', 'problem_user')
    def test_about_on_new_tab_problem_u(self):
        # - bejelentkezek
        self.login(USER[2], PASS)

        # - ellenorzom, hogy uj ablakban nyilt-e meg.
        assert self.about_window()

    @allure.title('About menüpont ellenőrzése (error_user)')
    @allure.description('A teszteset célja annak ellenőrzése, hogy a hamburger menü, About menüpontjára kattintva a https://saucelabs.com/ URL új tab-on jelenik-e meg.')
    @allure.severity(allure.severity_level.NORMAL)
    @allure.tag('pozitív', 'about', 'új ablak', 'error_user')
    def test_about_on_new_tab_error_u(self):
        # - bejelentkezek
        self.login(USER[3], PASS)

        # - ellenorzom, hogy uj ablakban nyilt-e meg.
        assert self.about_window()

    # Ellenorizzuk, hogy a fooldal aljan talalhato kozossegi media ikonok a megfelelo platform ceges oldalara mutatnak-e, es rakattintva uj tabon jelennek-e meg.
    @allure.title('A X - Twitter ikon tesztelése (standard_user)')
    @allure.description('A teszteset célja annak ellenőrzése, hogy a főoldal alján megjelenő közösségi média ikonok közül az X (Twitter) ikonra kattintva, új ablakban jelenik-e meg a cég oldala.')
    @allure.severity(allure.severity_level.NORMAL)
    @allure.tag('pozitív', 'X', 'Twitter', 'közösségi média', 'link', 'standard_user')
    def test_x_twitter_icon_standard_u(self):
        # - bejelentkezek
        self.login(USER[0], PASS)

        # - a social media ikonok teszteleset kiszerveztem egy fuggvenybe, mely parametere az elvart URL, valamint a lap aljan levo sm ikonok xpath-a.
        # visszateresi erteke true, ha uj tab-on nyilik meg a sm oldal es az uj tab url-je megegyezik az elvart url-el
        assert self.social_media_icon_check(twitter_url, twitter_xpath)

    @allure.title('A X - Twitter ikon tesztelése (problem_user)')
    @allure.description('A teszteset célja annak ellenőrzése, hogy a főoldal alján megjelenő közösségi média ikonok közül az X (Twitter) ikonra kattintva, új ablakban jelenik-e meg a cég oldala.')
    @allure.severity(allure.severity_level.NORMAL)
    @allure.tag('pozitív', 'X', 'Twitter', 'közösségi média', 'link', 'problem_user')
    def test_x_twitter_icon_problem_u(self):
        # - bejelentkezek
        self.login(USER[2], PASS)

        # - a social media ikonok teszteleset kiszerveztem egy fuggvenybe, mely parametere az elvart URL, valamint a lap aljan levo sm ikonok xpath-a.
        # visszateresi erteke true, ha uj tab-on nyilik meg a sm oldal es az uj tab url-je megegyezik az elvart url-el
        assert self.social_media_icon_check(twitter_url, twitter_xpath)

    @allure.title('A X - Twitter ikon tesztelése (error_user)')
    @allure.description('A teszteset célja annak ellenőrzése, hogy a főoldal alján megjelenő közösségi média ikonok közül az X (Twitter) ikonra kattintva, új ablakban jelenik-e meg a cég oldala.')
    @allure.severity(allure.severity_level.NORMAL)
    @allure.tag('pozitív', 'X', 'Twitter', 'közösségi média', 'link', 'error_user')
    def test_x_twitter_icon_error_u(self):
        # - bejelentkezek
        self.login(USER[3], PASS)

        # - a social media ikonok teszteleset kiszerveztem egy fuggvenybe, mely parametere az elvart URL, valamint a lap aljan levo sm ikonok xpath-a.
        # visszateresi erteke true, ha uj tab-on nyilik meg a sm oldal es az uj tab url-je megegyezik az elvart url-el
        assert self.social_media_icon_check(twitter_url, twitter_xpath)


    @allure.title('A Facebook ikon tesztelése (standard_user)')
    @allure.description(
        'A teszteset célja annak ellenőrzése, hogy a főoldal alján megjelenő közösségi média ikonok közül a Facebook ikonra kattintva, új ablakban jelenik-e meg a cég oldala.')
    @allure.severity(allure.severity_level.NORMAL)
    @allure.tag('pozitív', 'Facebook', 'közösségi média', 'link', 'standard_user')
    def test_facebook_icon_standard_u(self):
        # - bejelentkezek
        self.login(USER[0], PASS)

        # - a social media ikonok teszteleset kiszerveztem egy fuggvenybe, mely parametere az elvart URL, valamint a lap aljan levo sm ikonok xpath-a.
        # visszateresi erteke true, ha uj tab-on nyilik meg a sm oldal es az uj tab url-je megegyezik az elvart url-el
        assert self.social_media_icon_check(facebook_url, facebook_xpath)

    @allure.title('A Facebook ikon tesztelése (problem_user)')
    @allure.description(
        'A teszteset célja annak ellenőrzése, hogy a főoldal alján megjelenő közösségi média ikonok közül a Facebook ikonra kattintva, új ablakban jelenik-e meg a cég oldala.')
    @allure.severity(allure.severity_level.NORMAL)
    @allure.tag('pozitív', 'Facebook', 'közösségi média', 'link', 'problem_user')
    def test_facebook_icon_problem_u(self):
        # - bejelentkezek
        self.login(USER[2], PASS)

        # - a social media ikonok teszteleset kiszerveztem egy fuggvenybe, mely parametere az elvart URL, valamint a lap aljan levo sm ikonok xpath-a.
        # visszateresi erteke true, ha uj tab-on nyilik meg a sm oldal es az uj tab url-je megegyezik az elvart url-el
        assert self.social_media_icon_check(facebook_url, facebook_xpath)

    @allure.title('A Facebook ikon tesztelése (error_user)')
    @allure.description(
        'A teszteset célja annak ellenőrzése, hogy a főoldal alján megjelenő közösségi média ikonok közül a Facebook ikonra kattintva, új ablakban jelenik-e meg a cég oldala.')
    @allure.severity(allure.severity_level.NORMAL)
    @allure.tag('pozitív', 'Facebook', 'közösségi média', 'link', 'error_user')
    def test_facebook_icon_error_u(self):
        # - bejelentkezek
        self.login(USER[3], PASS)

        # - a social media ikonok teszteleset kiszerveztem egy fuggvenybe, mely parametere az elvart URL, valamint a lap aljan levo sm ikonok xpath-a.
        # visszateresi erteke true, ha uj tab-on nyilik meg a sm oldal es az uj tab url-je megegyezik az elvart url-el
        assert self.social_media_icon_check(facebook_url, facebook_xpath)


    @allure.title('A LinkedIn ikon tesztelése (standard_user)')
    @allure.description(
        'A teszteset célja annak ellenőrzése, hogy a főoldal alján megjelenő közösségi média ikonok közül a LinkedIn ikonra kattintva, új ablakban jelenik-e meg a cég oldala.')
    @allure.severity(allure.severity_level.NORMAL)
    @allure.tag('pozitív', 'LinkedIn', 'közösségi média', 'link', 'standard_user')
    def test_linkedin_icon_standard_u(self):
        # - bejelentkezek
        self.login(USER[0], PASS)

        # - a social media ikonok teszteleset kiszerveztem egy fuggvenybe, mely parametere az elvart URL, valamint a lap aljan levo sm ikonok xpath-a.
        # visszateresi erteke true, ha uj tab-on nyilik meg a sm oldal es az uj tab url-je megegyezik az elvart url-el
        assert self.social_media_icon_check(linkedin_url, linkedin_xpath)


    @allure.title('A LinkedIn ikon tesztelése (problem_user)')
    @allure.description(
        'A teszteset célja annak ellenőrzése, hogy a főoldal alján megjelenő közösségi média ikonok közül a LinkedIn ikonra kattintva, új ablakban jelenik-e meg a cég oldala.')
    @allure.severity(allure.severity_level.NORMAL)
    @allure.tag('pozitív', 'LinkedIn', 'közösségi média', 'link', 'problem_user')
    def test_linkedin_icon_problem_u(self):
        # - bejelentkezek
        self.login(USER[2], PASS)

        # - a social media ikonok teszteleset kiszerveztem egy fuggvenybe, mely parametere az elvart URL, valamint a lap aljan levo sm ikonok xpath-a.
        # visszateresi erteke true, ha uj tab-on nyilik meg a sm oldal es az uj tab url-je megegyezik az elvart url-el
        assert self.social_media_icon_check(linkedin_url, linkedin_xpath)

    @allure.title('A LinkedIn ikon tesztelése (error_user)')
    @allure.description(
        'A teszteset célja annak ellenőrzése, hogy a főoldal alján megjelenő közösségi média ikonok közül a LinkedIn ikonra kattintva, új ablakban jelenik-e meg a cég oldala.')
    @allure.severity(allure.severity_level.NORMAL)
    @allure.tag('pozitív', 'LinkedIn', 'közösségi média', 'link', 'error_user')
    def test_linkedin_icon_standard_u(self):
        # - bejelentkezek
        self.login(USER[3], PASS)

        # - a social media ikonok teszteleset kiszerveztem egy fuggvenybe, mely parametere az elvart URL, valamint a lap aljan levo sm ikonok xpath-a.
        # visszateresi erteke true, ha uj tab-on nyilik meg a sm oldal es az uj tab url-je megegyezik az elvart url-el
        assert self.social_media_icon_check(linkedin_url, linkedin_xpath)




    # Helyezzunk ket termeket a kosarba, majd ellenorizzuk, hogy ugyanazok a termekek jelennek-e meg a kosarban.


"""
# Tesztesetek:

# Helyezzunk ket termeket a kosarba a fooldalon, majd a kosarra lepve ellenorizzuk, hogy a termekek neve es ara megegyezik-e a kijelolt termekekkel.
#   A Remove gombbal tavolitsunk el egy termeket a kosarbol es ellenorizzuk, hogy eltunt-e
#   A Remuve gombbal tavolitsuk el a masik termeket is es ellenorizzuk, hogy a kosar ures.
#   Kattintsunk a Continue Shopping gombra es helyezzuk a termeke ismet a kosarba, majd ellenorizzuk ennek sikeresseget


# Kattintsunk egy termekre es a termeklapon helyezzunk ket termeket a kosarba a fooldalon.
#   Kattintsunk a Back to products gombra majd a kovetkezo termekre es helyezzuk azt is a kosarba. 
#   Lepjunk a kosarba es ellenorizzuk a termekek jelenletet.


Szervezzuk ki az alabbi lepeseket kulon fuggvenybe:
Helyezzunk ket termeket a kosarba, lepjunk a kosarra, majd kattintsunk ra a Checkout gombra
#   Maslojuk be a TESTADATokbol a firstname, lastname, postal_code adatokat a szoveges beviteli mezokbe és kattintsunk a Continue gombra.


Helyezzunk ket termeket a kosarba, lepjunk a kosarra, majd kattintsunk ra a Checkout gombra
#   Maslojuk be a TESTADATokbol a firstname, lastname, postal_code adatokat a szoveges beviteli mezokbe és kattintsunk a Continue gombra.
#   probaljuk megvaltoztatni a termekek darabszamat

Helyezzunk ket termeket a kosarba, lepjunk a kosarra, majd kattintsunk ra a Checkout gombra
#   Maslojuk be a TESTADATokbol a firstname, lastname, postal_code adatokat a szoveges beviteli mezokbe és kattintsunk a Continue gombra.
# ellenorizzuk a termekek nevet es arat a fooldalon jelzettekkel.

Helyezzunk ket termeket a kosarba, lepjunk a kosarra, majd kattintsunk ra a Checkout gombra
#   Maslojuk be a TESTADATokbol a firstname, lastname, postal_code adatokat a szoveges beviteli mezokbe és kattintsunk a Continue gombra.
#   Ellenorizzuk, hogy a ket termek aranak az osszege megeggyezik az Item total ertekkel

Helyezzunk ket termeket a kosarba, lepjunk a kosarra, majd kattintsunk ra a Checkout gombra
#   Maslojuk be a TESTADATokbol a firstname, lastname, postal_code adatokat a szoveges beviteli mezokbe és kattintsunk a Continue gombra.
#   Ellenorizzuk hogy az Item_total + Tax == Total-lal.

Helyezzunk ket termeket a kosarba, lepjunk a kosarra, majd kattintsunk ra a Checkout gombra
#   Maslojuk be a TESTADATokbol a firstname, lastname, postal_code adatokat a szoveges beviteli mezokbe és kattintsunk a Continue gombra.
#   kattintsunk a Finish gombra.
#   Ellenorizzuk, hogy a 'Thank you for your order!' felirat megjelenik-e az oldalon.

Helyezzunk ket termeket a kosarba, lepjunk a kosarra, majd kattintsunk ra a Checkout gombra
#   Maslojuk be a TESTADATokbol a firstname, lastname, postal_code adatokat a szoveges beviteli mezokbe és kattintsunk a Continue gombra.
#   Kattintsunk a Finish gombra.
#   Kattintsunk a Back Home gombra.
#   Ellenorizzuk, hogy a fooldalra jutunk-e, es a bevasarlokosar ures-e.

Az összes tesztesetet futtassuk le problem userrel és error userrel is.

"""
