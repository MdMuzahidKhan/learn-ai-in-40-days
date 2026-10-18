# Approach: The Library class manages books, members, and loans and performs the main operations.

from loan import Loan


class Library:
    def __init__(self):
        self.books = []
        self.members = []
        self.loans = []

    def add_book(self, book):
        self.books.append(book)
        print(f"Book added: {book.get_description()}")

    def add_member(self, member):
        self.members.append(member)
        print(f"Member added: {member}")

    def borrow_book(self, book_id, member_id, borrow_date):
        book = self.find_book(book_id)
        member = self.find_member(member_id)

        if book is None:
            print("Book not found.")
            return

        if member is None:
            print("Member not found.")
            return

        if book.is_borrowed:
            print("Book is already borrowed.")
            return

        book.is_borrowed = True
        loan = Loan(book, member, borrow_date)
        self.loans.append(loan)
        print(f"Book borrowed: {book.title} by {member.name}")

    def return_book(self, book_id, return_date):
        for loan in self.loans:
            if loan.book.book_id == book_id and loan.return_date is None:
                loan.mark_returned(return_date)
                loan.book.is_borrowed = False
                print(f"Book returned: {loan.book.title}")
                return

        print("Active loan not found for this book.")

    def list_overdue_loans(self, current_date):
        overdue_loans = [loan for loan in self.loans if loan.is_overdue(current_date)]

        if not overdue_loans:
            print("No overdue loans.")
            return

        print("Overdue loans:")
        for loan in overdue_loans:
            print(loan)

    def find_book(self, book_id):
        for book in self.books:
            if book.book_id == book_id:
                return book
        return None

    def find_member(self, member_id):
        for member in self.members:
            if member.member_id == member_id:
                return member
        return None