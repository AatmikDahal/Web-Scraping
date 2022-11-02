import re
from bs4 import BeautifulSoup
from locator.locator import BooksItemLocator, BooksLocator

class BooksParser():
    def __init__(self,page) -> None:
        self.soup = BeautifulSoup(page,'html.parser') # parsing the full books web-page
        
    @property 
    def parsing(self):
        return [BooksItemParser(e) for e in self.soup.select(BooksLocator.books)]
    
    @property
    def page_nums(self):
        pattern = 'Page [0-9]+ of ([0-9]+)'
        pager = self.soup.select_one(BooksLocator.pager).string.strip()
        matcher = re.findall(pattern,pager) # in findall it give the patter inside of () but in search it give ['full match','()']
        return matcher[0]
        
        
class BooksItemParser:

    RATING = {
        'One': 1,
        "Two": 2, 
        "Three": 3,
        "Four": 4, 
        "Five": 5
    }
    
    def __init__(self,parent) -> None:
        self.parent = parent

    
    def __repr__(self):
        return f'{self.title} for {self.price} with {self.rating} star rating\n'
    
    @property
    def title(self):
        book_title = self.parent.select_one(BooksItemLocator.TITLE).string
        return book_title
    
    
    @property
    def price(self):
        book_price = self.parent.select_one(BooksItemLocator.PRICE)
        return book_price.string    

    @property
    def rating(self):
        book_rating = self.parent.select_one(BooksItemLocator.RATING).attrs['class']
        rating_class = [rating for rating in book_rating if rating !='star-rating'] #one , two , three , four ,five 
        star_rating = BooksItemParser.RATING.get(rating_class[0])
        return star_rating
