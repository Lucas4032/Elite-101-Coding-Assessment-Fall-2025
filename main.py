# Fall 2025 Coding Assesment Created by: Lucas Mowers


from library_books import library_books
from datetime import datetime, timedelta

# -------- Level 1 --------
# TODO: Create a function to view all books that are currently available
# Output should include book ID, title, and author
def viewavailablebooks(books):
    #This prints all books that are available
    print("Available Books:")
    for book in books:
        if book["available"]:
            print(f"{book["id"]}, {book["title"]}, by {book["author"]")
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
            if not book["available"]
            print("That book is already checked out.")
            return
        book["available"] = False
        book["due_date"] = (datetime.now() + timedelta(days=14)).strftime("%m/%d/%Y")
        book ["checkouts"] += 1

        print(f"You have checked out '{book["title"]}'. Due: {book["due_date"]}")
        return
    print("Book ID not found.)
# -------- Level 4 --------
# TODO: Create a function to return a book by ID
# Set its availability to True and clear the due_date

# TODO: Create a function to list all overdue books
# A book is overdue if its due_date is before today AND it is still checked out


# -------- Level 5 --------
# TODO: Convert your data into a Book class with methods like checkout() and return_book()
# TODO: Add a simple menu that allows the user to choose different options like view, search, checkout, return, etc.

# -------- Optional Advanced Features --------
# You can implement these to move into Tier 4:
# - Add a new book (via input) to the catalog
# - Sort and display the top 3 most checked-out books
# - Partial title/author search
# - Save/load catalog to file (CSV or JSON)
# - Anything else you want to build on top of the system!

if __name__ == "__main__":
    # You can use this space to test your functions
    pass
