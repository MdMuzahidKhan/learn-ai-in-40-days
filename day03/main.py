# Approach: Create books and members, then demo add, borrow, return, and overdue operations end to end.

from datetime import date, timedelta
from book import PhysicalBook, EBook
from member import Member
from library import Library


library = Library()

book1 = PhysicalBook(1, "Python Basics", "John Smith", "A12")
book2 = EBook(2, "OOP in Python", "Jane Doe", "PDF")

member1 = Member(101, "Alice")
member2 = Member(102, "Bob")

library.add_book(book1)
library.add_book(book2)

library.add_member(member1)
library.add_member(member2)

print("\nPolymorphic method call:")
for book in library.books:
    print(book.get_description())
    print("Loan period:", book.get_loan_period(), "days")

print("\nBorrowing books:")
borrow_day = date.today() - timedelta(days=20)
library.borrow_book(1, 101, borrow_day)
library.borrow_book(2, 102, date.today())

print("\nListing overdue loans:")
library.list_overdue_loans(date.today())

print("\nReturning a book:")
library.return_book(1, date.today())

print("\nListing overdue loans after return:")
library.list_overdue_loans(date.today())