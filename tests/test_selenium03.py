import time
from selenium import webdriver
from selenium.webdriver.chrome import webdriver
from tests.pages3.LoginPage import LoginPage
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService


class TestSelenium:

    def test_login(self):
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

        driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
        time.sleep(2)

        login_page = LoginPage(driver)
        title = login_page.get_title()
        assert title == "Login"

        login_page.click_input_username()
        login_page.type_in_input_username("Admin")
        login_page.click_input_password()
        login_page.type_in_input_password("admin123")
        login_page.click_button_login()
        
        title = login_page.get_title_home_page()
        assert title == "Dashboard"
