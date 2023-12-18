from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement


class ProductStoreHomePage:
    LINK_HOME = (By.XPATH, "//*[@id='navbarExample']/ul/li[1]/a")
    FIRST_ITEM = (By.XPATH, "//div[@id='tbodyid']//a")
    CONTACT_ITEM = (By.XPATH, "//*[@id='navbarExample']/ul/li[2]/a")
    INPUT_CONTACT_EMAIL = (By.ID, "recipient-email")
    INPUT_CONTACT_NAME = (By.ID, "recipient-name")
    INPUT_MESSAGE = (By.ID, "message-text")
    BUTTON_SEND_MESSAGE = (By.XPATH, "//*[@id='exampleModal']/div/div/div[3]/button[2]")
    ABOUT_US_ITEM = (By.XPATH, "//*[@id='navbarExample']/ul/li[3]/a")
    CART_ITEM = (By.XPATH, "//*[@id='navbarExample']/ul/li[4]/a")
    BUTTON_PLACE_ORDER = (By.XPATH, "//*[@id='page-wrapper']/div/div[2]/button")
    INPUT_NAME = (By.ID, "name")
    INPUT_COUNTRY = (By.ID, "country")
    INPUT_CITY = (By.ID, "city")
    INPUT_CREDIT_CARD = (By.ID, "card")
    INPUT_MONTH = (By.ID, "month")
    INPUT_YEAR = (By.ID, "year")
    BUTTON_PURCHARSE = (By.XPATH, "//*[@id='orderModal']/div/div/div[3]/button[2]")
    LOG_IN_ITEM = (By.XPATH, "//*[@id='login2']")
    INPUT_USERNAME = (By.ID, "loginusername")
    INPUT_PASSWORD = (By.ID, "loginpassword")
    BUTTON_LOG_IN = (By.XPATH, "//*[@id='logInModal']/div/div/div[3]/button[2]")
    INPUT_LOG_OUT = (By.ID, "logout2")
    SIGN_UP_ITEM = (By.ID, "signin2")
    INPUT_USERNAME_SIGN_UP = (By.ID, "sign-username")
    INPUT_PASSWORD_SING_UP = (By.ID, "sign-password")
    BUTTON_SIGN_UP = (By.XPATH, "//*[@id='signInModal']/div/div/div[3]/button[2]")
    LINK_LOG_OUT = (By.ID, "logout2")
    LINK_WELCOME_MESSAGE = (By.ID, "nameofuser")

    def __init__(self, driver):
        self.driver = driver

    def click_link_home(self):
        web_element_link_home = self.driver.find_element(*self.LINK_HOME)
        web_element_link_home.click()

    def click_first_item(self):
        web_element_first_item = self.driver.find_element(*self.FIRST_ITEM)
        web_element_first_item.click()

    def click_contact_item(self):
        web_element_contact_item = self.driver.find_element(*self.CONTACT_ITEM)
        web_element_contact_item.click()

    def type_in_contact_email_input(self, text):
        web_element = self.driver.find_element(*self.INPUT_CONTACT_EMAIL)
        web_element.send_keys(text)

    def type_in_contact_name_input(self, text):
        web_element = self.driver.find_element(*self.INPUT_CONTACT_NAME)
        web_element.send_keys(text)

    def type_in_message_input(self, text):
        web_element = self.driver.find_element(*self.INPUT_MESSAGE)
        web_element.send_keys(text)

    def click_button_send_message(self):
        web_element_button_send_message = self.driver.find_element(*self.BUTTON_SEND_MESSAGE)
        web_element_button_send_message.click()

    def click_about_us_item(self):
        web_element_about_us_item = self.driver.find_element(*self.ABOUT_US_ITEM)
        web_element_about_us_item.click()

    def click_cart_item(self):
        web_element_cart_item = self.driver.find_element(*self.CART_ITEM)
        web_element_cart_item.click()

    def click_place_order_button(self):
        web_element_place_order_button = self.driver.find_element(*self.BUTTON_PLACE_ORDER)
        web_element_place_order_button.click()

    def type_in_input_name(self, text):
        web_element = self.driver.find_element(*self.INPUT_NAME)
        web_element.send_keys(text)

    def type_in_input_country(self, text):
        web_element = self.driver.find_element(*self.INPUT_COUNTRY)
        web_element.send_keys(text)

    def type_in_input_city(self, text):
        web_element = self.driver.find_element(*self.INPUT_CITY)
        web_element.send_keys(text)

    def type_in_input_credit_card(self, text):
        web_element = self.driver.find_element(*self.INPUT_CREDIT_CARD)
        web_element.send_keys(text)

    def type_in_input_month(self, text):
        web_element = self.driver.find_element(*self.INPUT_MONTH)
        web_element.send_keys(text)

    def type_in_input_year(self, text):
        web_element = self.driver.find_element(*self.INPUT_YEAR)
        web_element.send_keys(text)

    def click_button_purcharse(self):
        web_element_button_purcharse = self.driver.find_element(*self.BUTTON_PURCHARSE)
        web_element_button_purcharse.click()

    def click_log_in_item(self):
        web_element_log_in_item = self.driver.find_element(*self.LOG_IN_ITEM)
        web_element_log_in_item.click()

    def type_in_username_input(self, text):
        web_element = self.driver.find_element(*self.INPUT_USERNAME)
        web_element.send_keys(text)

    def type_in_password_input(self, text):
        web_element = self.driver.find_element(*self.INPUT_PASSWORD)
        web_element.send_keys(text)

    def click_log_in_button(self):
        web_element_log_in_button = self.driver.find_element(*self.BUTTON_LOG_IN)
        web_element_log_in_button.click()

    def click_sign_up_item(self):
        web_element_sign_up_item = self.driver.find_element(*self.SIGN_UP_ITEM)
        web_element_sign_up_item.click()

    def type_in_username_input_sign_up(self, text):
        web_element = self.driver.find_element(*self.INPUT_USERNAME_SIGN_UP)
        web_element.send_keys(text)

    def type_in_password_input_sign_up(self, text):
        web_element = self.driver.find_element(*self.INPUT_PASSWORD_SING_UP)
        web_element.send_keys(text)

    def click_sign_up_button(self):
        web_element_sign_up_button = self.driver.find_element(*self.BUTTON_SIGN_UP)
        web_element_sign_up_button.click()

    def get_log_out_text(self):
        web_element: WebElement = self.driver.find_element(*self.LINK_LOG_OUT)
        return web_element.text

    def get_welcome_message_text(self):
        web_element: WebElement = self.driver.find_element(*self.LINK_WELCOME_MESSAGE)
        return web_element.text
