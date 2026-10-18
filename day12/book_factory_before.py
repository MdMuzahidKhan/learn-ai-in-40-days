# Before refactor: duplicated logic, hardcoded values, and weak extensibility.

class BookFactory:
    @staticmethod
    def create_book(book_data):
        book_type = book_data["book_type"].lower()

        if book_type == "physical":
            return {
                "title": book_data["title"],
                "author": book_data["author"],
                "year": book_data["year"],
                "book_type": "physical",
                "extra_info": book_data["extra_info"],
            }

        if book_type == "ebook":
            return {
                "title": book_data["title"],
                "author": book_data["author"],
                "year": book_data["year"],
                "book_type": "ebook",
                "extra_info": book_data["extra_info"],
            }

        raise ValueError("Invalid book type")