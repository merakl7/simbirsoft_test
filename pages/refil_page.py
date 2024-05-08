from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from utils.calculation import Fibonacci


class MoneyTransactions(BasePage):
    DEPOSIT_BUTTON = (By.XPATH, "//button[contains(text(), 'Deposit')]")
    FILED_INPUT = (By.CSS_SELECTOR, "input.form-control.ng-pristine.ng-untouched.ng-invalid.ng-invalid-required")
    SENDING = (By.CSS_SELECTOR, "button.btn.btn-default")
    WITHDRAWAL_BUTTON = (By.XPATH, "//button[contains(text(), 'Withdrawl')]")
    BALANCE_ELEMENT = (By.CSS_SELECTOR, "strong.ng-binding:nth-of-type(2)")

    def deposit_money(self):
        fib_number = Fibonacci.get_calculated_number()

        self.click_element(self.DEPOSIT_BUTTON)
        self.input_text(self.FILED_INPUT, fib_number)
        self.click_element(self.SENDING)

        self.click_element(self.WITHDRAWAL_BUTTON)
        self.input_text(self.FILED_INPUT, fib_number)
        self.click_element(self.SENDING)

    def check_money(self):
        balance_element = self.wait_for_element(self.BALANCE_ELEMENT)
        balance_value = balance_element.text.strip()
        assert balance_value == "0"
        return balance_value
