from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement


class ProductPage:

    PRODUCT_LINK = (By.XPATH, "//*[@id='tbodyid']/div[1]/div/div/h4")
    HEADING_TITLE = (By.XPATH, "//*[@id='tbodyid']/h2")
    ADD_TO_CART_BUTTON = (By.XPATH, "//*[@id='tbodyid']/div[2]/div/a")

    def __init__(self, driver):
        self.driver: Webdriver = driver

    def click_link(self):
        web_element: WebElement = self.driver.find_element(*self.PRODUCT_LINK)
        web_element_link.click()

    def get_title(self):
        web_element: WebElement = self.driver.find_element(*self.HEADING_TITLE)
        return web_element.text

    def click_add_to_cart_button(self):
        web_element_add_to_cart_button: WebElement = self.driver.find_element(*self.ADD_TO_CART_BUTTON)
        web_element_add_to_cart_button.click()







