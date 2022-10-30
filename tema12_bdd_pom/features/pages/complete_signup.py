from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class CompleteSign(BasePage):
    EMAIL_SELECTOR = (By.XPATH, '//*[@id="root"]/div/div[4]/div[2]/div/div[2]/div/div/input')

    def click_personal(self):
        self.driver.find_element(By.XPATH, "//input[@value='personal']").click()

    def continue_button(self):
        continue_button = (By.XPATH, "//span[normalize-space()='CONTINUE']")
        return self.driver.find_element(*continue_button)

    def input_first_name(self, first_name):
        first_name_element = self.driver.find_element(By.XPATH, '//input')
        first_name_element.send_keys(first_name)

    def input_last_name(self, last_name):
        last_name_element = self.driver.find_element(By.XPATH, '//input')
        last_name_element.send_keys(last_name)

    def input_wrong_email(self):
        self.driver.find_element(*self.EMAIL_SELECTOR).send_keys('ceva')

    def verify_error(self):
        message = self.driver.find_element(By.XPATH, '//*[@id="root"]/div/div[4]/div[2]/div/div[2]/div/p').text
        return message

    def clear_email(self):
        email_element = self.driver.find_element(*self.EMAIL_SELECTOR)
        email_element.send_keys(Keys.COMMAND + "a")
        email_element.send_keys(Keys.DELETE)
