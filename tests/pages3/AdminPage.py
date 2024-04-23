from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement


class AdminPage:
    ICON_ADMIN_PAGE = (By.XPATH, "//a[contains(@href, '/web/index.php/admin/viewAdminModule')]")
    INPUT_USERNAME_ADMIN_PAGE = (By.XPATH, "//input[@class='oxd-input oxd-input--active']")
    BUTTON_SEARCH = (By.XPATH, "//button[@type='submit']")
    TITLE_NO_RECORDS_FOUND = (By.XPATH, "//span[@class='oxd-text oxd-text--span']")
    SUBTITLE_TABLE_USERNAME = (By.XPATH, "//div[@class='oxd-table']/div/div/div/div[2]")

    def __init__(self, driver):
        self.driver = driver

    def click_icon_admin_page(self):
        web_element_icon_admin_page = self.driver.find_element(*self.ICON_ADMIN_PAGE)
        web_element_icon_admin_page.click()

    def click_input_username_admin_page(self):
        web_element_input_username = self.driver.find_element(*self.INPUT_USERNAME_ADMIN_PAGE)
        web_element_input_username.click()

    def type_in_input_username_admin_page(self, text):
        web_element = self.driver.find_element(*self.INPUT_USERNAME_ADMIN_PAGE)
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






