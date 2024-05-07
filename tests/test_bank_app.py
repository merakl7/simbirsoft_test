import unittest
import pandas as pd
import allure
from selenium import webdriver
from pages.login_page import LoginPage
from pages.transaction_page import TransactionsPage
from pages.refil_page import MoneyTransactions
from utils.allure_report import attach_csv_report
from selenium.webdriver.common.by import By


class TestBankTransactions(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.login_page = LoginPage(cls.driver)
        cls.transactions_page = TransactionsPage(cls.driver)
        cls.refil_page = MoneyTransactions(cls.driver)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    @allure.title("Bank Transactions Test")
    def test_bank_transactions(self):
        self.login_page.open()

        self.login_page.click_login_button()

        self.login_page.select_customer("Harry Potter")

        self.refil_page.deposit_money()

        self.refil_page.check_money()

        self.transactions_page.navigate_to_transactions()
        transactions_report = self.transactions_page.get_transactions_data()
        transactions_data = []
        for element in transactions_report:
            date = element.find_element(By.XPATH, "./td[1]").text
            amount = element.find_element(By.XPATH, "./td[2]").text
            transaction_type = element.find_element(By.XPATH, "./td[3]").text
            transaction_info = (date, amount, transaction_type)
            transactions_data.append(transaction_info)

        df = pd.DataFrame(transactions_data, columns=['Дата-времяТранзакции', 'Сумма', 'ТипТранзакции'])
        csv_file = "Transactions.csv"
        df.to_csv(csv_file, index=False, encoding='utf8', sep=',')
        attach_csv_report(csv_file)


if __name__ == '__main__':
    unittest.main()
