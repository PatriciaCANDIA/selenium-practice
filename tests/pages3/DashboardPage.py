from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement


class DashboardPage:
    HEADING_TITLE_HOME_PAGE = (By.XPATH, "//*[@id='app']/div[1]/div[1]/header/div[1]/div[1]/span/h6")

    def __init__(self, driver):
        self.driver = driver

    def get_title_home_page(self):
        web_element: WebElement = self.driver.find_element(*self.HEADING_TITLE_HOME_PAGE)
        return web_element.text
