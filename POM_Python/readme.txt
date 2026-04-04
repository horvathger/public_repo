Ezzel a paranccsal lehet a jelentést generálni a public_repo mappában:
pytest .\POM_Python\ --alluredir=.\POM_Python\allure-results


Ezzel a paranccsal lehet a jelentést megnyitni a \POM_Python\ mappában:
allure serve

Ha a Utils\create_driver.py fájlban az alábbi sort kikommentelve,
a böngészőablakok megjelennek a tesztek futtatása közben:
options.add_argument("--headless=new")

