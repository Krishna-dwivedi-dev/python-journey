# Day 4: Bonus Q1 - Library Management System

class Library:
    def __init__(self, name, total_books):
        self.name = name
        self.total_books = total_books
        self.books_issued = 0

    def book_issued(self, count):
        if count > self.total_books:
            print("Not enough books available!")
        else:
            self.books_issued += count
            available = self.total_books - self.books_issued
            print(f"Books Issued! Available: {available}")

    def return_book(self, count):
        if count > self.books_issued:
            print("Can't return more books than issued!")
        else:
            self.books_issued -= count
            print(f"Books Returned! Available: {self.total_books - self.books_issued}")

    def display(self):
        print(f"Library: {self.name} | Total: {self.total_books} | Issued: {self.books_issued} | Available: {self.total_books - self.books_issued}")

# Test
lib = Library("Kavi Narmad", 1000)
lib.display()
lib.book_issued(145)
lib.return_book(50)
lib.display()