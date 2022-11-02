from app import _books

def print_best_books(books):
    best_books = sorted(books,key=lambda x: x.rating * -1)
    for book in best_books:
        print(f"\n{book}")

def print_cheapest_books(books):
    cheapest_books = sorted(books,key=lambda x: x.price)
    for book in cheapest_books:
        print(f"\n{book}")

def print_books(books):
    for book in books:
        print(f"\n{book}")

def next_available_books(books):
    pass 


USER_PROMPT = '''Enter one of the following
- 'b' to look at 5-star books
- 'c' to look at the cheapest books
- 'p' to print books
- 'n' to just get the next available book on the page
- 'q' to exit
Enter your choice: '''

user_choice = {
    'b':print_best_books,
    'c':print_cheapest_books,
    'n': next_available_books,
    'p':print_books 
}

def menu():
    user_input = input(USER_PROMPT)
    while user_input != 'q':
        if user_input in ['b','c','n','p']:
            user_choice[user_input](_books)
        else:
            print("Enter a valid data")
        user_input = input(USER_PROMPT)


menu()
print("\nProgram Quit")
