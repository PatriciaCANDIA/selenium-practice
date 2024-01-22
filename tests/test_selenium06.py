import time
from selenium import webdriver
from tests.pages3.DashboardPage import DashboardPage
from tests.pages3.LoginPage import LoginPage
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService


class TestSelenium:
    def test_dashboard_sections(self):
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

        driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
        time.sleep(5)

        login_page = LoginPage(driver)
        login_page.click_input_username()
        login_page.type_in_input_username("Admin")
        login_page.click_input_password()
        login_page.type_in_input_password("admin123")
        login_page.click_button_login()
        time.sleep(5)

        dashboard_page = DashboardPage(driver)
        title = dashboard_page.get_time_at_work_section_title()
        assert title == "Time at Work", "Time at Work doesnt exist"
        time.sleep(2)

        title = dashboard_page.get_my_actions_title()
        assert title == "My Actions", "My Actions doesnt exist"

        title = dashboard_page.get_quick_launch_title()
        assert title == "Quick Launch", "Quick Launch doesnt exist"

        title = dashboard_page.get_buzz_latest_posts_title()
        assert title == "Buzz Latest Posts", "Buzz Latest Posts doesnt exist"

        title = dashboard_page.get_employees_leaves_today_title()
        assert title == "Employees on Leave Today", "Employees on Leave Today doesnt exist"

        title = dashboard_page.get_employee_distribution_by_sub_unit_title()
        assert title == "Employee Distribution by Sub Unit", "Employee Distribution by Sub Unit doesnt exist"

        title = dashboard_page.get_employee_distribution_by_location_title()
        assert title == "Employee Distribution by Location", "Employee Distribution by Location doesnt exist"


