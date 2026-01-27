import allure
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait

URL = 'https://www.saucedemo.com'

USER = {'standard': 'standard_user', 'locked_out': 'locked_out_user', 'password': 'secret_sauce'}
standard_user = {'first_name': 'Elek', 'last_name': 'Teszt', 'postal_code': '1234'}
expected_error_message = 'Epic sadface: Sorry, this user has been locked out.'

twitter_url = 'https://x.com/saucelabs'
twitter_xpath = '//a[@data-test="social-twitter"]'

facebook_url = 'https://www.facebook.com/saucelabs'
facebook_xpath = '//a[@data-test="social-facebook"]'

linkedin_url = 'https://www.linkedin.com/company/sauce-labs/'
linkedin_xpath = '//a[@data-test="social-linkedin"]'


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
    def login(self, username, password):
        WebDriverWait(self.browser, 5).until(EC.element_to_be_clickable((By.ID, 'user-name'))).send_keys(username)
        WebDriverWait(self.browser, 5).until(EC.element_to_be_clickable((By.ID, 'password'))).send_keys(password)
        WebDriverWait(self.browser, 5).until(EC.element_to_be_clickable((By.ID, 'login-button'))).click()

    # a fuggvenyt a belepes utan, fooldalon meghivva megnyitja a fooldal bal oldalan levo hamburgermenut.
    def hamburger_menu(self):
        button_hamburger_menu = WebDriverWait(self.browser, 5).until(
            EC.element_to_be_clickable((By.XPATH, '//button[@id="react-burger-menu-btn"]')))
        button_hamburger_menu.click()

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

    # TESZTESETEK:  ***************************************

    # Locked_out user eseten ellenorizzuk le, hogy a megfelelo hibauzenet jelenik-e meg.
    @allure.title('Kizárt felhasználó belépési kísérletének ellenőrzése')
    @allure.description('A teszteset célja annak ellenőrzése, hogy a locked-out státuszú felhasználóval történő belépési kísérlet során a belpés elutasítésra kerül-e és a megfelelő hibaüzenet jelenik-e meg a képernyőn.')
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.tag('pozitív', 'kitiltott felhasználó', 'hibaüzenet')
    def test_login_with_locked_out_user(self):
        # - beirom a locked_out_user felhasznalonevet a felhasznalonev mezobe
        # - beirom a secret_sauce jelszot a jelszo mezobe
        # - megnyomom a Login gombot
        self.login(USER['locked_out'], USER['password'])

        # - ellenorzom, hogy az alabbi hibauzenetet kaptam-e: Epic sadface: Sorry, this user has been locked out.
        header_error = WebDriverWait(self.browser, 5).until(
            EC.visibility_of_element_located((By.XPATH, '//h3[@data-test="error"]')))
        assert header_error.text == expected_error_message

    # Jelentkezzunk be az oldalra, majd ellenorizzuk ennek a sikeresseget.
    @allure.title('Normál belépési folyamat ellenőrzése')
    @allure.description('A teszteset célja normál, engedélyezett felhasználóval történő bejelentkezés sikerességének az ellenőrzése.')
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.tag('pozitív', 'login', 'bejelentkezés')
    def test_login_successful(self):
        # - bejelentkezek
        self.login(USER['standard'], USER['password'])

        # - ellenorzom, hogy a jobb felso sarokban megjelenik-e a bevasarlokocsi ikon.
        shopping_cart_icon = WebDriverWait(self.browser, 5).until(
            EC.visibility_of_element_located((By.XPATH, '//a[@data-test="shopping-cart-link"]')))
        assert shopping_cart_icon.is_displayed()

    # Bejelentkezes utan ellenorizzuk, hogy a bal oldali hamburger menuben talalhato Logout gombbal ki tudunk-e lepni.
    @allure.title('Kijelentkezés tesztelése')
    @allure.description('A teszteset célja annak ellenőrzése, hogy a bejelentkezett felhasználó a bal oldali hamburgermenü Logout menüpontjának használatával ki tud-e jelenkezni.')
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.tag('pozitív', 'logout', 'kijelentkezés')
    def test_logout(self):
        # - bejelentkezek
        self.login(USER['standard'], USER['password'])

        # - megnyitom a hamburgermenut
        self.hamburger_menu()

        # - megkeresem es raklikkelek a logout gombra
        button_logout = WebDriverWait(self.browser, 5).until(EC.element_to_be_clickable((By.ID, 'logout_sidebar_link')))
        button_logout.click()

        # ellenorzom, hogy a kilepes megtortent-e
        button_login = WebDriverWait(self.browser, 5).until((EC.visibility_of_element_located((By.ID, 'login-button'))))
        assert button_login.is_displayed()

    # Bejelentkezes utan ellenorizzuk le, hogy a szuro mezo 4 db opciot tartalmaz.
    @allure.title('Szűrőmező hosszának ellenőrzése')
    @allure.description('A teszteset célja annak ellenőrzése, hogy bejelentkezés után a jobb oldali szűrő- rendező listának négy eleme van-e.')
    @allure.severity(allure.severity_level.NORMAL)
    @allure.tag('pozitív', 'szűrés', 'rendezés', 'legördülő menü')
    def test_product_sort_container_length(self):
        # - bejelentkezek
        self.login(USER['standard'], USER['password'])

        # - lekerem a legordulomenu elemeit tartalmazo webelementet
        legordulo_menu = WebDriverWait(self.browser, 5).until(
            EC.presence_of_all_elements_located((By.XPATH, '//select[@data-test="product-sort-container"]/option')))

        # - ellenorzom, hogy a legordulo menu 4db webelementet tartalmaz.
        assert len(legordulo_menu) == 4




    # ABC alapjan csokkeno sorrendbe rendezes funkcio mukodik-e
    def test_sort_by_abc_desc(self):
        # - bejelentkezek
        self.login(USER['standard'], USER['password'])

        # Egy items nevu webelement listaba kigyujtom a termekek neveit tartalmazo webelementeket, majd az így kapott listan végigmegyek es kigyujtom az itemlist-be azok textjet.
        itemlist = []
        items = WebDriverWait(self.browser,5).until(EC.visibility_of_all_elements_located((By.XPATH, '//div[@data-test="inventory-item-name"]')))
        for item in items:
            itemlist.append(item.text)
        # Ellenorzom a kezdeti rendezest, ami alapertelmezetten ABC novekvo.
        assert itemlist == sorted(itemlist)

        # kivalasztom a legordulomenubol a z-a rendezest.
        product_sort_container = Select(WebDriverWait(self.browser,5).until(EC.element_to_be_clickable((By.XPATH, '//select[@data-test="product-sort-container"]'))))
        product_sort_container.select_by_value('za')

        itemlist = []
        items = WebDriverWait(self.browser, 5).until(
            EC.visibility_of_all_elements_located((By.XPATH, '//div[@data-test="inventory-item-name"]')))
        for item in items:
            itemlist.append(item.text)
        # Ellenorzom hogy a rendezes megfordult-e.
        assert itemlist == sorted(itemlist, reverse=True)


    # ABC alapjan novekvo sorrendbe rendezes funkcio mukodik-e
    def test_sort_by_abc_asc(self):
        # - bejelentkezek
        self.login(USER['standard'], USER['password'])

        # kivalasztom a legordulomenubol a z-a rendezest.
        product_sort_container = Select(WebDriverWait(self.browser,5).until(EC.element_to_be_clickable((By.XPATH, '//select[@data-test="product-sort-container"]'))))
        product_sort_container.select_by_value('za')

        itemlist = []
        items = WebDriverWait(self.browser, 5).until(
            EC.visibility_of_all_elements_located((By.XPATH, '//div[@data-test="inventory-item-name"]')))
        for item in items:
            itemlist.append(item.text)
        # Ellenorzom hogy a rendezes megvaltozott-e csokkenobe.
        assert itemlist == sorted(itemlist, reverse=True)

        # kivalasztom a legordulomenubol a a-z rendezest.
        product_sort_container = Select(WebDriverWait(self.browser,5).until(EC.element_to_be_clickable((By.XPATH, '//select[@data-test="product-sort-container"]'))))
        product_sort_container.select_by_value('az')


        # Egy items nevu webelement listaba kigyujtom a termekek neveit tartalmazo webelementeket, majd az így kapott listan végigmegyek es kigyujtom az itemlist-be azok textjet.
        itemlist = []
        items = WebDriverWait(self.browser,5).until(EC.visibility_of_all_elements_located((By.XPATH, '//div[@data-test="inventory-item-name"]')))
        for item in items:
            itemlist.append(item.text)
        # Ellenorzom a kezdeti rendezest, ami alapertelmezetten ABC novekvo.
        assert itemlist == sorted(itemlist)




    # Az ar alapjan csokkeno sorrendbe rendezes funkcio mukodik-e




    # Az ar alapjan novekvo sorrendbe rendezes funkcio mukodik-e
    @allure.title('Termékek ár szerint növekvő sorrendbe rendezése')
    @allure.description('ä teszteset célja annak ellenőrzése, hogy a jobb felső részen található legördülő menüvel ár szerint növekvő rendbe rendezhetőek-e a termékek.')
    @allure.severity(allure.severity_level.NORMAL)
    @allure.tag('pozitív', 'rendezés', 'ár szerint', 'növekvő')
    def test_sort_by_price_asc(self):
        # - bejelentkezek
        self.login(USER['standard'], USER['password'])

        # - a valaszteklistabol kivalasztom a novekvo rendbe rendezest(lohi)
        select_sort = Select(WebDriverWait(self.browser, 5).until(
            EC.element_to_be_clickable((By.XPATH, '//select[@data-test="product-sort-container"]'))))
        select_sort.select_by_value('lohi')

        # - kigyujtom a termekek arait egy webelement listaba, majd for ciklussal vegig megyek, az elso karaktert ($) levagom, a tobbi karaktert tortszamma konvertalva hozzaadom az eredmenylistahoz.
        arak_szovegesen = self.browser.find_elements(By.XPATH, '//div[@data-test="inventory-item-price"]')
        arak_szammal = []
        for ar in arak_szovegesen:
            arak_szammal.append(float(ar.text[1:]))

        # - a biztonsag kedveert ellenorzom, hogy nincs nulla, vagy negativ erteku ar-e a lista elejen.
        assert arak_szammal[0] > 0

        # - ellenorzom, hogy a kinyert arlista megegyezik-e ugyanezen lista novekvobe rendezett formajaval
        assert arak_szammal == sorted(arak_szammal)

    # Helyezzunk termekeket a kosarunkba, és ellenorizzuk le, hogy a kosar melletti ikon a termekek szamat mutatja-e.
    @allure.title('Termékek kosárba helyezése és a kosár számlálójának ellenőrzése')
    @allure.description('A teszteset célja annak ellenőrzése, hogy ha termékeket helyezünk a bevásárlókosárba, akkor a jobb fölső sarokban található kosáron a kosárba helyezett termékek számának megfelelő szám jelenik-e meg.')
    @allure.severity(allure.severity_level.NORMAL)
    @allure.tag('pozitív', 'kosár', 'termék')
    def test_shopping_cart_badge(self):
        # - bejelentkezek
        self.login(USER['standard'], USER['password'])

        # - megkeresem a listaban az elso harom termek Add to cart gombjat es raklikkelek. Ellenorzom, hogy a bevasarlokosar ikonon megjelenik-e a termekek darabszama.
        for i in range(1, 4):
            WebDriverWait(self.browser, 5).until(
                EC.element_to_be_clickable((By.XPATH, f'(//div[@class="pricebar"]/button)[{i}]'))).click()
            shopping_cart_badge_number = WebDriverWait(self.browser, 5).until(
            EC.visibility_of_element_located((By.XPATH, '//span[@data-test="shopping-cart-badge"]')))
            assert int(shopping_cart_badge_number.text) == i


    # Ellenőrizzük le, hogy minden ár dollárban van-e megadva.
    @allure.title('Valuta ellenőrzése')
    @allure.description('A teszteset célja annak ellenőrzése, hogy a honalpon a termékek ára mindenhol dollárban van-e megjelenítve.')
    @allure.severity(allure.severity_level.NORMAL)
    @allure.tag('pozitív', 'ár', 'valuta')
    def test_all_price_dollar(self):
        # - bejelentkezek
        self.login(USER['standard'], USER['password'])

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
    @allure.title('A termék képének ellenőrzése a főoldalon és a terméklapon.')
    @allure.description('A teszteset célja annak ellenőrzése, hogy a termék képe a főoldalon megegyezik-e a terméklapon szereplő képpel.')
    @allure.severity(allure.severity_level.NORMAL)
    @allure.tag('pozitív', 'kép', 'termék')
    def test_product_image_url(self):
        # - bejelentkezek
        self.login(USER['standard'], USER['password'])

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
        assert first_product_image_inside_url == first_product_image_inside_url


    # Ellenorizzuk le, hogy a hamburgermenuben az About gombra kattintva a swaglabs.com uj tab-on jelenik-e meg.
    # ELBUKÓ TESZTESET, mert nem nyit uj tabot az oldal betoltesekor, pedig uzleti szempontbol indokolt lenne, hogy a webshop oldala nyitva maradjon.
    @allure.title('About menüpont ellenőrzése')
    @allure.description('A tszteset célja annak ellenőrzése, hogy a hamburger menü, About menüpontjára kattintva a https://saucelabs.com/ URL új tab-on jelenik-e meg.')
    @allure.severity(allure.severity_level.NORMAL)
    @allure.tag('pozitív', 'about', 'új ablak')
    def test_about_on_new_tab(self):
        # - bejelentkezek
        self.login(USER['standard'], USER['password'])

        # - megnyitom a hamburgermenut
        self.hamburger_menu()

        # - az aktualisan nyitott ablakok szamat elmentem egy valtozoba (ez ertelemszeruen egy lesz)
        number_of_open_tabs = len(self.browser.window_handles)

        # - rakattintok az About gombra.
        WebDriverWait(self.browser, 5).until(EC.element_to_be_clickable((By.ID, 'about_sidebar_link'))).click()

        # - ellenorzom, hogy uj ablakban nyilt-e meg.
        assert len(self.browser.window_handles) == number_of_open_tabs + 1


    # Ellenorizzuk, hogy a fooldal aljan talalhato kozossegi media ikonok a megfelelo platform ceges oldalara mutatnak-e, es rakattintva uj tabon jelennek-e meg.
    @allure.title('A X - Twitter ikon tesztelése')
    @allure.description('A teszteset célja annak ellenőrzése, hogy a főoldal alján megjelenő közösségi média ikonok közül az X (Twitter) ikonra kattintva, új ablakban jelenik-e meg a cég oldala.')
    @allure.severity(allure.severity_level.NORMAL)
    @allure.tag('pozitív', 'X', 'Twitter', 'közösségi média', 'link')
    def test_x_twitter_icon(self):
        # - bejelentkezek
        self.login(USER['standard'], USER['password'])

        # - a social media ikonok teszteleset kiszerveztem egy fuggvenybe, mely parametere az elvart URL, valamint a lap aljan levo sm ikonok xpath-a.
        # visszateresi erteke true, ha uj tab-on nyilik meg a sm oldal es az uj tab url-je megegyezik az elvart url-el
        assert self.social_media_icon_check(twitter_url, twitter_xpath)

    @allure.title('A Facebook ikon tesztelése')
    @allure.description(
        'A teszteset célja annak ellenőrzése, hogy a főoldal alján megjelenő közösségi média ikonok közül a Facebook ikonra kattintva, új ablakban jelenik-e meg a cég oldala.')
    @allure.severity(allure.severity_level.NORMAL)
    @allure.tag('pozitív', 'Facebook', 'közösségi média', 'link')
    def test_facebook_icon(self):
        # - bejelentkezek
        self.login(USER['standard'], USER['password'])

        # - a social media ikonok teszteleset kiszerveztem egy fuggvenybe, mely parametere az elvart URL, valamint a lap aljan levo sm ikonok xpath-a.
        # visszateresi erteke true, ha uj tab-on nyilik meg a sm oldal es az uj tab url-je megegyezik az elvart url-el
        assert self.social_media_icon_check(facebook_url, facebook_xpath)

    @allure.title('A LinkedIn ikon tesztelése')
    @allure.description(
        'A teszteset célja annak ellenőrzése, hogy a főoldal alján megjelenő közösségi média ikonok közül a LinkedIn ikonra kattintva, új ablakban jelenik-e meg a cég oldala.')
    @allure.severity(allure.severity_level.NORMAL)
    @allure.tag('pozitív', 'LinkedIn', 'közösségi média', 'link')
    def test_linkedin_icon(self):
        # - bejelentkezek
        self.login(USER['standard'], USER['password'])

        # - a social media ikonok teszteleset kiszerveztem egy fuggvenybe, mely parametere az elvart URL, valamint a lap aljan levo sm ikonok xpath-a.
        # visszateresi erteke true, ha uj tab-on nyilik meg a sm oldal es az uj tab url-je megegyezik az elvart url-el
        assert self.social_media_icon_check(linkedin_url, linkedin_xpath)


    # Helyezzunk ket termeket a kosarba, majd ellenorizzuk, hogy ugyanazok a termekek jelennek-e meg a kosarban.
    def test_two_item_in_the_cart_comparison(self):
        # - bejelentkezek
        self.login(USER['standard'], USER['password'])

        # Ket elemet a bevasarlokocsihoz adok es a nevuket eltarolom egy listaban.
        item_add_to_cart_buttons = WebDriverWait(self.browser,5).until(EC.visibility_of_all_elements_located((By.XPATH, '//button[text()="Add to cart"]')))
        item_names = WebDriverWait(self.browser,5).until(EC.visibility_of_all_elements_located((By.XPATH, '//div[@data-test="inventory-item-name"]')))
        mainpage_item_names = []
        mainpage_item_names.append(item_names[0].text)
        mainpage_item_names.append(item_names[1].text)
        item_add_to_cart_buttons[0].click()
        item_add_to_cart_buttons[1].click()

        # Belepek a shopping cartba.
        shopping_cart = WebDriverWait(self.browser,5).until(EC.element_to_be_clickable((By.XPATH, '//div[@id="shopping_cart_container"]')))
        shopping_cart.click()

        # Kigyujtom a shopping cartban levo termekek neveit egy kulon listaba.
        shopping_cart_names = []
        item_names_cart = WebDriverWait(self.browser, 5).until(
            EC.visibility_of_all_elements_located((By.XPATH, '//div[@data-test="inventory-item-name"]')))
        shopping_cart_names.append(item_names_cart[0].text)
        shopping_cart_names.append(item_names_cart[1].text)

        # Ellenorzom, hogy a lista ket elemet tartalmaz-e.
        assert len(shopping_cart_names) == 2

        # Ellenorzom, hogy a ket lista sorrendezve azonos elemeket tartalmazza-e.
        assert sorted(mainpage_item_names) == sorted(shopping_cart_names)

        # Ellenorzom, hogy a ket lista megegyezik-e teljesen. Sorrendjuk is.
        assert mainpage_item_names == shopping_cart_names

