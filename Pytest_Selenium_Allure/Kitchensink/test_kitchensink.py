import csv

import allure
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait

URL = 'https://high-flyer.hu/selenium/kitchensink.html'

TESTDATA = {'Name': 'Aladár', 'string': 'Ez egy teszt string.'}


# ez a fuggveny a radio buttonok allapotanak ellenorzesere szolgal.
def radio_button_check(self):
    radio_button_bmw = WebDriverWait(self.browser, 5).until(EC.element_to_be_clickable((By.ID, 'bmwradio')))
    radio_button_benz = WebDriverWait(self.browser, 5).until(
        EC.element_to_be_clickable((By.XPATH, '//input[@id="benzradio"]')))
    radio_button_honda = WebDriverWait(self.browser, 5).until(
        EC.element_to_be_clickable((By.XPATH, '(//input[@type="radio"])[3]')))
    result = ''
    if not radio_button_bmw.is_selected() and not radio_button_benz.is_selected() and not radio_button_honda.is_selected():
        result = 'none_of_them'
    if radio_button_bmw.is_selected() and not radio_button_benz.is_selected() and not radio_button_honda.is_selected():
        result = 'bmw'
    if not radio_button_bmw.is_selected() and radio_button_benz.is_selected() and not radio_button_honda.is_selected():
        result = 'benz'
    if not radio_button_bmw.is_selected() and not radio_button_benz.is_selected() and radio_button_honda.is_selected():
        result = 'honda'
    return result


# Ez a fuggveny ellenorzi, hogy a checkboxok be vannak-e pipalva.
def checkbox_select_check(self):
    checkbox_bmw = WebDriverWait(self.browser, 5).until(
        EC.element_to_be_clickable((By.XPATH, '//input[@id="bmwcheck"]')))
    checkbox_benz = WebDriverWait(self.browser, 5).until(EC.element_to_be_clickable((By.ID, 'benzcheck')))
    checkbox_honda = WebDriverWait(self.browser, 5).until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#hondacheck')))
    result = ''
    if not checkbox_bmw.is_selected() and not checkbox_benz.is_selected() and not checkbox_honda.is_selected():
        result = 'none_of_them_are_selected'

    if checkbox_bmw.is_selected() and not checkbox_benz.is_selected() and not checkbox_honda.is_selected():
        result = 'bmw_is_selected'
    if not checkbox_bmw.is_selected() and checkbox_benz.is_selected() and not checkbox_honda.is_selected():
        result = 'benz_is_selected'
    if not checkbox_bmw.is_selected() and not checkbox_benz.is_selected() and checkbox_honda.is_selected():
        result = 'honda_is_selected'

    if checkbox_bmw.is_selected() and checkbox_benz.is_selected() and not checkbox_honda.is_selected():
        result = 'bmw_and_benz_are_selected'
    if checkbox_bmw.is_selected() and not checkbox_benz.is_selected() and checkbox_honda.is_selected():
        result = 'bmw_and_honda_are_selected'
    if not checkbox_bmw.is_selected() and checkbox_benz.is_selected() and checkbox_honda.is_selected():
        result = 'honda_and_benz_are_selected'

    if checkbox_bmw.is_selected() and checkbox_benz.is_selected() and checkbox_honda.is_selected():
        result = 'all_of_them_selected'

    return result


# Ez a fugveny osszeszamolja a DOM-ban talalhato elrejtett uzeneteket.
def hidden_message_pieces_check(self):
    hidden_message = WebDriverWait(self.browser, 5).until(
        EC.presence_of_all_elements_located((By.XPATH, '//input[@style="display: none;"]')))
    return len(hidden_message)


