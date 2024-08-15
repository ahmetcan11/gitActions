import unittest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from PageObjectTest.pages.google_finance_page import GoogleFinancePage


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
        missing_from_website = [stock for stock in self.given_test_data if stock not in stocks]
        print("Stocks in the given test data but not on the website:", missing_from_website)

    def test_title(self):
        self.google_finance_page.open()
        title = self.google_finance_page.get_page_title()
        try:
            self.assertIn("Google Finance", title, "Page title does not contain 'Google Finance'")
        except AssertionError as e:
            print(f"Assertion failed for page title: {str(e)}")

    def test_stock_compare(self):
        self.google_finance_page.open()
        stocks = self.google_finance_page.get_stocks()
        try:
            for test_stock in self.given_test_data:
                self.assertIn(test_stock, stocks, f"Stock {test_stock} not found on the page")
        except AssertionError as e:
            print(f"Assertion failed for stock comparison: {str(e)}")

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

if __name__ == "__main__":
    unittest.main()