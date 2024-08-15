import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from PageFactoryTest.pages.google_finance_page import GoogleFinancePage

class GoogleFinanceTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        chrome_options = Options()
        chrome_options.add_argument("--headless")
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--disable-dev-shm-usage")
        chrome_options.add_argument("--disable-gpu")
        chrome_options.add_argument("--window-size=1920x1080")

        cls.driver = webdriver.Chrome(options=chrome_options)
        cls.driver.maximize_window()
        cls.google_finance_page = GoogleFinancePage(cls.driver)
        cls.given_test_data = ["NFLX", "MSFT", "TSLA"]

    def test_not_in_test_data(self):
        self.google_finance_page.open()
        stocks = self.google_finance_page.get_stocks()
        not_in_test_data = [stock for stock in stocks if stock not in self.given_test_data]
        print(not_in_test_data)

    def test_in_test_data(self):
        self.google_finance_page.open()
        stocks = self.google_finance_page.get_stocks()
        in_test_data = [stock for stock in stocks if stock in self.given_test_data]
        print(in_test_data)

    def test_title(self):
        self.google_finance_page.open()
        title = self.google_finance_page.get_page_title()
        self.assertIn("Google Finance", title, "Page title does not contain 'Google Finance'")

    def test_stock_compare(self):
        self.google_finance_page.open()
        stocks = self.google_finance_page.get_stocks()
        for test_stock in self.given_test_data:
            self.assertIn(test_stock, stocks, f"Stock {test_stock} not found in page stocks")

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

if __name__ == "__main__":
    unittest.main()