# Az allure riport formazasahoz dekoratorokat hasznaltam.
@allure.epic('A Kitchensink oldal tesztelése')
@allure.suite('Smoke tesztek')
class TestKitchensink(object):

    # A setup method minden teszteset elott lefut es letrehozza a webdrivert.
    def setup_method(self):
        options = Options()
        options.add_experimental_option("detach", True)
        self.browser = webdriver.Chrome(options=options)
        self.browser.maximize_window()
        self.browser.get(URL)

    # A teardown method minden teszteset vegen lefut es bezarja a bongeszoablakot.
    def teardown_method(self):
        self.browser.quit()

    @allure.title('Rádiógombok ellenőrzése')
    @allure.description('A teszteset célja a rádiógombok működésének ellemőrzése.')
    @allure.severity(allure.severity_level.NORMAL)
    @allure.tag('pozitív', 'radio button', 'rádiógomb')
    def test_radio_buttons(self):

        # Kulon valtozokba kimentem a radio buttonokat.
        radio_button_bmw = WebDriverWait(self.browser, 5).until(EC.element_to_be_clickable((By.ID, 'bmwradio')))
        radio_button_benz = WebDriverWait(self.browser, 5).until(
            EC.element_to_be_clickable((By.XPATH, '//input[@id="benzradio"]')))
        radio_button_honda = WebDriverWait(self.browser, 5).until(
            EC.element_to_be_clickable((By.XPATH, '(//input[@type="radio"])[3]')))

        # A kiszervezett fuggveny segitsegevel ellenorzom a radio buttonok kezdeti allapotat.
        assert radio_button_check(self) == 'none_of_them'

        # Beklikkelem egyesevel a gombokat es asserttel ellenorzom a gombok allapotat minden modositas utan.
        radio_button_bmw.click()
        assert radio_button_check(self) == 'bmw'

        radio_button_benz.click()
        assert radio_button_check(self) == 'benz'

        radio_button_honda.click()
        assert radio_button_check(self) == 'honda'

    @allure.title('Legördülő menüből egyszeres kiválasztás ellenőrzése')
    @allure.description('A teszteset célja az egyszeres kiválaszású legördülő menü működésének ellenőrzése.')
    @allure.severity(allure.severity_level.NORMAL)
    @allure.tag('pozitív', 'select', 'single-select', 'egyszeres kiválasztás', 'legördülő menü')
    def test_single_select_from_list(self):
        # Az egyszeres kivalasztasu legordulo listat elmentem egy valtozoba
        select_cars = Select(self.browser.find_element(By.ID, 'carselect'))

        # Egyesevel kivalasztom az elemeket es asserttel ellenorzom az allapotukat. Minddharom esetben kulonbozo modszert hasznaltam az elemek kivalasztasahoz.
        select_cars.select_by_visible_text('Honda')
        assert select_cars.first_selected_option.text == 'Honda'

        select_cars.select_by_index(1)
        assert select_cars.first_selected_option.text == 'Benz'

        select_cars.select_by_value('bmw')
        assert select_cars.first_selected_option.text == 'BMW'

    @allure.title('Legördülő menüből többszörös kiválasztás ellenőrzése')
    @allure.description('A teszteset célja a többszörös kiválaszású legördülő menü működésének ellenőrzése.')
    @allure.severity(allure.severity_level.NORMAL)
    @allure.tag('pozitív', 'select', 'multiple-select', 'többszörös kiválasztás', 'legördülő menü')
    def test_multiple_select_from_list(self):
        # Ellenorzom a tobbszoros kivalasztasu legordulo lista kezdeti allapotat oly modon, hogy megszamolom a kivalasztott elemek szamat.
        multiselect_fruits = Select(self.browser.find_element(By.XPATH, '//select[@id="multiple-select-example"]'))
        assert len(multiselect_fruits.all_selected_options) == 0

        # Kulonbozo modszerekkel kijelolom a lista mindharom elemet es asserttel ellenorzom a kijeloles megtortentet.
        multiselect_fruits.select_by_value('apple')
        multiselect_fruits.select_by_index(1)
        multiselect_fruits.select_by_visible_text('Peach')
        assert len(multiselect_fruits.all_selected_options) == 3

        # Torlom a kijelolest az egyes indexu (masodik) elemnel es ellenorzom a kijelolt elemek szamat.
        multiselect_fruits.deselect_by_index(1)
        assert len(multiselect_fruits.all_selected_options) == 2

        # Torlom az 'apple' erteku elem kijeloleset es ellenorzom a kijelolve maradt elemek szamat.
        multiselect_fruits.deselect_by_value('apple')
        assert len(multiselect_fruits.all_selected_options) == 1

        # Torlom a 'Peach' megjeleno szovegu listaelem kijeloleset es ellenorzom a lista hosszat.
        multiselect_fruits.deselect_by_visible_text('Peach')
        assert len(multiselect_fruits.all_selected_options) == 0

    @allure.title('A checkboxok ellenőrzése')
    @allure.description('A teszteset célja a checkboxok működésének ellenőrzése.')
    @allure.severity(allure.severity_level.NORMAL)
    @allure.tag('pozitív', 'checkbox')
    def test_checkboxes(self):
        # A checkbox webelementeket egyenkent elmentem egy-egy kulon valtozoba.
        checkbox_bmw = WebDriverWait(self.browser, 5).until(
            EC.element_to_be_clickable((By.XPATH, '//input[@id="bmwcheck"]')))
        checkbox_benz = WebDriverWait(self.browser, 5).until(EC.element_to_be_clickable((By.ID, 'benzcheck')))
        checkbox_honda = WebDriverWait(self.browser, 5).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, '#hondacheck')))

        # A kiszervezett fuggvennyel leellenorzom, hogy egy se legyen kijelolve, majd egyesevel megklikkelem a checkboxokat es asserttel ellenorzom a kijeloles sikeret.
        assert checkbox_select_check(self) == 'none_of_them_are_selected'
        checkbox_bmw.click()
        assert checkbox_select_check(self) == 'bmw_is_selected'
        checkbox_benz.click()
        assert checkbox_select_check(self) == 'bmw_and_benz_are_selected'
        checkbox_honda.click()
        assert checkbox_select_check(self) == 'all_of_them_selected'

        # Vegig iteralok a checkboxokon es egyesevel rakattintok mindre, majd ellenorzom hogy torlodtek-e a kijelolesek.
        all_check_box = self.browser.find_elements(By.XPATH, '//input[@type="checkbox"]')
        for checkbox in all_check_box:
            checkbox.click()
        assert checkbox_select_check(self) == 'none_of_them_are_selected'

    @allure.title('Új ablak nyitásának az ellenőrzése')
    @allure.description('A teszteset célja az új ablak nyitás funkció ellenőrzése.')
    @allure.severity(allure.severity_level.NORMAL)
    @allure.tag('pozitív', 'új ablak nyitása', 'open new window', 'ablak', 'window')
    def test_open_window(self):
        # Megkeresem es rakattintok az Open Window gombra.
        self.browser.find_element(By.ID, 'openwindow').click()

        # Az eredeti ablak azonositojat elmentem egy valtozoba es ellenorzom, hogy az URL a kitchensink oldala-e.
        # Ezt kovetoen a masik ablak azonositojat is elmentem egy valtozoba majd atnavigalok a masik ablakba es kiolvasom az aktualis URL-t es ellenorzom, hogy az a met.hu-e.
        eredeti_ablak = self.browser.window_handles[0]
        assert self.browser.current_url == 'https://high-flyer.hu/selenium/kitchensink.html'
        met_hu_ablak = self.browser.window_handles[1]
        self.browser.switch_to.window(met_hu_ablak)
        assert self.browser.current_url == 'https://met.hu/'

        # Bezarom a met.hu ablakot, visszavaltok az eredeti ablakra es ellenorzom, hogy a kitchensink oldala-e az aktualis oldal.
        self.browser.close()
        self.browser.switch_to.window(eredeti_ablak)
        assert self.browser.current_url == 'https://high-flyer.hu/selenium/kitchensink.html'

    @allure.title('Új lapfül nyitásának az ellenőrzése')
    @allure.description('A teszteset célja az új lapfül nyitás funkció ellenőrzése.')
    @allure.severity(allure.severity_level.NORMAL)
    @allure.tag('pozitív', 'új lapfül nyitása', 'open new tab', 'lapfül', 'tab')
    def test_open_tab(self):

        # Megkeresem es rakattintok az Open Tab gombra.
        self.browser.find_element(By.ID, 'opentab').click()

        # Elmentem a ket ablak azonositóit egy-egy valtozoba es ellenorzom, hogy az aktualis ablak a kitchensink-e
        eredeti_ablak = self.browser.window_handles[0]
        goggle_ablak = self.browser.window_handles[1]
        assert self.browser.current_url == 'https://high-flyer.hu/selenium/kitchensink.html'

        # Atvaltok a Google ablakra es ellenorzom az URL-t, majd megkattintom a gmail linket es belekattintok az input mezobe.
        self.browser.switch_to.window(goggle_ablak)
        assert self.browser.current_url == 'https://www.google.com/'
        WebDriverWait(self.browser, 5).until(EC.element_to_be_clickable((By.XPATH, '//button[@id="W0wltc"]'))).click()
        anchor_to_gmail = WebDriverWait(self.browser, 5).until(
            EC.element_to_be_clickable((By.XPATH, '//a[@href="https://mail.google.com/mail/&ogbl"]')))
        anchor_to_gmail.click()
        WebDriverWait(self.browser, 5).until(EC.element_to_be_clickable((By.XPATH, '//input[@id="identifierId"]')))

        # Ellenorzom, hogy az aktualis URL tartalmazza-e a 'https://accounts.google.com/' reszt, majd bezarom az ablakot es visszaterek az eredeti ablakra, amit szinten ellenorzok asserttel.
        assert 'https://accounts.google.com/' in self.browser.current_url
        self.browser.close()
        self.browser.switch_to.window(eredeti_ablak)
        assert self.browser.current_url == 'https://high-flyer.hu/selenium/kitchensink.html'

    @allure.title('Az alert ablak kezelésének az ellenőrzése')
    @allure.description('A teszteset célja a felugró alert ablak funkció ellenőrzése.')
    @allure.severity(allure.severity_level.NORMAL)
    @allure.tag('pozitív', 'alert')
    def test_alert(self):
        # Kimentem egy valtozoba az input mezo webelemet es beleirom a tesztadatok dictionary 'Name' kulcsahoz tartozo erteket.
        input_name = WebDriverWait(self.browser, 5).until(EC.element_to_be_clickable((By.XPATH, '//input[@id="name"]')))
        input_name.send_keys(TESTDATA['Name'])

        # Rakattintok az 'Alert' gombra, atvaltok az alert ablakra, majd asserttel ellenorzom az ablak szoveget, vegul bezarom az ablakot.
        WebDriverWait(self.browser, 5).until(EC.element_to_be_clickable((By.XPATH, '//input[@id="alertbtn"]'))).click()
        new_alert = self.browser.switch_to.alert
        assert new_alert.text == f"Hello {TESTDATA['Name']}, share this practice page and share your knowledge"
        new_alert.accept()

    @allure.title('A confirm ablak kezelésének az ellenőrzése')
    @allure.description('A teszteset célja a felugró confirm ablak funkció ellenőrzése.')
    @allure.severity(allure.severity_level.NORMAL)
    @allure.tag('pozitív', 'confirm')
    def test_confirm(self):
        # Kimentem egy valtozoba az input mezo webelemet es beleirom a tesztadatok dictionary 'Name' kulcsahoz tartozo erteket.
        input_name = WebDriverWait(self.browser, 5).until(EC.element_to_be_clickable((By.XPATH, '//input[@id="name"]')))
        input_name.send_keys(TESTDATA['Name'])

        # Rakattintok az 'Confirm' gombra, atvaltok az confirm ablakra, majd asserttel ellenorzom az ablak szoveget, vegul bezarom az ablakot.
        WebDriverWait(self.browser, 5).until(
            EC.element_to_be_clickable((By.XPATH, '//input[@id="confirmbtn"]'))).click()
        new_alert = self.browser.switch_to.alert
        assert new_alert.text == f"Hello {TESTDATA['Name']}, Are you sure you want to confirm?"
        new_confirm = self.browser.switch_to.alert
        new_confirm.dismiss()

    @allure.title('A mouse hover menü megjelenésének az ellenőrzése')
    @allure.description(
        'A teszteset célja annak ellenőrzése, hogy ha az egeret a "Mouse Hover" felirat fölé visszük, akkor tényleg megjelenik-e a menü.')
    @allure.severity(allure.severity_level.NORMAL)
    @allure.tag('pozitív', 'mouse hover')
    def test_mouse_hover_menu(self):
        # A webelemet elmentem egy valtozoba.
        button_mouse_hover = WebDriverWait(self.browser, 5).until(
            EC.element_to_be_clickable((By.XPATH, '//button[@id="mousehover"]')))

        # Felveszek egy valtozot, ami az oldal URL-et kiegeszeti az assertalashoz.
        elvart_url = URL + "#top"

        # Action chains-szel szimulalom, mintha az egermutatot a gomb fole vinnem.
        actions = ActionChains(self.browser)
        actions.move_to_element(button_mouse_hover)
        actions.perform()

        # Rakattintok a megjeleno linkre, majd ellenorzom, hogy az megegyezik-e az elvarttal.
        anchor_top = WebDriverWait(self.browser, 5).until(EC.element_to_be_clickable((By.XPATH, '//a[@href="#top"]')))
        anchor_top.click()
        uj_url = self.browser.current_url

        assert elvart_url == uj_url

    @allure.title('A láthatatlan gomb kattinthatóságának az ellenőrzése')
    @allure.description(
        'A teszteset célja annak ellenőrzése, hogy az oldalon elhelyezett láthatatlan gomb valóban nem kattinható-e meg.')
    @allure.severity(allure.severity_level.NORMAL)
    @allure.tag('pozitív', 'hidden button', 'láthatatlan gomb')
    def test_hidden_button(self):
        # Eloszor felveszek egy logikai valtozot, majd try-except blokkal megvizsgalom, hogy megkattinthato-e a lathatatlan gomb.
        # Ha nem, akkor False-ra allitom a logikai valtozo erteket.
        hidden_button_is_clickable = True
        try:
            WebDriverWait(self.browser, 5).until(
                EC.presence_of_element_located((By.XPATH, '//input[@value="Gone"]'))).click()
        except Exception as err:
            hidden_button_is_clickable = False
        assert hidden_button_is_clickable == False

    @allure.title('A beviteli mezőt eltüntető és megjelenítő gombok ellenőrzése')
    @allure.description(
        'A teszteset célja annak ellenőrzése, hogy a beviteli mezőbe rögzített adat valóban eltűnik-e a "Hide" gomb megnyomására és előtűnik-e ismét a "Show"-gomb megnyomására.')
    @allure.severity(allure.severity_level.NORMAL)
    @allure.tag('pozitív', 'hide button', 'show button')
    def test_show_and_hide(self):

        # Az input mezo webelemet elmentem egy valtozoba, majd beletoltom a testadatokat tartalmazo dictionary 'string' kulcsahoz tartalmazo erteket.
        input_hide_and_show = WebDriverWait(self.browser, 5).until(
            EC.element_to_be_clickable((By.XPATH, '//input[@id="displayed-text"]')))
        input_hide_and_show.send_keys(TESTDATA['string'])

        # Egy kiszervezett fuggvenyel ellenorzom, hogy hany rejtett elem van a DOM-ban. (A Visibility Example resznel van egy.)
        assert hidden_message_pieces_check(self) == 1

        # Rakattintok a Hide gombra, es ellenorzom, hogy egyel nott-e a DOM-ban a rejtett elemek szama.
        button_hide_text = WebDriverWait(self.browser, 5).until(EC.element_to_be_clickable((By.ID, 'hide-textbox')))
        button_hide_text.click()

        assert hidden_message_pieces_check(self) == 2

        # Rakattintok a Show gombra es ellenorzom, hogy egyel csokkent-e a rejtett elemek szama a DOM-ban.
        button_show = WebDriverWait(self.browser, 5).until(EC.element_to_be_clickable((By.ID, 'show-textbox')))
        button_show.click()

        assert hidden_message_pieces_check(self) == 1

    # Mivel nem volt jobb otletem, hogy mit lehet egy statikus tablazaton ellenorizni, ezert megprobaltam kimenteni a tablazat adatait egy csv-be,
    # majd onnan visszaolvasva ellenorizni a tartalmat.

    @allure.title('Táblázat kimentésének és ismételt beolvasásának ellenőrzése')
    @allure.description(
        'A teszteset célja annak ellenőrzése, hogy az oldalon található táblázat adatai kimenthetők-e egy külső csv állományba, illetve visszaolvasásukat követően megegyeznek-e az oldalon található adatokkal.')
    @allure.severity(allure.severity_level.NORMAL)
    @allure.tag('pozitív', 'table', 'táblázat', 'csv write', 'csv read')
    def test_table_to_csv(self):
        # A tablat tartalmazo webelemet kimentem egy valtozoba.
        product_table = self.browser.find_element(By.ID, 'product')

        # A tablaban levo tr elemeket kimentem egy webelem-listaba
        tr_s = product_table.find_elements(By.TAG_NAME, 'tr')

        # A 0. indexu tr elemben talalhatok a th elemek (tablazat fejresze), melyeket egyesevel hozzafuzok a header_text listahoz.
        header_row = tr_s[0]
        header_text = []
        th_s = header_row.find_elements(By.TAG_NAME, 'th')
        for th in th_s:
            header_text.append(th.text)

        # A tobbi tr a tablazat adatsorait tatalmazza ezert azokat soronkent kulon listaba gyujtom, majd a soronkenti listakat egy masik gyujtolistaba fuzom.
        table_data_rows = tr_s[1:]
        table_data_text = []
        for tr in table_data_rows:
            row_text = []
            td_s = tr.find_elements(By.TAG_NAME, 'td')
            for td in td_s:
                row_text.append(td.text)
            table_data_text.append(row_text)

        # Kiirom csv fajlba a listak listajat
        with open('production_table_export.csv', 'w', encoding='UTF-8') as csvfile:
            csvwriter = csv.writer(csvfile, delimiter=';', lineterminator="\n")
            csvwriter.writerow(header_text)
            csvwriter.writerows(table_data_text)

        # Beolvasom az adatokat a fajlbol
        with open('production_table_export.csv', 'r', encoding='UTF-8') as csvfile_import:
            content = csv.DictReader(csvfile_import, delimiter=';', lineterminator='\n')
            import_list_of_the_tablerows = []
            for row in content:
                import_list_of_the_tablerows.append(row['Author'])
                import_list_of_the_tablerows.append(row['Course'])
                import_list_of_the_tablerows.append(row['Price'])
                import_list_of_the_tablerows.append(row['Actions'])

        # Kigyujtom a td elemeket a DOM-bol.
        table_content = self.browser.find_elements(By.TAG_NAME, 'td')
        list_of_th_tds = []
        for table_data in table_content:
            list_of_th_tds.append(table_data.text)

        # Osszehasonlítom a ket listat.
        assert import_list_of_the_tablerows == list_of_th_tds
