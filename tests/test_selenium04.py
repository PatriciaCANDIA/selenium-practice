import time
from selenium import webdriver
from tests.pages3.LoginPage import LoginPage
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService


class TestSelenium:

    def test_not_logged_in(self):
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

        driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
        time.sleep(2)

        login_page = LoginPage(driver)
        login_page.click_input_username()
        login_page.type_in_input_username("Addmin")
        login_page.click_input_password()
        login_page.type_in_input_password("addmin123")
        login_page.click_button_login()
        time.sleep(5)

        text = login_page.get_invalid_credential_text()
        assert text == "Invalid credentials"




