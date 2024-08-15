from selenium.webdriver.common.by import By
from PageFactoryTest.pages.base_page import BasePage
from seleniumpagefactory import PageFactory


class GoogleFinancePage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.url = "https://www.google.com/finance/"
        self.driver.get(self.url)
        self.elements_xpath = (By.XPATH, "//section[@aria-labelledby='smart-watchlist-title']//div[contains(@class, 'COaKTb')]")

    def open(self):
        super().open(self.url)

    def get_stocks(self):
        stocks_elements = self.find_elements(*self.elements_xpath)
        return [element.text for element in stocks_elements]

    def get_page_title(self):
        return self.driver.title