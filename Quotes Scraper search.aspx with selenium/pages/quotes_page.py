from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import NoSuchElementException
from typing import List
from selenium.webdriver.support.ui import Select
from locators.quotes_page_locators import QuotesPageLocators
from parsers.quote import QuoteParser
from selenium.webdriver.common.by import By
        

class QuotesPage:
    def __init__(self,browser):
        self.browser = browser # gets the quotes.toscrape.com/search.aspx's html/css/javascript 

    @property
    def quotes(self)->List[QuoteParser]:
        quote =  [
            QuoteParser(e) for e in self.browser.find_elements(By.CSS_SELECTOR,QuotesPageLocators.QUOTE)
            ] # -> ['Quote1','Quote2','Quote3']
        return quote[0]
    
    @property
    def author_dropdown(self) -> Select:
        element = self.browser.find_element(By.CSS_SELECTOR,QuotesPageLocators.AUTHOR_DROPDOWN) # find the author dropdown in the page 
        return Select(element) #selects the name of the author tag in the website
    
    @property
    def tag_dropdown(self) -> Select:
        element = self.browser.find_element(By.CSS_SELECTOR,QuotesPageLocators.TAG_DROPDOWN)
        return Select(element) #selects the name of the tag *tag* in the website)

    @property
    def search_button(self):
        return self.browser.find_element(By.CSS_SELECTOR, QuotesPageLocators.SEARCH_BUTTON)
    
    @property
    def get_available_tags(self):
        available_tags = [option.text.strip() for option in self.tag_dropdown.options]
        return available_tags[1:]
    
    def select_author(self,author_name:str):
        self.author_dropdown.select_by_visible_text(author_name) # selects the user's author in the site

    def select_tag(self, tag_name:str):
        self.tag_dropdown.select_by_visible_text(tag_name)# selects the user's tag in the site
    
    def search_for_quote(self,author:str,tag:str)-> List[QuoteParser]:
        #adding the wait func to the program
        WebDriverWait(self.browser,10).until(
            expected_conditions.presence_of_element_located(
                (By.CSS_SELECTOR,QuotesPageLocators.TAG_DROPDOWN_VALUE_OPTION) 
            ))
        try:
            self.select_tag(tag)
        except NoSuchElementException:
            raise InvalidTagForAuthorError(
                f"Author {author} does not have any quotes with tag {tag}" )
        except Exception as e:
            print(e)   
            print("An unknown error has occurred. Please try again later")
        self.search_button.click()
        print(self.quotes)
        
        
class InvalidTagForAuthorError(ValueError):
    pass