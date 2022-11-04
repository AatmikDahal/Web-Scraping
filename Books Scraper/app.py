import requests
from parser.html_parser import  BooksParser 


_books = []#['{self.title} for {self.price} with {self.rating} star rating \n']


base_page_content = requests.get('https://books.toscrape.com/').content
page = BooksParser(base_page_content)


for i in range(page.page_nums):
    url = f'https://books.toscrape.com/catalogue/page-{i+1}.html'
    page_content = requests.get(url).content
    page = BooksParser(page_content)
    _books.extend(page.parsing)
    



