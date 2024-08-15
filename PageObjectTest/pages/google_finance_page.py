from selenium.webdriver.common.by import By
from PageObjectTest.pages.base_page import BasePage

class GoogleFinancePage(BasePage):
    elementsXpath = (By.XPATH, "//section[@aria-labelledby='smart-watchlist-title']//div[contains(@class, 'COaKTb')]")

    def __init__(self, driver):
        super().__init__(driver)
        self.url = "https://www.google.com/finance/"

    def open(self):
        self.driver.get(self.url)

    def get_stocks(self):
        return [element.text for element in self.find_elements(*self.elementsXpath)]

    def get_page_title(self):
        return self.driver.title
