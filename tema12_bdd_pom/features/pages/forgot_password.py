from features.pages.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class FormForgot(BasePage):
    URL = "https://jules.app/forgot-password"

    def send_email_btn(self):
        self.driver.find_element(By.XPATH, '//*[@id="root"]//button/span[1]').click()

    def send_message(self):
        return self.driver.find_element(By.XPATH, '//*[@id="client-snackbar"]/div/span').is_displayed()

    def input_email(self, value):
        self.driver.find_element(By.XPATH, '//input[@placeholder="Enter your email"]').send_keys(value)
