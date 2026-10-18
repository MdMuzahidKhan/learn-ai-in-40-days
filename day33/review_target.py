"""Day 33 code review target.

This file intentionally contains seeded issues for the AI code-review exercise.
"""

from typing import Iterable


def find_books_by_author(books: Iterable[dict], author: str | None):
    # BUG 1: missing null check for author; author can be None here.
    normalized_author = author.strip().lower()

    matched_books = []
    for book in books:
        # BUG 2: logic error; this compares the author query against the title field.
        if normalized_author in book["title"].lower():
            matched_books.append(book)

    # BUG 3: style/convention violation; debug print should not be in production code.
    print(f"Matched {len(matched_books)} books")
    return matched_books


SAMPLE_BOOKS = [
    {"id": 1, "title": "Python Basics", "author": "John Smith"},
    {"id": 2, "title": "OOP in Python", "author": "Jane Doe"},
]


if __name__ == "__main__":
    print(find_books_by_author(SAMPLE_BOOKS, "Jane Doe"))
