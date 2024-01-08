from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement


class ResetPasswordPage:
    LINK_FORGOT_PASSWORD = (By.XPATH, "//*[@id='app']/div[1]/div/div[1]/div/div[2]/div[2]/form/div[4]/p")
    RESET_PASSWORD_TITLE = (By.XPATH, "//*[@id='app']/div[1]/div[1]/div/form/h6")
    USERNAME_INPUT = (By.NAME, "username")
    CANCEL_BUTTON = (By.XPATH, "//*[@id='app']/div[1]/div[1]/div/form/div[2]/button[1]")
    RESET_PASSWORD_BUTTON = (By.XPATH, "//*[@id='app']/div[1]/div[1]/div/form/div[2]/button[2]")
    REQUIRED_MESSAGE = (By.XPATH, "//*[@id='app']/div[1]/div[1]/div/form/div[1]/div/span")
    SUCCESSFULLY_MESSAGE_TITLE = (By.XPATH, "//*[@id='app']/div[1]/div[1]/div/h6")

    def __init__(self, driver):
        self.driver = driver

    def click_link_forgot_password(self):
        web_element_link_forgot_password = self.driver.find_element(*self.LINK_FORGOT_PASSWORD)
        web_element_link_forgot_password.click()

    def get_reset_password_title(self):
        web_element: WebElement = self.driver.find_element(*self.RESET_PASSWORD_TITLE)
        return web_element.text

    def click_username_input(self):
        web_element_username_input = self.driver.find_element(*self.USERNAME_INPUT)
        web_element_username_input.click()

    def type_in_username_input(self, text):
        web_element = self.driver.find_element(*self.USERNAME_INPUT)
        web_element.send_keys(text)

    def click_cancel_button(self):
        web_element_cancel_button = self.driver.find_element(*self.CANCEL_BUTTON)
        web_element_cancel_button.click()

    def click_reset_password_button(self):
        web_element_reset_password_button = self.driver.find_element(*self.RESET_PASSWORD_BUTTON)
        web_element_reset_password_button.click()

    def get_required_message_title(self):
        web_element: WebElement = self.driver.find_element(*self.REQUIRED_MESSAGE)
        return web_element.text

    def get_successfully_message_title(self):
        web_element: WebElement = self.driver.find_element(*self.SUCCESSFULLY_MESSAGE_TITLE)
        return web_element.text

