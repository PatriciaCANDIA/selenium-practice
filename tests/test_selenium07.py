import time
from selenium import webdriver
from tests.pages3.AdminPage import AdminPage
from tests.pages3.LoginPage import LoginPage
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService


class TestSelenium:
    def test_username_not_found(self):
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

        admin_page = AdminPage(driver)
        time.sleep(5)
        admin_page.click_icon_admin_page()
        time.sleep(2)
        admin_page.click_input_username_admin_page()
        admin_page.type_in_input_username_admin_page("Adminn")
        admin_page.click_button_search()
        time.sleep(5)

        title = admin_page.get_title_no_records_found()
        assert title == "No Records Found", "No Records Found does not appear"
