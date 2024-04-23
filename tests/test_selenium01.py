import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from tests.pages.HomePage import HomePage
from tests.pages.SerchResultPage import SearchResultPage
from webdriver_manager.chrome import ChromeDriverManager


class TestSelenium:  # Los nombres de las clases se escriben en Camel Case

    def test01(self):
        # selenium 4

        # Linea obligatoria para levantar el navegador
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

        # Step 1 - Go to wikipedia home page
        self.driver.get("https://wikipedia.org")  # Funcion get
        time.sleep(5)

        # Step 2 -  Click link English
        home_page = HomePage(self.driver)
        home_page.click_link_english()

        # Step 3 - Go back to previous link
        self.driver.back()

        # Step 4 - Click link Espanol
        home_page = HomePage(self.driver)
        home_page.click_link_espanol()
        self.driver.back()

        home_page = HomePage(self.driver)
        home_page.click_link_frances()
        self.driver.back()

        home_page = HomePage(self.driver)
        home_page.click_link_portugues()
        self.driver.back()

        # Linea obligatoria para matar el navegador
        self.driver.quit()

    def test_buscar(self):
        # Linea obligatoria para levantar el navegador
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

        # Step 1 - Go to wikipedia home page
        self.driver.get("https://wikipedia.org")  # Funcion get

        # Step 2 - Type 'Piramides' in search box
        home_page = HomePage(self.driver)
        home_page.type_in_search_input("piramides")

        # Step 3 - Click 'Magnifying glass' button
        home_page.click_button_magnifying_glass()

        search_result_page = SearchResultPage(self.driver)
        title = search_result_page.get_heading()

        assert title == "Search results", "The search result page was not displayed"

    # InvalidArgumentException
    # NoSuchElementException 'El elemento que estoy buscando no esta en el DOM/HTML'
    # StaleElementException 'Se cargo nuevamente la pagina'
    # InterceptedClickException 'Esta mal cargada la pagina, puede ser que un elemento este arriba de otro y no le haga click'
