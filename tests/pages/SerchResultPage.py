from selenium.webdriver.common.by import By


class SearchResultPage:
    HEADING = (By.TAG_NAME, "h1")

    def __init__(self, driver):
        self.driver = driver

    def get_heading(self):
        web_element = self.driver.find_element(*self.HEADING)
        return web_element.text