# Szervezzuk ki az alabbi lepeseket kulon fuggvenybe:
# Helyezzunk ket termeket a kosarba, lepjunk a kosarra, majd kattintsunk ra a Checkout gombra
#   Maslojuk be a TESTADATokbol a firstname, lastname, postal_code adatokat a szoveges beviteli mezokbe és kattintsunk a Continue gombra.

    def test_two_items_checkout(self):
        # - bejelentkezek
        self.login(USER['standard'], USER['password'])

        logged_in_url = self.browser.current_url

        # Ket elemet a bevasarlokocsihoz adok es az arukat eltarolom egy listaban.
        item_add_to_cart_buttons = WebDriverWait(self.browser, 5).until(
            EC.visibility_of_all_elements_located((By.XPATH, '//button[text()="Add to cart"]')))
        item_prices = WebDriverWait(self.browser, 5).until(
            EC.visibility_of_all_elements_located((By.XPATH, '//div[@data-test="inventory-item-price"]')))
        mainpage_item_prices = []
        mainpage_item_prices.append(item_prices[0].text)
        mainpage_item_prices.append(item_prices[1].text)
        item_add_to_cart_buttons[0].click()
        item_add_to_cart_buttons[1].click()



        # Belepek a shopping cartba.
        shopping_cart = WebDriverWait(self.browser, 5).until(
            EC.element_to_be_clickable((By.XPATH, '//div[@id="shopping_cart_container"]')))
        shopping_cart.click()

        # Kigyujtom a shopping cartban levo termekek arait egy kulon listaba.
        shopping_cart_prices = []
        item_prices_cart = WebDriverWait(self.browser, 5).until(
            EC.visibility_of_all_elements_located((By.XPATH, '//div[@data-test="inventory-item-price"]')))
        shopping_cart_prices.append(item_prices_cart[0].text)
        shopping_cart_prices.append(item_prices_cart[1].text)


        # Ellenorzom, hogy a lista ket elemet tartalmaz-e.
        assert len(shopping_cart_prices) == 2

        # Ellenorzom, hogy a ket lista sorrendezve azonos elemeket tartalmazza-e.
        assert sorted(mainpage_item_prices) == sorted(shopping_cart_prices)

        # Ellenorzom, hogy a ket lista megegyezik-e teljesen. Sorrendjuk is.
        assert mainpage_item_prices == shopping_cart_prices

        # Rakattintok a checkout gombra
        WebDriverWait(self.browser,5).until(EC.element_to_be_clickable((By.NAME, 'checkout'))).click()

        input_firstname = WebDriverWait(self.browser,5).until(EC.visibility_of_element_located((By.ID, 'first-name')))
        input_firstname.send_keys(standard_user['first_name'])

        input_lastname = WebDriverWait(self.browser, 5).until(EC.visibility_of_element_located((By.ID, 'last-name')))
        input_lastname.send_keys(standard_user['last_name'])

        input_postal_code = WebDriverWait(self.browser, 5).until(EC.visibility_of_element_located((By.ID, 'postal-code')))
        input_postal_code.send_keys(standard_user['postal_code'])

        button_continue = WebDriverWait(self.browser,5).until(EC.element_to_be_clickable((By.ID, 'continue')))
        button_continue.click()

        checkout_item_prices = WebDriverWait(self.browser,5).until(EC.visibility_of_all_elements_located((By.XPATH, '//div[@data-test="inventory-item-price"]')))
        checkout_prices_list = []
        checkout_prices_list.append(checkout_item_prices[0].text)
        checkout_prices_list.append(checkout_item_prices[1].text)
        # print(checkout_prices_list)

        # Ellenorzom, hogy a lista ket elemet tartalmaz-e.
        assert len(checkout_prices_list) == 2

        # Ellenorzom, hogy a ket lista sorrendezve azonos elemeket tartalmazza-e.
        assert sorted(mainpage_item_prices) == sorted(checkout_prices_list)

        # Ellenorzom, hogy a ket lista megegyezik-e teljesen. Sorrendjuk is.
        assert mainpage_item_prices == checkout_prices_list

        # Szamma alakitom az arakat tartalmazo listat.
        numeric_price_list = []
        for price_string in checkout_prices_list:
            numeric_price_list.append(float(price_string[1:]))
        # print(numeric_price_list)

        # Kigyujtom kulon valtozokba az Item total, a Tax es a Total ertekeit, hogy matematikailag ellenorizhessem az ertekeket.
        item_total = WebDriverWait(self.browser,5).until(EC.visibility_of_element_located((By.XPATH, '//div[@data-test="subtotal-label"]')))
        item_total_numeric = float((item_total.text)[13:])

        # Leellenorzom, hogy az itemtotal erteke megegyezik-e az ket termek ertekenek az osszegevel.
        assert  item_total_numeric == numeric_price_list[0] + numeric_price_list[1]

        # Kimentem a Tax erteket egy valtozoba es szamma konvertalom.
        tax = WebDriverWait(self.browser, 5).until(
            EC.visibility_of_element_located((By.XPATH, '//div[@data-test="tax-label"]')))
        tax_numeric = float((tax.text)[6:])

        # Kimentem a vegosszeget egy valtozoba es szamma konvertalom.
        total = WebDriverWait(self.browser,5).until(EC.visibility_of_element_located((By.XPATH, '//div[@data-test="total-label"]')))
        total_numeric = float((total.text)[8:])

        # Ellenorzom, hogy a vegosszeg az a termekek es az ado osszegevel egyenlo-e.
        assert item_total_numeric + tax_numeric == total_numeric

        # Rakattintok a finish gombra.
        WebDriverWait(self.browser,5).until(EC.element_to_be_clickable((By.ID, 'finish'))).click()

        # Ellenorzom, hogy az ablakban megjelenik-e a megrendelest megkoszono uzenet,
        thank_message = WebDriverWait(self.browser,5).until(EC.visibility_of_element_located((By.XPATH, '//h2[@data-test="complete-header"]')))
        assert thank_message.text == 'Thank you for your order!'

        # Rakattintok a gombra, ami visszavezet a fooldalra
        WebDriverWait(self.browser,5).until(EC.element_to_be_clickable((By.NAME, 'back-to-products'))).click()

        # Lekerem az aktualis url-t es osszehasonlitom a belepes utan eltarolt logged_in_url-lel. Ezzel ellenorzom, hogy valoban a fooldalra jutottunk-e.
        actual_url = self.browser.current_url
        assert actual_url == logged_in_url



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
