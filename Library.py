# 1. Create Library Class
class Library:
    @classmethod
    def view_all_books(cls):
        print("\nAll Books:")
        for book in Book.get_all_books():
            book.view_book_info()
    @classmethod
    def borrow_book(cls, book_id):
        for book in Book.get_all_books():
            if book._book_id == book_id:
                book.borrow_book()
                return
        print("Invalid Book ID.")    

    @classmethod
    def return_book(cls, book_id):
        for book in Book.get_all_books():
            if book._book_id == book_id:
                book.return_book()
                return
        print("Invalid Book ID.")              

# 2. Create Book Class
class Book():
    total_books = 0
    book_list = []  # 9.Protected

    def __init__(self, book_id, title, author):
# 3. Initialized Book Object
        self._book_id = book_id
        self._title = title
        self._author = author
        self._availability = True
        Book.total_books += 1
        Book.book_list.append(self)

# 4. Implement borrow_book() method
    def borrow_book(self):
        if self._availability:
            self._availability = False
            print(f"Book '{self._title}' borrowed successfully.")
        else:
            print("Book is already borrowed.")

# 5. Implement return_book() method
    def return_book(self):
        if not self._availability:
            self._availability = True
            print(f"Book '{self._title}' returned successfully.")
        else:
            print("Book is already available.")
       

# 6. Implement view_book_info() method
    def view_book_info(self):
        availability_status = "Available" if self._availability else "Not Available"
        print(f"Book ID: {self._book_id}, Title: {self._title}, Author: {self._author}, Availability: {availability_status}")

    @classmethod
    def get_all_books(cls):
        return cls.book_list

if __name__ == "__main__":
    book1 = Book(101, "The Lord of the Rings", "J.R.R. Tolkien")
    book2 = Book(102, "To Kill a Mockingbird", "Harper Lee")
    book3 = Book(103, "Python Programming", "John Doe")
    book4 = Book(104, "Deep Learning", "Yann LeCun")
    book5 = Book(105, "Python for Data Analysis", "Wes McKinney")
    book6 = Book(106, "1984", "George Orwell")
    book7 = Book(107, "Artificial Intelligence", "Marvin Minsky")

    print(f"\nTotal books in the library: {Book.total_books}")
# 7. Menu System
    while True:
        print("\n-------Welcome to the Library-------")
        print("1. View All Books")
        print("2. Borrow Book")
        print("3. Return Book")
        print("4. Exit")

        choice = input("Enter your choice: ")
        if choice == '1':
            Library.view_all_books()
        elif choice == '2':
            book_id = int(input("Enter Book ID to borrow: "))
            Library.borrow_book(book_id)
        elif choice == '3':
            book_id = int(input("Enter Book ID to return: "))
            Library.return_book(book_id)
        elif choice == '4':
            print("Exit...")
            break
        else:
            print("Invalid choice. Please try again.")

