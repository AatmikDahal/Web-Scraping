from bs4 import BeautifulSoup
from locator.quote_locator import QuoteItemLocator, QuoteLocator, QuotesPage
from locator.quote_locator import QuotesPage

class Quotes_Page:
    """
    Parses the html data retrieved from the requests library and passes it to ParsingItems class
    one by one
    """
    def __init__(self, page):   
        self.soup = BeautifulSoup(page, 'html.parser') # html of quote pages being instantiated to being parsed

    @property
    def quotes(self): #returns ParsingItems Class
        return  [ParsingItems(e) for e in self.soup.select(QuoteLocator.QUOTE)]





class ParsingItems:
    
    """
    Parses the the html data and 
    - gets content,tags and authors using BeautifulSoup and Locator created 
    - returns __repr__ using the parsed data
    """
    def __init__(self,parent):
        self.parent = parent

    def __repr__(self):
        return f'< {self.content} -----> by {self.author} >'
    
    @property
    def content(self): # returns content of the quotes present in the page
        locator = QuoteItemLocator.CONTENT
        return self.parent.select_one(locator).string

    @property
    def author(self): # returns all the names of authors present in the page
        locator = QuoteItemLocator.AUTHOR
        return self.parent.select_one(locator).string

    @property
    def tags(self):
            locator = QuoteItemLocator.TAGS
            tags =  self.parent.select(locator) # returns all tags present in the page
            tags_list = [tags]
            for x in tags_list:
                for y in x:
                    print(y.string) # all the tags in the page as individual strings

        
