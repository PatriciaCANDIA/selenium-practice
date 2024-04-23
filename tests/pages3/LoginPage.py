from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement


class LoginPage:
    HEADING_TITLE = (By.XPATH, "//h5[@class='oxd-text oxd-text--h5 orangehrm-login-title']")
    INPUT_USERNAME = (By.NAME, "username")
    INPUT_PASSWORD = (By.NAME, "password")
    BUTTON_LOGIN = (By.XPATH, "//button[@type='submit']")
    INVALID_CREDENTIALS_TEXT = (By.XPATH, "//p[text()='Invalid credentials']")

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

    def get_invalid_credential_text(self):
        web_element: WebElement = self.driver.find_element(*self.INVALID_CREDENTIALS_TEXT)
        return web_element.text









