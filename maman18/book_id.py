

class BookId(object):

    def __init__(self, book_code):
        self.book_code = book_code
        self.loaner_user_id = None

    def __repr__(self):
        return str(self.book_code)

