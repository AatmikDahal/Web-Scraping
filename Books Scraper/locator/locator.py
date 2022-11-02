import requests

class BooksPageLocator:
    page = requests.get("https://books.toscrape.com/").content
    

class BooksLocator:
    books = 'div.page_inner div.col-sm-8.col-md-9 section li.col-xs-6.col-sm-4.col-md-3.col-lg-3'
    pager = 'div.page_inner ul.pager li.current'

class BooksItemLocator:
    TITLE = "article.product_pod h3 a"
    RATING = "article.product_pod p.star-rating"
    PRICE = "article.product_pod p.price_color"
    
