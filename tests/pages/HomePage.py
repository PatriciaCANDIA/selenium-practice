from selenium.webdriver.common.by import By


class HomePage:
    #Atributos
    LINK_ENGLISH = (By.ID, "js-link-box-en")
    LINK_ESPANOL = (By.ID, "js-link-box-es")
    LINK_FRANCES = (By.ID, "js-link-box-fr")
    LINK_PORTUGUES = (By.ID, "js-link-box-pt")
    INPUT_SEARCH_BOX = (By.ID, "searchInput")
    BUTTON_MAGNIFYING_GLASS = (By.XPATH, "//*[@id='search-form]/fieldset/button/i")

    #Funcion especial init. Cuando se instancia la clase se llama a esta funcion
    def __init__(self, driver):
        self.driver = driver

    #Metodos/funciones : cosas que sabe hacer la pagina

    def click_link_english(self):
        web_element_link_english = self.driver.find_element(*self.LINK_ENGLISH)
        web_element_link_english.click()

    def click_link_espanol(self):
        web_element_link_espanol = self.driver.find_element(*self.LINK_ESPANOL)
        web_element_link_espanol.click()

    def click_link_frances(self):
        web_element_link_frances = self.driver.find_element(*self.LINK_FRANCES)
        web_element_link_frances.click()

    def click_link_portugues(self):
        web_element_link_portugues = self.driver.find_element(*self.LINK_PORTUGUES)
        web_element_link_portugues.click()

    def click_button_magnifying_glass(self):
        web_element = self.driver.find_element(*self.BUTTON_MAGNIFYING_GLASS)
        web_element.click()

    def type_in_search_input(self, text):
        web_element = self.driver.find_element(self.INPUT_SEARCH_BOX)
        web_element.send_keys(text)
