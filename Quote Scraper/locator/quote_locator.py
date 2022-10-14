import requests

class QuotesPage:
    quotes_page = requests.get('http://quotes.toscrape.com/').content  # retrieves html data of the page following the link 

class QuoteLocator:
    QUOTE = 'div.quote' #locates all the quotes in the page


class QuoteItemLocator:
    CONTENT = 'div.quote span.text' #locates the content of the quote ->div.quote
    AUTHOR = 'div.quote small.author' #locates the author of the quote ->div.quote
    TAGS = 'div.quote div.tags a.tag' #locates the tags of the quotes ->div.quotes