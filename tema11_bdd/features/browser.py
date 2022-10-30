from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager


class Browser:

    def __init__(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)

    def close(self):
        self.driver.quit()

    def set_username_correct(self, username):
        username_box = self.driver.find_element(By.ID, 'username')
        username_box.send_keys(username)

    def set_password_correct(self, password):
        password_box = self.driver.find_element(By.ID, 'password')
        password_box.send_keys(password)

    def click_login(self):
        login_button = self.driver.find_element(By.XPATH, '//*[@id="login"]/button')
        login_button.click()

    def get_page_menu(self):
        menu_text = self.driver.find_element(By.XPATH, '//*[@id="flash"]').text
        return menu_text

    def click_check_link(self):
        click_link = self.driver.find_element(By.LINK_TEXT, 'Checkboxes')
        click_link.click()

    def get_current_url(self):
        return self.driver.current_url

    def select_checkbox(self):
        select_box = self.driver.find_element(By.XPATH, '//*[@id="checkboxes"]')
        select_box.click()

    def click_dropdown(self):
        select_dropdown = self.driver.find_element(By.LINK_TEXT, 'Dropdown')
        select_dropdown.click()

    def click_option_dropdown(self):
        select_option = self.driver.find_element(By.XPATH, '//*[@id="dropdown"]/option[3]')
        select_option.click()

    def click_form_authentication(self):
        select_dropdown = self.driver.find_element(By.LINK_TEXT, 'Form Authentication')
        select_dropdown.click()

    def click_logout_button(self):
        self.driver.find_element(By.XPATH, "//a[@class='button secondary radius']").click()

    def click_x_message(self):
        self.driver.find_element(By.XPATH, "//a[@class='close']").click()
