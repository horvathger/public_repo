'''
Automatizáljuk le a játék kitöltését - az egész folyamat egy tesztesetként jelenjen meg
A feladatot pytest, class, selenium és assert(ek) használatával oldjuk meg.
https://techstepacademy.com/trial-of-the-stones

Figyeljünk arra, hogy a szkriptünk az oldalról olvasson be MINDENT!
(Pl. a gazdagabb kereskedő meghatározásához az oldalról olvassuk be az egyes kereskedők nevét és vagyonát,
az értékeket hasonlítsuk össze és a gazdagabb kereskedő nevét írja be a szkript a megfelelő inputmezőbe)
'''
import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select

URL = "https://techstepacademy.com/trial-of-the-stones"

class TestTOS(object):
    # a setup methoddal letrehozom a webdrivert es megadom neki a szukseges parametereket.
    def setup_method(self):
        options = Options()
        options.add_experimental_option("detach", True)
        self.browser = webdriver.Chrome(options=options)
        self.browser.maximize_window()
        self.browser.get(URL)

    # a teardown method minden teszteset futtatasanak a vegen lefut es bezarja a bongeszoablakot.
    def teardown_method(self):
        self.browser.quit()

    def test_trial_of_stones(self):
        # az "oldalrol olvasson be MINDENT!" feltetel miatt a "bamboo" es a "rock" szavakat is az oldalrol kerestem ki.
        # a "bamboo" elem megtalalhato a DOM-ban, csak "display:none' a style-ja, ezert nem latszik.
        maybe_bamboo_element = WebDriverWait(self.browser,5).until(EC.presence_of_element_located((By.XPATH, '//div[@id="passwordBanner"]/h4')))

        # a "rock" szo csak egy beagyazott JavaScriptben talahato meg ezert a script elemnek ki kell nyerni a szoveget, majd azt a "riddle.value.toLowerCase() == " string utani reszrol ki kell vagni 4 karakter hosszan.
        maybe_rock_element = WebDriverWait(self.browser,5).until(EC.presence_of_element_located((By.XPATH, '//div[@id="block-05ea3afedc551e378bdc"]//script')))
        maybe_rock_content = maybe_rock_element.get_attribute("innerHTML")
        start_of_rock = ((maybe_rock_content.index('riddle.value.toLowerCase() == "')) + len(
            'riddle.value.toLowerCase() == "'))
        the_four_letter_word = maybe_rock_content[start_of_rock: (start_of_rock + 4)]

        # az input mezobe be kell masolni a "rock" kifejezest, amit fentebb a the_four_letter_word valtozoban eltaroltunk, majd ra kel klikkelni az "Answer" gombra
        input_four_letter_stone = WebDriverWait(self.browser,5).until(EC.element_to_be_clickable((By.XPATH, '//input[@id="r1Input"]')))
        input_four_letter_stone.send_keys(the_four_letter_word)
        self.browser.find_element(By.ID, 'r1Btn').click()

        # le kell kerni a program valaszat es ossze kell hasonlitani a maybe_bamboo_element szovegevel
        answer_of_stone = WebDriverWait(self.browser,5).until(EC.visibility_of_element_located((By.XPATH, '//div[@id="passwordBanner"]/h4')))
        assert answer_of_stone.text == maybe_bamboo_element.text

        # a password input mezojebe be kell masolni az iment megkapott es az answer_of_stone valtozoban eltarolt erteket (bamboo), majd ra kell kattintani az "Answer"gombra.
        input_password = WebDriverWait(self.browser,5).until(EC.element_to_be_clickable((By.XPATH, '//input[@id="r2Input"]')))
        input_password.send_keys(answer_of_stone.text)
        self.browser.find_element(By.ID, 'r2Butn').click()

        # a kapott valaszt osszehasonlitom az elvarttal
        answer_of_password = WebDriverWait(self.browser,5).until(EC.visibility_of_element_located((By.XPATH,'//div[@id="successBanner1"]/h4')))
        assert answer_of_password.text == 'Success!'

        # lekerem a ket kereskedo vagyonara vonatkozo webelemeket
        merchant1_wealth = WebDriverWait(self.browser,5).until(EC.visibility_of_element_located((By.XPATH, '(//div/span)[1]/following-sibling::p')))

        merchant2_wealth = WebDriverWait(self.browser, 5).until(
            EC.visibility_of_element_located((By.XPATH, '(//div/span)[2]/following-sibling::p')))

        # ha az elso kereskedo vagyona nagyobb, mint a masodike, akkor az answer_of_richest valtozoban elmentem az elso kereskedo nevet, ha nem, akkor a masodikat.
        # a biztonsag kedveert az egeszet berktam egy try-except blokkba, arra az esetre, ha a ket kereskedo vagyona egyenlo lenne.
        try:
            if int(merchant1_wealth.text) > int(merchant2_wealth.text):
                answer_of_richest = self.browser.find_element(By.XPATH, '(//div/span)[1]/b').text
            elif int(merchant1_wealth.text) < int(merchant2_wealth.text):
                answer_of_richest = self.browser.find_element(By.XPATH, '(//div/span)[2]/b').text
        except ValueError as ve:
            print('A ket kereskedo vagyona egyenlo')

        # az input mezobe bekuldom a gazdagabbik kereskedo nevet es raklikkelek az "Answer" gombra
        input_richest = self.browser.find_element(By.ID, 'r3Input')
        input_richest.send_keys(answer_of_richest)
        self.browser.find_element(By.ID, 'r3Butn').click()

        # ellenorzom, hogy a kapott valasz megegyezik-e az elvarttal.
        answer_of_password = WebDriverWait(self.browser,5).until(EC.visibility_of_element_located((By.XPATH,'//div[@id="successBanner2"]/h4')))
        assert answer_of_password.text == 'Success!'

        # megkeresem a "Check Answer" gombot, es raklikkelek, majd megvizsgalom a kiirt valaszt, hogy megegyezik-e az elvarttal.
        WebDriverWait(self.browser,5).until(EC.element_to_be_clickable((By.XPATH, '//button[@id="checkButn"]'))).click()
        check_answer_message = WebDriverWait(self.browser,5).until(EC.visibility_of_element_located((By.XPATH, '//div[@id="trialCompleteBanner"]/h4'))).text
        assert check_answer_message == 'Trial Complete'

        time.sleep(2)

