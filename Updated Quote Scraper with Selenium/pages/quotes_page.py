from locators.quotes_page_locators import QuotesPageLocators
from parsers.quote import QuoteParser
from selenium.webdriver.common.by import By
        

class QuotesPage:
    def __init__(self,browser):
        self.browser = browser

    @property
    def quotes(self):
        return [
            QuoteParser(e) for e in self.browser.find_elements(By.CSS_SELECTOR,QuotesPageLocators.QUOTE)
            ]
