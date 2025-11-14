# Fall 2025 Coding Assesment Created by: Lucas Mowers
#Date: 11/13/25

#This also helped me learn date time since I hadn't really used it much before hand
#https://docs.python.org/3/library/datetime.html

#I also refreshed myself on classes using this https://docs.python.org/3/tutorial/classes.html

from library_books import library_books
from datetime import datetime, timedelta

# -------- Level 1 --------
# TODO: Create a function to view all books that are currently available
# Output should include book ID, title, and author
def viewavailablebooks(books):
    #This prints all books that are available
    print("Available Books:")
    for book in books:
        #when putting in viewavailablebooks(librarybooks) it prints all the available
        if  book["available"]:
           print(f"{book['id']}, {book['title']}, by {book['author']}")
    print()

# -------- Level 2 --------
# TODO: Create a function to search books by author OR genre
# Search should be case-insensitive
# Return a list of matching books
def search_books(books, term):
    #This will return the books where the author or genre would match the term
    term = term.lower()
    results = []

    for book in books:
        if term in book["author"].lower() or term in book["genre"].lower():
            results.append(book)
    return results
# -------- Level 3 --------
# TODO: Create a function to checkout a book by ID
# If the book is available:
#   - Mark it unavailable
#   - Set the due_date to 2 weeks from today
#   - Increment the checkouts counter
# If it is not available:
#   - Print a message saying it's already checked out

def checkout_book(books, book_id):
    #checks the book out if its available

    for book in books:
        if book["id"] == book_id:
            if not book["available"]:
                print("That book is already checked out.")
                return
        book["available"] = False
        book["due_date"] = (datetime.now() + timedelta(days=14)).strftime("%m/%d/%Y")
        book ["checkouts"] += 1

        print(f"You have checked out '{book["title"]}'. Due: {book["due_date"]}")
        return
    #if it didnt find the book id it just returns not found
    print("Book ID not found.")
# -------- Level 4 --------
# TODO: Create a function to return a book by ID
# Set its availability to True and clear the due_date

def return_book(books, book_id):
    #this will return the books with the id to know which book
    for book in books:
        if book["id"] == book_id:
            book["available"] = True
            book["due_date"] = None
            #this will print this when you return that book
            print(f"'{book['title']}' has been returned.")
            return
    #this will happen if that book id does not exist
    print("Book ID not found")
# TODO: Create a function to list all overdue books
# A book is overdue if its due_date is before today AND it is still checked out
def viewoverdue_books(books):
    #this will list all overdue books (like said in the prompt)
    print("Overdue Books:")
    today = datetime.now()
    found = False

    for book in books:
        if not book["available"] and book["due_date"]:
            due = datetime.strptime(book["due_date"], "%m/%d/%Y")
            if due < today:
                found = True
                print(f"{book['id']}: {book['title']} (Due: {book['due_date']})")
    if not found:
        print("No overdue books.")
    print()
# -------- Level 5 --------
# TODO: Convert your data into a Book class with methods like checkout() and return_book()
# TODO: Add a simple menu that allows the user to choose different options like view, search, checkout, return, etc.
#this is all the data being converted into a book class
class Book:
    def __init__(self, id, title, author, genre, available, due_date, checkouts):
        self.id = id
        self.title = title
        self.author = author
        self.genre = genre
        self.available = available
        self.due_date = due_date
        self.checkouts = checkouts
    def checkout (self):
        if not self.available:
            print(f"{self.title} is already checked out.")
            return
        self.available = False
        due = datetime.now() + timedelta(days=14)
        self.due_date = due.strftime("%m/%d/%Y")
        self.checkouts += 1
        print(f"You checked out '{self.title}'. Due: {self.due_date}")

    def return_book(self):
        self.available = True
        self.due_date = None
        print(f"{self.title} has been returned.")
    def is_overdue(self):
        if self.available or not self.due_date:
            return False
        due = datetime.strptime(self.due_date, "%m/%d/%Y")
        return due < datetime.now()

#This helps convert the dictionaries to book objects

def convert_to_objects():
    objects = []
    for b in library_books:
        objects.append(Book(
            b["id"], b["title"], b["author"], b["genre"],
            b["available"], b["due_date"], b["checkouts"]
        ))
    return objects

#this is the simple menu

def menu():
    books = convert_to_objects()

    while True:
        print("Library Menu")
        print("1. View available books")
        print("2. Search books")
        print("3. Checkout book")
        print("4. Return book")
        print("5. View overdue books")
        print("0. Quit")

        choice = input("Choose an option: ")
        
        if choice == "1":
            for b in books:
                if b.available:
                    print(f"{b.id}: {b.title} by {b.author}")

        elif choice == "2":
            term = input("Search author or genre: ").lower()
            for b in books:
                if term in b.author.lower() or term in b.genre.lower():
                    print(f"{b.id}: {b.title}")

        elif choice == "3":
            book_id = input("Enter book ID: ")
            for b in books:
                if b.id == book_id:
                    b.checkout()

        elif choice == "4":
            book_id = input("Enter book ID: ")
            for b in books:
                if b.id == book_id:
                    b.return_book()

        elif choice == "5":
            for b in books:
                if b.is_overdue():
                    print(f"{b.id}: {b.title} (Due: {b.due_date})")

        elif choice == "0":
            print("Goodbye.")
            return
        else:
            print("Invalid option.")


#This is where i tested
if __name__ == "__main__":
    menu()

