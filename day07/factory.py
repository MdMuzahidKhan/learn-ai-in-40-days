# Approach: Use a factory to decide which type of book data to create based on input.

class BookFactory:
    @staticmethod
    def create_book(book_data):
        book_type = book_data["book_type"].lower()

        def build_payload(normalized_book_type):
            return {
                "title": book_data["title"],
                "author": book_data["author"],
                "year": book_data["year"],
                "book_type": normalized_book_type,
                "extra_info": book_data["extra_info"],
            }

        if book_type == "physical":
            return build_payload("physical")

        if book_type == "ebook":
            return build_payload("ebook")

        raise ValueError(f"Invalid book type: {book_data['book_type']}")