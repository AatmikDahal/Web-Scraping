from app import _books

class Sorting:
    
    books_list = []
    
    def __init__(self,book) -> None:
        self.parent = book  
    
    def print_best_books(self):
        best_books = sorted(self.parent ,key=lambda x: x.rating * -1)
        for book in best_books:
            print(f"\n{book}")
            
    
    def print_cheapest_books(self):
        cheapest_books = sorted(self.parent,key=lambda x: x.price)
        for book in cheapest_books:
            print(f"\n{book}")

    def print_books(self):
        book =self.parent
        for _ in book:
            print(_)
            
    
            
USER_PROMPT = '''Enter one of the following
- 'b' to look at 5-star books
- 'c' to look at the cheapest books
- 'p' to print books
- 'q' to exit
Enter your choice: '''

Sorted = Sorting(_books)

user_choice = {
    'b':Sorted.print_best_books,
    'c':Sorted.print_cheapest_books,
    'p':Sorted.print_books,
}

def menu():
    user_input = input(USER_PROMPT)
    while user_input != 'q':
        if user_input in ['b','c','p']:
            user_choice[user_input]()
        else:
            print("Enter a valid data")
        user_input = input(USER_PROMPT)


menu()
print("\nProgram Quit")
