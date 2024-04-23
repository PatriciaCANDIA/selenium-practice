from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement


class PinPage:
    ICON_PIN_PAGE = (By.XPATH, "//a[contains(@href, '/web/index.php/pim/viewPimModule')]")
    INPUT_EMPLOYEE_NAME = (By.XPATH, "//div[@class='oxd-autocomplete-wrapper']/div")  #VER. Me salen 2
    BUTTON_SEARCH = (By.XPATH, "//button[@type='submit']")
    TITLE_NO_RECORDS_FOUND = (By.XPATH, "//span[@class='oxd-text oxd-text--span']")
    SUBTITLE_TABLE_USERNAME = (By.XPATH, "//p[text()='Amelia']") #VER
    BUTTON_ADD = (By.XPATH, "//button[@class='oxd-button oxd-button--medium oxd-button--secondary']")
    BUTTON_SAVE = (By.XPATH, "//button[@class='oxd-button oxd-button--medium oxd-button--secondary orangehrm-left-space']")
    TEXT_REQUIRED_FIRST_NAME = (By. XPATH, "//input[@name='firstName']/../following-sibling::span")
    TEXT_REQUIRED_LAST_NAME = (By.XPATH, "//input[@name='lastName']/../following-sibling::span")
    INPUT_EMPLOYEE_FIRST_NAME = (By.NAME, "firstName")
    INPUT_EMPLOYEE_LAST_NAME = (By.NAME, "lastName")
    INPUT_EMPLOYEE_ID = (By.XPATH, "//input[@class='oxd-input oxd-input--active']")
    TITLE_PERSONAL_DETAILS = (By.XPATH, "//*[@id='app']/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/h6")
    TITLE_INPUT_FIRST_NAME = (By.NAME, "firstName")
    TITLE_INPUT_LAST_NAME = (By.NAME, "lastName")

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

    def click_input_employee_first_name(self):
        web_element_input_employee_first_name = self.driver.find_element(*self.INPUT_EMPLOYEE_FIRST_NAME)
        web_element_input_employee_first_name.click()

    def type_in_input_employee_first_name(self, text):
        web_element = self.driver.find_element(*self.INPUT_EMPLOYEE_FIRST_NAME)
        web_element.send_keys(text)

    def click_input_employee_last_name(self):
        web_element_input_employee_last_name = self.driver.find_element(*self.INPUT_EMPLOYEE_LAST_NAME)
        web_element_input_employee_last_name.click()

    def type_in_input_employee_last_name(self, text):
        web_element = self.driver.find_element(*self.INPUT_EMPLOYEE_LAST_NAME)
        web_element.send_keys(text)

    def click_input_employee_id(self):
        web_element_input_employee_id = self.driver.find_element(*self.INPUT_EMPLOYEE_ID)
        web_element_input_employee_id.click()

    def type_in_input_employee_id(self, text):
        web_element = self.driver.find_element(*self.INPUT_EMPLOYEE_ID)
        web_element.send_keys(text)

    def get_title_personal_details(self):
        web_element: WebElement = self.driver.find_element(*self.TITLE_PERSONAL_DETAILS)
        return web_element.text

    def get_title_input_first_name(self):
        web_element: WebElement = self.driver.find_element(*self.TITLE_INPUT_FIRST_NAME)
        return web_element.text

    def get_title_input_last_name(self):
        web_element: WebElement = self.driver.find_element(*self.TITLE_INPUT_LAST_NAME)
        return web_element.text

















