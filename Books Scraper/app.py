from cgi import print_arguments
from parser.html_parser import  BooksParser 
from locator.locator import  BooksPageLocator

_books = [] #['{self.title} for {self.price} with {self.rating} star rating \n']

parsed = BooksParser(BooksPageLocator.page)
_books.extend(parsed.parsing)

