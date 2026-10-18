# Approach: Use a repository class to separate data access from API route logic.

from abc import ABC, abstractmethod
import logging


logger = logging.getLogger(__name__)


class BookRepository(ABC):
    @abstractmethod
    def get_all(self):
        pass

    @abstractmethod
    def get_by_id(self, book_id):
        pass

    @abstractmethod
    def create(self, book_data):
        pass

    @abstractmethod
    def update(self, book_id, book_data):
        pass

    @abstractmethod
    def delete(self, book_id):
        pass


class InMemoryBookRepository(BookRepository):
    def __init__(self):
        self.books = [
            {
                "id": 1,
                "title": "Python Basics",
                "author": "John Smith",
                "year": 2021,
                "book_type": "physical",
                "extra_info": "A12",
            },
            {
                "id": 2,
                "title": "OOP in Python",
                "author": "Jane Doe",
                "year": 2022,
                "book_type": "ebook",
                "extra_info": "PDF",
            },
        ]

    def get_all(self):
        logger.info("Repository get_all called count=%s", len(self.books))
        return self.books

    def get_by_id(self, book_id):
        logger.info("Repository lookup for book_id=%s", book_id)
        for book in self.books:
            if book["id"] == book_id:
                logger.info("Repository found book_id=%s", book_id)
                return book
        logger.warning("Repository did not find book_id=%s", book_id)
        return None

    def create(self, book_data):
        new_id = max((book["id"] for book in self.books), default=0) + 1
        book_data["id"] = new_id
        self.books.append(book_data)
        logger.info("Repository created book_id=%s", new_id)
        return book_data

    def update(self, book_id, book_data):
        logger.info("Repository update called for book_id=%s", book_id)
        book = self.get_by_id(book_id)
        if book is None:
            return None

        book.update(book_data)
        logger.info("Repository updated book_id=%s", book_id)
        return book

    def delete(self, book_id):
        logger.info("Repository delete called for book_id=%s", book_id)
        book = self.get_by_id(book_id)
        if book is None:
            return None

        self.books.remove(book)
        logger.info("Repository deleted book_id=%s", book_id)
        return book