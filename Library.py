class Library:
    def view_all_books(self):
        print("\nAll Books:")
        for book in Book.book_list:
            book.view_book_info()

    def borrow_book(self, book_id):
        for book in Book.book_list:
            if book._book_id == book_id:
                book.borrow_book()
                return
        print("Invalid Book ID.")

    def return_book(self, book_id):
        for book in Book.book_list:
            if book._book_id == book_id:
                book.return_book()
                return
        print("Invalid Book ID.")

class Book:
    total_books = 0
    book_list = []

    def __init__(self, book_id, title, author):
        self._book_id = book_id
        self._title = title
        self._author = author
        self._availability = True
        Book.total_books += 1
        Book.book_list.append(self)

    def borrow_book(self):
        if self._availability:
            self._availability = False
            print(f"Book '{self._title}' borrowed successfully.")
        else:
            print("Book is already borrowed.")

    def return_book(self):
        if not self._availability:
            self._availability = True
            print(f"Book '{self._title}' returned successfully.")
        else:
            print("Book is already available.")

    def view_book_info(self):
        availability_status = "Available" if self._availability else "Not Available"
        print(f"Book ID: {self._book_id}, " f"Title: {self._title}, " f"Author: {self._author}, " f"Availability: {availability_status}")

if __name__ == "__main__":
    book1 = Book(101, "The Lord of the Rings", "J.R.R. Tolkien")
    book2 = Book(102, "To Kill a Mockingbird", "Harper Lee")
    book3 = Book(103, "Python Programming", "John Doe")
    book4 = Book(104, "Deep Learning", "Yann LeCun")
    book5 = Book(105, "Python for Data Analysis", "Wes McKinney")
    book6 = Book(106, "1984", "George Orwell")
    book7 = Book(107, "Artificial Intelligence", "Marvin Minsky")

    library = Library()

    print(f"\nTotal books in the library: {Book.total_books}")

    while True:
        print("\n-------Welcome to the Library-------")
        print("1. View All Books")
        print("2. Borrow Book")
        print("3. Return Book")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            library.view_all_books()

        elif choice == '2':
            book_id = int(input("Enter Book ID to borrow: "))
            library.borrow_book(book_id)

        elif choice == '3':
            book_id = int(input("Enter Book ID to return: "))
            library.return_book(book_id)

        elif choice == '4':
            print("Exiting...")
            break

        else:
            print("Invalid choice. Please try again.")