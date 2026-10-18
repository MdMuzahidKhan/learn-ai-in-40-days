# After refactor: clearer naming, removed duplication, and improved extensibility.

PHYSICAL_BOOK = "physical"
EBOOK = "ebook"

SUPPORTED_BOOK_TYPES = {PHYSICAL_BOOK, EBOOK}


class BookFactory:
    @staticmethod
    def create_book(book_input):
        normalized_book_type = BookFactory._normalize_book_type(book_input["book_type"])
        return BookFactory._build_book_data(book_input, normalized_book_type)

    @staticmethod
    def _normalize_book_type(book_type_value):
        normalized_book_type = book_type_value.lower()

        if normalized_book_type not in SUPPORTED_BOOK_TYPES:
            raise ValueError("Invalid book type")

        return normalized_book_type

    @staticmethod
    def _build_book_data(book_input, normalized_book_type):
        return {
            "title": book_input["title"],
            "author": book_input["author"],
            "year": book_input["year"],
            "book_type": normalized_book_type,
            "extra_info": book_input["extra_info"],
        }