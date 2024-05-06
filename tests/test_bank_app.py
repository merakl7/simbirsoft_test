import unittest
import datetime
import pandas as pd
import allure
from selenium import webdriver
from pages.login_page import LoginPage
from pages.transaction_page import TransactionsPage
from utils.allure_report import attach_csv_report

class TestBankTransactions(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Remote(command_executor="http://your_grid_url:4444/wd/hub", desired_capabilities={})
        cls.login_page = LoginPage(cls.driver)
        cls.transactions_page = TransactionsPage(cls.driver)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    @allure.title("Bank Transactions Test")
    def test_bank_transactions(self):
        try:
            # Открытие страницы логина
            self.login_page.open()

            # Нажатие кнопки логина
            self.login_page.click_login_button()

            # Выбор клиента по имени
            self.login_page.select_customer("Harry Potter")

            # Вычисление числа Фибоначчи исходя из текущей даты
            day_of_month = datetime.datetime.now().day + 1
            fib1, fib2 = 1, 1
            for _ in range(day_of_month - 2):
                fib1, fib2 = fib2, fib1 + fib2

            # Пополнение счета
            self.transactions_page.navigate_to_transactions()
            transactions_data = self.transactions_page.get_transactions_data()

            # Сохранение данных в CSV файл
            df = pd.DataFrame([(td.text for td in row.find_elements_by_tag_name('td')) for row in transactions_data],
                              columns=['Дата-времяТранзакции', 'Сумма', 'ТипТранзакции'])
            csv_file = "Transactions.csv"
            df.to_csv(csv_file, index=False, encoding='utf8', sep=',')
            attach_csv_report(csv_file)

        except Exception as e:
            allure.attach(self.driver.get_screenshot_as_png(), name="screenshot", attachment_type=allure.attachment_type.PNG)
            raise e

if __name__ == '__main__':
    unittest.main()
