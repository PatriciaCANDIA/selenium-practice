from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement


class DashboardPage:
    HEADING_TITLE_HOME_PAGE = (By.XPATH, "//*[@id='app']/div[1]/div[1]/header/div[1]/div[1]/span/h6")
    TIME_AT_WORK_SECTION_TITLE = (By.XPATH, "//*[@id='app']/div[1]/div[2]/div[2]/div/div[1]/div/div[1]/div/p")
    MY_ACTIONS_SECTION_TITLE = (By.XPATH, "//*[@id='app']/div[1]/div[2]/div[2]/div/div[2]/div/div[1]/div/p")
    QUICK_LAUNCH_SECTION_TITLE = (By.XPATH, "//*[@id='app']/div[1]/div[2]/div[2]/div/div[3]/div/div[1]/div/p")
    BUZZ_LATEST_POSTS_SECTION_TITLE = (By.XPATH, "//*[@id='app']/div[1]/div[2]/div[2]/div/div[4]/div/div[1]/div/p")
    EMPLOYEES_ON_LEAVE_TODAY_SECTION_TITLE = (By.XPATH, "//*[@id='app']/div[1]/div[2]/div[2]/div/div[5]/div/div[1]/div/p")
    EMPLOYEE_DISTRIBUTION_BY_SUB_UNIT_SECTION_TITLE = (By.XPATH, "//*[@id='app']/div[1]/div[2]/div[2]/div/div[6]/div/div[1]/div/p")
    EMPLOYEE_DISTRIBUTION_BY_LOCATION_SECTION_TITLE = (By.XPATH, "//*[@id='app']/div[1]/div[2]/div[2]/div/div[7]/div/div[1]/div/p")

    def __init__(self, driver):
        self.driver = driver

    def get_title_home_page(self):
        web_element: WebElement = self.driver.find_element(*self.HEADING_TITLE_HOME_PAGE)
        return web_element.text

    def get_time_at_work_section_title(self):
        web_element: WebElement = self.driver.find_element(*self.TIME_AT_WORK_SECTION_TITLE)
        return web_element.text

    def get_my_actions_title(self):
        web_element: WebElement = self.driver.find_element(*self.MY_ACTIONS_SECTION_TITLE)
        return web_element.text

    def get_quick_launch_title(self):
        web_element: WebElement = self.driver.find_element(*self.QUICK_LAUNCH_SECTION_TITLE)
        return web_element.text

    def get_buzz_latest_posts_title(self):
        web_element: WebElement = self.driver.find_element(*self.BUZZ_LATEST_POSTS_SECTION_TITLE)
        return web_element.text

    def get_employees_leaves_today_title(self):
        web_element: WebElement = self.driver.find_element(*self.EMPLOYEES_ON_LEAVE_TODAY_SECTION_TITLE)
        return web_element.text

    def get_employee_distribution_by_sub_unit_title(self):
        web_element: WebElement = self.driver.find_element(*self.EMPLOYEE_DISTRIBUTION_BY_SUB_UNIT_SECTION_TITLE)
        return web_element.text

    def get_employee_distribution_by_location_title(self):
        web_element: WebElement = self.driver.find_element(*self.EMPLOYEE_DISTRIBUTION_BY_LOCATION_SECTION_TITLE)
        return web_element.text
