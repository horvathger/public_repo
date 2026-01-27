A csatolt állományok az alábbi linken elérhető tesztoldal alapvető funkcióit ellenőrzik.

https://high-flyer.hu/selenium/kitchensink.html


A 12 db tesztesethez Pytestet, a webböngésző automatizáláshoz Seleniumot, a riportkészítéshez pedig Allure-t használtam.

Az allure használatához a parancssorból az 'allure serve' parancsot kell lefuttatni abban a mappában, amelyben a test_kitchensink.py állomány és az Allure-results mappa található.
A könnyebb meg megtekinthetőség érdekében mellékeltem képernyőfotókat az allure riportból.
A teszt és a riport generálás újrafuttatható az alábbi paranccsal:
pytest --alluredir=./allure-results


A production_table_export.csv-t az utolso teszteset hozza létre, ebbe olvassa ki a weboldalon található táblázat tartalmát.