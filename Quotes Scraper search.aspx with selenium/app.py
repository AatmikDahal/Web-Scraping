from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from pages.quotes_page import QuotesPage

author = input("Enter the name of the author, to find their quote in our catalogue: ") #getting user input on the author they want 

chrome_driver_path= Service(r"C:\Users\lenovo\Downloads\chromedriver_win32\chromedriver.exe") #chromeDriver path
brave_path = r"C:\Program Files\BraveSoftware\Brave-Browser\Application\brave.exe" #browser of choice application's path only req for anything else than chrome for chrome not req
# r'*string*' returns raw form of the string    


Option = webdriver.ChromeOptions()
Option.binary_location = brave_path # choosing brave as my browser of choice instead of default chrome
Option.add_experimental_option('excludeSwitches', ['enable-logging']) # removing logging / webdriver messages 

browser = webdriver.Chrome(service=chrome_driver_path,options=Option)

browser.get('https://quotes.toscrape.com/search.aspx')
#launching browser and going the specific page

page = QuotesPage(browser) # giving the page's html/css/javascript to QuotesPage
page.select_author(author)
tags = page.get_available_tags

selected_tag = input("Please select one of the following tags \n[{}] : ".format(" | ".join(tags))).lower()

page.search_for_quote(author,selected_tag)




