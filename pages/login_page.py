from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class LoginPage(BasePage):
    URL = "https://www.globalsqa.com/angularJs-protractor/BankingProject/#/login"
    LOGIN_BUTTON = (By.CSS_SELECTOR, 'button.btn.btn-primary.btn-lg')
    CUSTOMER_DROPDOWN = (By.ID, 'userSelect')
    SUBMIT_BUTTON = (By.CSS_SELECTOR, 'button.btn.btn-default[type="submit"][ng-show="custId != \'\'"]')

    def open(self):
        self.driver.get(self.URL)

    def click_login_button(self):
        self.click_element(self.LOGIN_BUTTON)

    def select_customer(self, customer_name):
        self.click_element(self.CUSTOMER_DROPDOWN)
        dropdown_option = (By.XPATH, f'//option[text()="{customer_name}"]')
        self.click_element(dropdown_option)
        self.click_element(self.SUBMIT_BUTTON)
