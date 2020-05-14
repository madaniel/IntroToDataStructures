

class UserId(object):

    def __init__(self, user_name, user_id):
        self.user_name = user_name
        self.user_id = user_id
        self.book_list = []
        self.is_active = True

    @property
    def books_count(self):
        return len(self.book_list)

    def __repr__(self):
        return f"User Name: {self.user_name}, User ID: {self.user_id}, Books Loaned: {self.book_list}, User Active: {self.is_active}"
