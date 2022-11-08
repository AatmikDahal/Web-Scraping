from selenium import webdriver
from pages.quotes_page import QuotesPage

chrome_driver_path= r"C:\Users\lenovo\Downloads\chromedriver_win32\chromedriver.exe"
brave_path = r"C:\Program Files\BraveSoftware\Brave-Browser\Application\brave.exe"

Option = webdriver.ChromeOptions()
Option.binary_location = brave_path


browser = webdriver.Chrome(executable_path=chrome_driver_path,options=Option)

browser.get('https://quotes.toscrape.com/')

page = QuotesPage(browser)

for quote in page.quotes:
    print(quote)
