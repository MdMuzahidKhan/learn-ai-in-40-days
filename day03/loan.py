# Approach: A loan connects one member with one book and tracks borrow, due, and return dates.

from datetime import timedelta


class Loan:
    def __init__(self, book, member, borrow_date):
        self.book = book
        self.member = member
        self.borrow_date = borrow_date
        self.due_date = borrow_date + timedelta(days=book.get_loan_period())
        self.return_date = None

    def mark_returned(self, return_date):
        self.return_date = return_date

    def is_overdue(self, current_date):
        return self.return_date is None and current_date > self.due_date

    def __str__(self):
        status = "Returned" if self.return_date else "Active"
        return f"{self.book.title} borrowed by {self.member.name}, Due: {self.due_date}, Status: {status}"