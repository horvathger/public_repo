Ezzel a paranccsal lehet a jelentést generálni a public_repo mappában:
pytest .\POM_Python\ --alluredir=.\POM_Python\allure-results


Ezzel a paranccsal lehet a jelentést megnyitni a \POM_Python\ mappában:
allure serve

Ha a Utils\create_driver.py fájlban az alábbi sort kikommentelve,
a böngészőablakok megjelennek a tesztek futtatása közben:
options.add_argument("--headless=new")

Ha a tesztállományokban a Test Classok elején a teardown methodokat kikommenteljük és "pass"-t írunk be,
akkor a tesztek futásának végén a böngészőablakok nem záródnak be,
így meg lehet nézni a tesztek által végrehajtott műveleteket.