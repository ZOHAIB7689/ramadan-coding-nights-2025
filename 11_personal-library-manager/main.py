import json

class BookCollection:
    """A class to manage a collection of books and organize their reading materials."""

    def __init__(self, file_name="data.json"):
        """Initialize the book collection with an empty list and set up the file."""
        self.file_name = file_name
        self.load_books()

    def load_books(self):
        """Load books from the JSON file."""
        try:
            with open(self.file_name, "r") as file:
                self.books = json.load(file)
        except FileNotFoundError:
            self.books = []
        except json.JSONDecodeError:
            print("Error: JSON file is corrupted. Starting with an empty collection.")
            self.books = []

    def save_books(self):
        """Save the current book collection to the JSON file."""
        with open(self.file_name, "w") as file:
            json.dump(self.books, file, indent=4)

    def add_book(self):
        """Add a new book to the collection."""
        title = input("Enter book title: ")
        author = input("Enter book author: ")
        year = input("Enter book year: ")
        book = {"title": title, "author": author, "year": year}
        self.books.append(book)
        self.save_books()
        print("Book added successfully!")

    def remove_book(self):
        """Remove a book from the collection by title."""
        title = input("Enter book title to remove: ")
        self.books = [book for book in self.books if book["title"].lower() != title.lower()]
        self.save_books()
        print("Book removed successfully!")

    def list_books(self):
        """List all books in the collection."""
        if not self.books:
            print("No books in the collection.")
        else:
            for idx, book in enumerate(self.books, start=1):
                print(f"{idx}. {book['title']} by {book['author']} ({book['year']})")

    def find_book(self):
        """Find a book by title."""
        title = input("Enter book title to find: ")
        book = next((book for book in self.books if book["title"].lower() == title.lower()), None)
        if book:
            print(f"Book found: {book['title']} by {book['author']} ({book['year']})")
        else:
            print("Book not found!")

    def run(self):
        while True:
            print("\nBook Manager Menu:")
            print("1. Add book")
            print("2. Remove book")
            print("3. List books")
            print("4. Find book")
            print("5. Quit")
            choice = input("Enter your choice: ")
            if choice == "1":
                self.add_book()
            elif choice == "2":
                self.remove_book()
            elif choice == "3":
                self.list_books()
            elif choice == "4":
                self.find_book()
            elif choice == "5":
                break
            else:
                print("Invalid choice. Please try again.")

if __name__ == "__main__":
    book_collection = BookCollection()
    book_collection.run()