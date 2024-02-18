from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement


class PinPage:
    ICON_PIN_PAGE = (By.XPATH, "//*[@id='app']/div[1]/div[1]/aside/nav/div[2]/ul/li[2]")
    INPUT_EMPLOYEE_NAME = (By.XPATH, "//*[@id='app']/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[1]/div/div[1]/div/div[2]/div/div/input")
    BUTTON_SEARCH = (By.XPATH, "//*[@id='app']/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[2]/button[2]")
    TITLE_NO_RECORDS_FOUND = (By.XPATH, "//*[@id='app']/div[1]/div[2]/div[2]/div/div[2]/div[2]/div/span")
    SUBTITLE_TABLE_USERNAME = (By.XPATH, "//*[@id='app']/div[1]/div[2]/div[2]/div/div[2]/div[3]/div/div[2]/div/div/div[3]/div")
    BUTTON_ADD = (By.XPATH, "//*[@id='app']/div[1]/div[2]/div[2]/div/div[2]/div[1]/button")
    BUTTON_SAVE = (By.XPATH, "//*[@id='app']/div[1]/div[2]/div[2]/div/div/form/div[2]/button[2]")
    TEXT_REQUIRED_FIRST_NAME = (By.XPATH, "//*[@id='app']/div[1]/div[2]/div[2]/div/div/form/div[1]/div[2]/div[1]/div[1]/div/div/div[2]/div[1]/span")
    TEXT_REQUIRED_LAST_NAME = (By.XPATH, "//*[@id='app']/div[1]/div[2]/div[2]/div/div/form/div[1]/div[2]/div[1]/div[1]/div/div/div[2]/div[3]/span")

    def __init__(self, driver):
        self.driver = driver

    def click_icon_pin_page(self):
        web_element_icon_pin_page = self.driver.find_element(*self.ICON_PIN_PAGE)
        web_element_icon_pin_page.click()

    def click_input_employee_name(self):
        web_element_input_employee_name = self.driver.find_element(*self.INPUT_EMPLOYEE_NAME)
        web_element_input_employee_name.click()

    def type_in_input_employee_name(self, text):
        web_element = self.driver.find_element(*self.INPUT_EMPLOYEE_NAME)
        web_element.send_keys(text)

    def click_button_search(self):
        web_element_button_search = self.driver.find_element(*self.BUTTON_SEARCH)
        web_element_button_search.click()

    def get_title_no_records_found(self):
        web_element: WebElement = self.driver.find_element(*self.TITLE_NO_RECORDS_FOUND)
        return web_element.text

    def get_subtitle_table_username(self):
        web_element: WebElement = self.driver.find_element(*self.SUBTITLE_TABLE_USERNAME)
        return web_element.text

    def click_button_add(self):
        web_element_button_add = self.driver.find_element(*self.BUTTON_ADD)
        web_element_button_add.click()

    def click_button_save(self):
        web_element_button_save = self.driver.find_element(*self.BUTTON_SAVE)
        web_element_button_save.click()

    def get_title_required_first_name(self):
        web_element: WebElement = self.driver.find_element(*self.TEXT_REQUIRED_FIRST_NAME)
        return web_element.text

    def get_title_required_last_name(self):
        web_element: WebElement = self.driver.find_element(*self.TEXT_REQUIRED_LAST_NAME)
        return web_element.text
