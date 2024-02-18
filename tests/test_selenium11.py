import time
from selenium import webdriver
from tests.pages3.LoginPage import LoginPage
from tests.pages3.PinPage import PinPage
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService


class TestSelenium:
    def test_not_add_employee(self):
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

        pin_page = PinPage(driver)
        pin_page.click_icon_pin_page()
        time.sleep(2)
        pin_page.click_button_add()
        time.sleep(2)
        pin_page.click_button_save()
        time.sleep(2)

        title = pin_page.get_title_required_first_name()
        assert title == "Required", "Required doesnt appear"

        title = pin_page.get_title_required_last_name()
        assert title == "Required", "Required doesnt appear"
