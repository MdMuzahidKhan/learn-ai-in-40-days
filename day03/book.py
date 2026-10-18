# Approach: Use an abstract base class for shared book behavior and subclasses for specific book types.

from abc import ABC, abstractmethod


class Book(ABC):
    def __init__(self, book_id, title, author):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.is_borrowed = False

    @abstractmethod
    def get_loan_period(self):
        pass

    def get_description(self):
        return f"{self.title} by {self.author}"


class PhysicalBook(Book):
    def __init__(self, book_id, title, author, shelf_number):
        super().__init__(book_id, title, author)
        self.shelf_number = shelf_number

    def get_loan_period(self):
        return 14

    def get_description(self):
        return f"Physical Book: {self.title} by {self.author}, Shelf: {self.shelf_number}"


class EBook(Book):
    def __init__(self, book_id, title, author, file_format):
        super().__init__(book_id, title, author)
        self.file_format = file_format

    def get_loan_period(self):
        return 7

    def get_description(self):
        return f"EBook: {self.title} by {self.author}, Format: {self.file_format}"