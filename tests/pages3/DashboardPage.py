from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement


class DashboardPage:
    HEADING_TITLE_HOME_PAGE = (By.XPATH, "//span[@class='oxd-topbar-header-breadcrumb']")
    TIME_AT_WORK_SECTION_TITLE = (By.XPATH, "//p[text()='Time at Work']")
    MY_ACTIONS_SECTION_TITLE = (By.XPATH, "//p[text()='My Actions']")
    QUICK_LAUNCH_SECTION_TITLE = (By.XPATH, "//p[text()='Quick Launch']")
    BUZZ_LATEST_POSTS_SECTION_TITLE = (By.XPATH, "//p[text()='Buzz Latest Posts']")
    EMPLOYEES_ON_LEAVE_TODAY_SECTION_TITLE = (By.XPATH, "//p[text()='Employees on Leave Today']")
    EMPLOYEE_DISTRIBUTION_BY_SUB_UNIT_SECTION_TITLE = (By.XPATH, "//p[text()='Employee Distribution by Sub Unit']")
    EMPLOYEE_DISTRIBUTION_BY_LOCATION_SECTION_TITLE = (By.XPATH, "//p[text()='Employee Distribution by Location']")

    def __init__(self, driver):
        self.driver = driver
        self.driver = driver
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
