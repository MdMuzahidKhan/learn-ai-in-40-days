from typing import Optional

from pydantic import BaseModel, Field


class BookResponseDTO(BaseModel):
    id: int
    title: str
    author: str
    year: int
    book_type: str
    extra_info: str


class BookCreateDTO(BaseModel):
    title: str = Field(min_length=1)
    author: str = Field(min_length=1)
    year: int = Field(ge=1)
    book_type: str = Field(min_length=1)
    extra_info: str = Field(min_length=1)


class BookUpdateDTO(BaseModel):
    title: Optional[str] = Field(default=None, min_length=1)
    author: Optional[str] = Field(default=None, min_length=1)
    year: Optional[int] = Field(default=None, ge=1)
    book_type: Optional[str] = Field(default=None, min_length=1)
    extra_info: Optional[str] = Field(default=None, min_length=1)


class DeleteBookResponseDTO(BaseModel):
    message: str


class BookStatsDTO(BaseModel):
    total_books: int
    physical_books: int
    ebook_books: int


class LoginRequestDTO(BaseModel):
    username: str = Field(min_length=1)
    password: str = Field(min_length=1)


class TokenResponseDTO(BaseModel):
    access_token: str
    token_type: str = "bearer"