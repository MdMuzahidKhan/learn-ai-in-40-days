# Approach: Store basic member information used during borrowing and returning.

class Member:
    def __init__(self, member_id, name):
        self.member_id = member_id
        self.name = name

    def __str__(self):
        return f"Member {self.member_id}: {self.name}"