import logging

from dtos import BookCreateDTO, BookResponseDTO, BookStatsDTO, BookUpdateDTO, DeleteBookResponseDTO
from factory import BookFactory
from repository import BookRepository


logger = logging.getLogger(__name__)


class BookService:
    def __init__(self, repository: BookRepository):
        self.repository = repository

    @staticmethod
    def _to_response_dto(book_data: dict) -> BookResponseDTO:
        return BookResponseDTO(**book_data)

    @staticmethod
    def _normalize_author_query(author: str | None) -> str | None:
        if author is None:
            return None

        normalized_author = author.strip().lower()
        if not normalized_author:
            return None

        return normalized_author

    def get_all_books(self, author: str | None = None):
        logger.info("Fetching all books from repository")
        books = self.repository.get_all()

        normalized_author = self._normalize_author_query(author)
        if normalized_author:
            # The filter matches author substrings so queries like "john" still find "John Smith".
            books = [
                book for book in books
                if normalized_author in book["author"].lower()
            ]
            logger.info("Filtered books by author=%s count=%s", author, len(books))

        return [self._to_response_dto(book) for book in books]

    def get_book_stats(self):
        logger.info("Building book statistics from repository")
        books = self.repository.get_all()

        physical_books = sum(1 for book in books if book["book_type"].lower() == "physical")
        ebook_books = sum(1 for book in books if book["book_type"].lower() == "ebook")

        return BookStatsDTO(
            total_books=len(books),
            physical_books=physical_books,
            ebook_books=ebook_books,
        )

    def get_book_by_id(self, book_id: int):
        logger.info("Fetching book by id=%s", book_id)
        book = self.repository.get_by_id(book_id)
        if book is None:
            logger.warning("Book not found in service for id=%s", book_id)
            return None

        return self._to_response_dto(book)

    def create_book(self, book_data: BookCreateDTO):
        book_payload = book_data.model_dump()
        existing_books = self.repository.get_all()

        logger.info("Checking duplicate title for new book title=%s", book_payload["title"])

        if any(existing_book["title"].lower() == book_payload["title"].lower() for existing_book in existing_books):
            logger.warning("Duplicate title detected for title=%s", book_payload["title"])
            raise ValueError("Book already exists")

        new_book = BookFactory.create_book(book_payload)
        created_book = self.repository.create(new_book)
        logger.info("Book created successfully with id=%s title=%s", created_book["id"], created_book["title"])
        return self._to_response_dto(created_book)

    def update_book(self, book_id: int, book_data: BookUpdateDTO):
        logger.info("Updating book id=%s", book_id)
        existing_book = self.repository.get_by_id(book_id)
        if existing_book is None:
            logger.warning("Update failed because book was not found in service id=%s", book_id)
            return None

        update_payload = book_data.model_dump(exclude_none=True)
        updated_book = self.repository.update(book_id, update_payload)
        logger.info("Book updated successfully id=%s", book_id)
        return self._to_response_dto(updated_book)

    def delete_book(self, book_id: int):
        logger.info("Deleting book id=%s", book_id)
        deleted_book = self.repository.delete(book_id)
        if deleted_book is None:
            logger.warning("Delete failed because book was not found in service id=%s", book_id)
            return None

        logger.info("Book deleted successfully id=%s", book_id)
        return DeleteBookResponseDTO(message="Book deleted successfully")