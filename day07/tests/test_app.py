from copy import deepcopy
import os
import secrets
import sys

import pytest
from fastapi.testclient import TestClient

sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))

# Use disposable test-only configuration, never inherited developer secrets.
# Restore the process environment immediately after importing the application.
with pytest.MonkeyPatch.context() as test_environment:
    test_environment.setenv("SECRET_KEY", secrets.token_urlsafe(48))
    test_environment.setenv("DEMO_USERNAME", "test-" + secrets.token_hex(8))
    test_environment.setenv("DEMO_PASSWORD", secrets.token_urlsafe(32))
    import app as app_module
    import auth as auth_module

import dependencies as dependencies_module


@pytest.fixture
def client():
    original_books = deepcopy(dependencies_module.repository_instance.books)
    test_client = TestClient(app_module.app)
    yield test_client
    dependencies_module.repository_instance.books = deepcopy(original_books)

@pytest.fixture
def sample_books():
    return [
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


@pytest.fixture
def mocked_books(sample_books):
    dependencies_module.repository_instance.books = deepcopy(sample_books)
    return dependencies_module.repository_instance.books


def get_auth_headers(client):
    response = client.post(
        "/login",
        json={"username": auth_module.DEMO_USERNAME, "password": auth_module.DEMO_PASSWORD},
    )
    assert response.status_code == 200
    token = response.json()["access_token"]
    return {"Authorization": f"Bearer {token}"}


def test_login_success(client):
    response = client.post(
        "/login",
        json={"username": auth_module.DEMO_USERNAME, "password": auth_module.DEMO_PASSWORD},
    )

    assert response.status_code == 200
    assert response.json()["token_type"] == "bearer"
    assert response.json()["access_token"]


def test_login_failure(client):
    response = client.post(
        "/login",
        json={"username": "wrong", "password": "wrong"},
    )

    assert response.status_code == 401
    assert response.json()["detail"] == "Incorrect username or password"


def test_get_books_success(client, mocked_books):
    response = client.get("/books")

    assert response.status_code == 200
    assert response.json() == mocked_books


def test_get_book_stats(client, mocked_books):
    response = client.get("/books/stats")

    assert response.status_code == 200
    assert response.json() == {
        "total_books": 2,
        "physical_books": 1,
        "ebook_books": 1,
    }


def test_get_books_filter_by_author_exact_match(client, mocked_books):
    response = client.get("/books?author=Jane Doe")

    assert response.status_code == 200
    result = response.json()
    assert len(result) == 1
    assert result[0]["author"] == "Jane Doe"


def test_get_books_filter_by_author_case_insensitive(client, mocked_books):
    response = client.get("/books?author=john smith")

    assert response.status_code == 200
    result = response.json()
    assert len(result) == 1
    assert result[0]["author"] == "John Smith"


def test_get_books_filter_by_author_no_match(client, mocked_books):
    response = client.get("/books?author=Unknown Author")

    assert response.status_code == 200
    result = response.json()
    assert result == []


def test_get_books_ignores_blank_author_query(client, mocked_books):
    response = client.get("/books?author=   ")

    assert response.status_code == 200
    assert response.json() == mocked_books


def test_get_book_success(client, mocked_books):
    response = client.get("/books/1")

    assert response.status_code == 200
    assert response.json()["id"] == 1
    assert response.json()["title"] == "Python Basics"
    assert response.json()["book_type"] == "physical"
    assert response.json()["extra_info"] == "A12"


def test_get_book_failure_not_found(client, mocked_books):
    response = client.get("/books/999")

    assert response.status_code == 404
    assert response.json()["detail"] == "Book not found"


def test_post_book_success(client, mocked_books):
    new_book = {
        "title": "Clean Code",
        "author": "Robert C. Martin",
        "year": 2008,
        "book_type": "physical",
        "extra_info": "B15",
    }

    response = client.post("/books", json=new_book, headers=get_auth_headers(client))

    assert response.status_code == 201
    assert response.json()["title"] == "Clean Code"
    assert response.json()["author"] == "Robert C. Martin"
    assert response.json()["year"] == 2008
    assert response.json()["book_type"] == "physical"
    assert response.json()["extra_info"] == "B15"
    assert response.json()["id"] == 3


def test_post_book_failure_duplicate_title(client, mocked_books):
    duplicate_book = {
        "title": "Python Basics",
        "author": "Someone Else",
        "year": 2024,
        "book_type": "ebook",
        "extra_info": "EPUB",
    }

    response = client.post("/books", json=duplicate_book, headers=get_auth_headers(client))

    assert response.status_code == 400
    assert response.json()["detail"] == "Book already exists"


def test_post_book_failure_invalid_type(client, mocked_books):
    invalid_book = {
        "title": "Strange Book",
        "author": "Guest Author",
        "year": 2024,
        "book_type": "audiobook",
        "extra_info": "MP3",
    }

    response = client.post("/books", json=invalid_book, headers=get_auth_headers(client))

    assert response.status_code == 400
    assert response.json()["detail"] == "Invalid book type: audiobook"


def test_post_book_failure_without_token(client, mocked_books):
    response = client.post(
        "/books",
        json={
            "title": "Tokenless Book",
            "author": "Guest",
            "year": 2024,
            "book_type": "physical",
            "extra_info": "C10",
        },
    )

    assert response.status_code == 401


def test_put_book_success(client, mocked_books):
    updated_book = {
        "title": "Python Basics Updated",
        "author": "John Smith",
        "year": 2024,
        "book_type": "physical",
        "extra_info": "A15",
    }

    response = client.put("/books/1", json=updated_book, headers=get_auth_headers(client))

    assert response.status_code == 200
    assert response.json()["id"] == 1
    assert response.json()["title"] == "Python Basics Updated"
    assert response.json()["author"] == "John Smith"
    assert response.json()["year"] == 2024
    assert response.json()["book_type"] == "physical"
    assert response.json()["extra_info"] == "A15"


def test_put_book_failure_not_found(client, mocked_books):
    updated_book = {
        "title": "Unknown Book",
        "author": "Nobody",
        "year": 2024,
        "book_type": "ebook",
        "extra_info": "MOBI",
    }

    response = client.put("/books/999", json=updated_book, headers=get_auth_headers(client))

    assert response.status_code == 404
    assert response.json()["detail"] == "Book not found"


def test_put_book_failure_without_token(client, mocked_books):
    response = client.put(
        "/books/1",
        json={
            "title": "Blocked Update",
            "author": "John Smith",
            "year": 2024,
            "book_type": "physical",
            "extra_info": "A15",
        },
    )

    assert response.status_code == 401


def test_delete_book_success(client, mocked_books):
    response = client.delete("/books/1", headers=get_auth_headers(client))

    assert response.status_code == 200
    assert response.json()["message"] == "Book deleted successfully"


def test_delete_book_failure_not_found(client, mocked_books):
    response = client.delete("/books/999", headers=get_auth_headers(client))

    assert response.status_code == 404
    assert response.json()["detail"] == "Book not found"


def test_delete_book_failure_without_token(client, mocked_books):
    response = client.delete("/books/1")

    assert response.status_code == 401
    
def test_get_books_filter_by_author_exact_match(client, mocked_books):
    response = client.get("/books?author=Jane Doe")

    assert response.status_code == 200
    result = response.json()
    assert len(result) == 1
    assert result[0]["author"] == "Jane Doe"


def test_get_books_filter_by_author_case_insensitive(client, mocked_books):
    response = client.get("/books?author=john smith")

    assert response.status_code == 200
    result = response.json()
    assert len(result) == 1
    assert result[0]["author"] == "John Smith"


def test_get_books_filter_by_author_no_match(client, mocked_books):
    response = client.get("/books?author=Unknown Author")

    assert response.status_code == 200
    result = response.json()
    assert result == []