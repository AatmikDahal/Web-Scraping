from locator.quote_locator import QuotesPage
from parser.html_parser import Quotes_Page,QuotesPage


class getting_data:
    """
    Used to return all the parsed data
    """
    def content():
        parsing = Quotes_Page(QuotesPage.quotes_page)
        for x in parsing.quotes:
            print(x.content)
            

    def tags():
        parsing = Quotes_Page(QuotesPage.quotes_page)
        for x in parsing.quotes:
            print(x.tags)
            

    def author():
        parsing = Quotes_Page(QuotesPage.quotes_page)
        for x in parsing.quotes:
            print(x.author)
            

    def string():
        parsing = Quotes_Page(QuotesPage.quotes_page)
        for x in parsing.quotes:
            print(x)
    
user_choice = {
    "c": getting_data.content,
    "a": getting_data.author,
    "t": getting_data.tags,
    "s": getting_data.string
}

user_prompt = '''
Enter 
c -> for all quotes content,
a -> for all quotes author,
t -> for all quotes tags, 
s -> for all quotes string :  '''



def menu():
    """menu for users to use the program
    """
    user_input = input(user_prompt)
    while user_input != 'q':
        if user_input in ['c','a','t', 's']:
            print('\n')
            user_choice[user_input]()
        else:
            print('Enter a valid character')
        user_input = input(user_prompt)
    else:
        print("\n PROGRAM QUIT")
        
        
menu()