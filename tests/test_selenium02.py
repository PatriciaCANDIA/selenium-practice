import time
from selenium import webdriver
from tests.pages2.ProductPage import ProductPage
from tests.pages2.ProductStoreHomePage import ProductStoreHomePage
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService


class TestSelenium:

    def test_primer_item(self):
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

        driver.get("https://www.demoblaze.com")
        time.sleep(2)

        product_store_home_page = ProductStoreHomePage(driver)
        product_store_home_page.click_link_home()
        time.sleep(2)
        product_store_home_page.click_first_item()
        time.sleep(2)

        product_page = ProductPage(driver)
        title = product_page.get_title()

        assert title == "Samsung galaxy s6"

    def test_send_message(self):
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

        driver.get("https://www.demoblaze.com")
        time.sleep(2)

        product_store_home_page = ProductStoreHomePage(driver)
        product_store_home_page.click_contact_item()
        time.sleep(2)

        product_store_home_page.type_in_contact_email_input("cualquiermail@yahoo.com")
        product_store_home_page.type_in_contact_name_input("cualquiernombre")
        product_store_home_page.type_in_message_input("quiero mas informacion")
        product_store_home_page.click_button_send_message()
        time.sleep(5)

    def test_about_us_item(self):
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

        driver.get("https://www.demoblaze.com")
        time.sleep(2)
        product_store_home_page = ProductStoreHomePage(driver)
        product_store_home_page.click_about_us_item()

    def test_cart_item(self):
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

        driver.get("https://www.demoblaze.com")
        product_store_home_page = ProductStoreHomePage(driver)
        product_store_home_page.click_cart_item()

    def test_add_product(self):
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

        driver.get("https://www.demoblaze.com")
        time.sleep(2)

        product_store_home_page = ProductStoreHomePage(driver)
        product_store_home_page.click_first_item()
        time.sleep(2)

        product_page = ProductPage(driver)
        product_page.click_add_to_cart_button()
        time.sleep(2)
        driver.back()

    def test_place_order(self):
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

        driver.get("https://www.demoblaze.com")
        time.sleep(2)

        product_store_home_page = ProductStoreHomePage(driver)
        product_store_home_page.click_cart_item()
        product_store_home_page.click_place_order_button()
        time.sleep(2)
        product_store_home_page.type_in_input_name("Patricia")
        product_store_home_page.type_in_input_country("Argentina")
        product_store_home_page.type_in_input_city("Misiones")
        product_store_home_page.type_in_input_credit_card("33388899965")
        product_store_home_page.type_in_input_month("4")
        product_store_home_page.type_in_input_year("2024")
        product_store_home_page.click_button_purcharse()

    def test_log_in(self):
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

        driver.get("https://www.demoblaze.coma")
        time.sleep(2)
        product_store_home_page = ProductStoreHomePage(driver)
        product_store_home_page.click_log_in_item()
        time.sleep(2)

        product_store_home_page.type_in_username_input("Pato888")
        product_store_home_page.type_in_password_input("222222")
        product_store_home_page.click_log_in_button()
        time.sleep(2)
        assert product_store_home_page.get_log_out_text() == "Log out"
        assert product_store_home_page.get_welcome_message_text() == "Welcome Pato888"

    def test_sign_up(self):
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

        driver.get("https://www.demoblaze.com")
        time.sleep(2)

        product_store_home_page = ProductStoreHomePage(driver)
        product_store_home_page.click_sign_up_item()
        time.sleep(2)
        product_store_home_page.type_in_username_input_sign_up("Pato88")
        product_store_home_page.type_in_password_input_sign_up("222222")
        product_store_home_page.click_sign_up_button()
        time.sleep(10)
