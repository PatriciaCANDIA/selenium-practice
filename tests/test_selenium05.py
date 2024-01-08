import time
from selenium import webdriver
from tests.pages3.LoginPage import LoginPage
from tests.pages3.ResetPasswordPage import ResetPasswordPage
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService


class TestSelenium:

    def test_cancel_reset_password(self):
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

        driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
        time.sleep(5)

        resetpasswordpage = ResetPasswordPage(driver)
        resetpasswordpage.click_link_forgot_password()
        time.sleep(2)

        title = resetpasswordpage.get_reset_password_title()
        assert title == "Reset Password"
        time.sleep(5)

        resetpasswordpage.click_username_input()
        resetpasswordpage.type_in_username_input("cualquiernombre")
        resetpasswordpage.click_cancel_button()
        time.sleep(2)

        login_page = LoginPage(driver)
        title = login_page.get_title()
        assert title == "Login"

    def test_error_reset_password(self):
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

        driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
        time.sleep(5)

        resetpasswordpage = ResetPasswordPage(driver)
        resetpasswordpage.click_link_forgot_password()
        time.sleep(5)
        title = resetpasswordpage.get_reset_password_title()
        assert title == "Reset Password"
        time.sleep(5)

        resetpasswordpage.click_reset_password_button()
        time.sleep(2)
        title = resetpasswordpage.get_required_message_title()
        assert title == "Required"
        time.sleep(2)

    def test_successfully_reset_password(self):
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

        driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
        time.sleep(5)

        resetpasswordpage = ResetPasswordPage(driver)
        resetpasswordpage.click_link_forgot_password()
        time.sleep(5)
        title = resetpasswordpage.get_reset_password_title()
        assert title == "Reset Password"
        time.sleep(5)

        resetpasswordpage.click_reset_password_button()
        time.sleep(2)
        title = resetpasswordpage.get_required_message_title()
        assert title == "Required"
        time.sleep(2)

        resetpasswordpage.click_username_input()
        resetpasswordpage.type_in_username_input("cualquiernombre")
        resetpasswordpage.click_reset_password_button()
        time.sleep(5)

        title = resetpasswordpage.get_successfully_message_title()
        assert title == "Reset Password link sent successfully"
        time.sleep(2)
