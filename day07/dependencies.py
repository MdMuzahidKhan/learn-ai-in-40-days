from repository import BookRepository, InMemoryBookRepository
from service import BookService


repository_instance = InMemoryBookRepository()


def get_repository() -> BookRepository:
    return repository_instance


def get_book_service() -> BookService:
    repository = get_repository()
    return BookService(repository)