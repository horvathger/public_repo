"""
Automatizáljuk a játékot, majd a végén ellenőrizzük a 'You Rock!' felirat megjelenését
A feladatot pytest, class, selenium és assert(ek) használatával oldjuk meg.
https://high-flyer.hu/selenium/memory-game.html

"""
import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

URL = 'https://high-flyer.hu/selenium/memory-game.html'


class TestMemoriaJatek(object):

    def setup_method(self):
        options = Options()
        options.add_experimental_option("detach", True)
        self.browser = webdriver.Chrome(options=options)
        self.browser.maximize_window()
        self.browser.get(URL)

    def teardown_method(self):
        pass #self.browser.quit()

    def test_memoria_jatek(self):
        cards = WebDriverWait(self.browser, 5).until(
            EC.visibility_of_all_elements_located((By.XPATH, '//div[@data-id]')))
        number_of_cards = len(cards)  # kigyujtottem a kartyakat es megszamoltam hany darab.

        # osszesen 24 kartya van a kartyakat azonosito data-id 1-12 kozott valtozik es ugyanaz a data-id-ja a kartyaparoknak.

        for card_id in range(1, (
        int(number_of_cards / 2 + 1))):  # a cardID max értéke az összes kártya db számnak a fele, mivel minden kártyának pontosan egy párja van
            pair_of_cards = self.browser.find_elements(By.XPATH,
                                                       f'//div[@data-id="{card_id}"]')  # card-id alapjan iteracionkent legyujtom a kartyaparokat.
            pair_of_cards[0].click()  # a kartyapar-webelementeket tartalmazo lista mindket elemere rakattintok.
            pair_of_cards[1].click()

        you_rock = WebDriverWait(self.browser, 5).until(EC.visibility_of_element_located((By.XPATH, '//div/h2')))
        assert you_rock.text == 'You Rock!'
        time.sleep(1)  # ez a sleep arra jó, hogy látszódjon az eredmény ablak, mielott bezarodik.
