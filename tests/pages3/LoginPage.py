from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement


class LoginPage:
    HEADING_TITLE = (By.XPATH, "//*[@id='app']/div[1]/div/div[1]/div/div[2]/h5")
    INPUT_USERNAME = (By.NAME, "username")
    INPUT_PASSWORD = (By.NAME, "password")
    BUTTON_LOGIN = (By.XPATH, "//*[@id='app']/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button")
    HEADING_TITLE_HOME_PAGE = (By.XPATH, "//*[@id='app']/div[1]/div[1]/header/div[1]/div[1]/span/h6")

    def __init__(self, driver):
        self.driver = driver

    def get_title(self):
        web_element: WebElement = self.driver.find_element(*self.HEADING_TITLE)
        return web_element.text

    def click_input_username(self):
        web_element_input_username = self.driver.find_element(*self.INPUT_USERNAME)
        web_element_input_username.click()

    def type_in_input_username(self, text):
        web_element = self.driver.find_element(*self.INPUT_USERNAME)
        web_element.send_keys(text)

    def click_input_password(self):
        web_element_input_password = self.driver.find_element(*self.INPUT_PASSWORD)
        web_element_input_password.click()

    def type_in_input_password(self, text):
        web_element = self.driver.find_element(*self.INPUT_PASSWORD)
        web_element.send_keys(text)

    def click_button_login(self):
        web_element_button_login = self.driver.find_element(*self.BUTTON_LOGIN)
        web_element_button_login.click()

    def get_title_home_page(self):
        web_element: WebElement = self.driver.find_element(*self.HEADING_TITLE_HOME_PAGE)
        return web_element.text







