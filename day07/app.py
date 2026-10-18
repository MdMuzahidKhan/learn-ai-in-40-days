import logging

from fastapi import Depends, FastAPI, HTTPException, status
from fastapi.middleware.cors import CORSMiddleware

from auth import create_access_token, get_current_user, verify_login
from dependencies import get_book_service
from dtos import (
    BookCreateDTO,
    BookResponseDTO,
    BookStatsDTO,
    BookUpdateDTO,
    DeleteBookResponseDTO,
    LoginRequestDTO,
    TokenResponseDTO,
)
from service import BookService


logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s %(levelname)s %(name)s %(message)s",
)
logger = logging.getLogger(__name__)


app = FastAPI(title="Day 16 Book API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.post("/login", response_model=TokenResponseDTO)
def login(credentials: LoginRequestDTO):
    """Authenticate the demo user and return a bearer access token."""
    logger.info("Login request received for username=%s", credentials.username)
    if not verify_login(credentials.username, credentials.password):
        logger.warning("Login failed for username=%s", credentials.username)
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
        )

    token = create_access_token(credentials.username)
    logger.info("Login succeeded for username=%s", credentials.username)
    return TokenResponseDTO(access_token=token)


@app.get("/books", response_model=list[BookResponseDTO])
def get_books(author: str | None = None, service: BookService = Depends(get_book_service)):
    """Return all books or filter them by an author substring, case-insensitively."""
    logger.info("Get books request received author=%s", author)
    return service.get_all_books(author=author)


@app.get("/books/stats", response_model=BookStatsDTO)
def get_book_stats(service: BookService = Depends(get_book_service)):
    """Return a small inventory summary for the current book list."""
    logger.info("Get book stats request received")
    return service.get_book_stats()


@app.get("/books/{book_id}", response_model=BookResponseDTO)
def get_book(book_id: int, service: BookService = Depends(get_book_service)):
    """Return a single book by id, or 404 when it does not exist."""
    logger.info("Get book request received for book_id=%s", book_id)
    book = service.get_book_by_id(book_id)
    if book is None:
        logger.warning("Book not found for book_id=%s", book_id)
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Book not found")
    return book


@app.post("/books", response_model=BookResponseDTO, status_code=status.HTTP_201_CREATED)
def create_book(
    book: BookCreateDTO,
    current_user: str = Depends(get_current_user),
    service: BookService = Depends(get_book_service),
):
    """Create a new book record for an authenticated user."""
    logger.info("Create book request received for user=%s title=%s", current_user, book.title)
    try:
        return service.create_book(book)
    except ValueError as error:
        logger.warning("Create book rejected for user=%s reason=%s", current_user, str(error))
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(error))
    except Exception as error:
        logger.error("Unexpected create book error for user=%s error=%s", current_user, str(error))
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Internal server error")


@app.put("/books/{book_id}", response_model=BookResponseDTO)
def update_book(
    book_id: int,
    book_update: BookUpdateDTO,
    current_user: str = Depends(get_current_user),
    service: BookService = Depends(get_book_service),
):
    """Update an existing book record for an authenticated user."""
    logger.info("Update book request received for user=%s book_id=%s", current_user, book_id)
    updated_book = service.update_book(book_id, book_update)

    if updated_book is None:
        logger.warning("Update failed because book was not found book_id=%s", book_id)
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Book not found")

    return updated_book


@app.delete("/books/{book_id}", response_model=DeleteBookResponseDTO)
def delete_book(
    book_id: int,
    current_user: str = Depends(get_current_user),
    service: BookService = Depends(get_book_service),
):
    """Delete a book record for an authenticated user."""
    logger.info("Delete book request received for user=%s book_id=%s", current_user, book_id)
    deleted_book = service.delete_book(book_id)

    if deleted_book is None:
        logger.warning("Delete failed because book was not found book_id=%s", book_id)
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Book not found")

    return deleted_book