from selenium.webdriver.common.by import By
from pages.base_page import BasePage
import time

class TransactionsPage(BasePage):
    TRANSACTIONS_BUTTON = (By.XPATH, "//button[contains(text(), 'Transactions')]")
    TRANSACTIONS_REPORT = (By.XPATH, "//tr[@class='ng-scope']")

    def navigate_to_transactions(self):
        self.click_element(self.TRANSACTIONS_BUTTON)


    def get_transactions_data(self):
        time.sleep(1)
        self.driver.refresh()
        return self.driver.find_elements(*self.TRANSACTIONS_REPORT)

