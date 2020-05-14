
from maman18.db_api import DbApi, DbOperation, DbError, ParserError
from maman18.parser import Parser, NOT_FOUND


class Menu(object):

    def __init__(self, parser: Parser, db_api: DbApi):
        self.parser = parser
        self.db_api = db_api

    @staticmethod
    def get_user_input():
        return input("\nPlease enter query or new input, enter 0 to exit:\n")

    def do_operation(self):
        """
        self.user_name = None
        self.user_id = None
        self.book_code = None
        self.operation = None
        """
        if not self.parser.is_active:
            return "Exit..."

        operation_dict = {DbOperation.ACTIVATE_USER:                        self.activate_user,
                          DbOperation.DEACTIVATE_USER:                      self.deactivate_user,
                          DbOperation.LOAN_BOOK:                            self.loan_book,
                          DbOperation.RETURN_BOOK:                          self.return_book,
                          DbOperation.QUERY_BOOKS_FOR_LOANER:               self.query_books_for_loaner,
                          DbOperation.QUERY_LOANER_FOR_BOOK:                self.query_loaner_for_book,
                          DbOperation.QUERY_TOP_BOOKS:                      self.query_top_books,
                          DbOperation.QUERY_INVALID_USER_OR_BOOK_ID:        self.query_unknown}

        if self.parser.operation not in operation_dict:
            return DbError.OPERATION_UNKNOWN

        return operation_dict[self.parser.operation]()

    def loan_book(self):
        if self.parser.book_code == NOT_FOUND:
            return ParserError.INVALID_BOOK_ID
        if self.parser.user_id == NOT_FOUND:
            return ParserError.INVALID_USER_ID
        if self.parser.user_name == NOT_FOUND:
            return ParserError.INVALID_USER_NAME

        # User input is OK
        return self.db_api.loan_book(book_code=self.parser.book_code, user_id=self.parser.user_id, user_name=self.parser.user_name)

    def return_book(self):
        if self.parser.book_code == NOT_FOUND:
            return ParserError.INVALID_BOOK_ID

        # User input is OK
        return self.db_api.return_book(book_code=self.parser.book_code)

    def activate_user(self):
        if self.parser.user_id == NOT_FOUND:
            return ParserError.INVALID_USER_ID
        if self.parser.user_name == NOT_FOUND:
            return ParserError.INVALID_USER_NAME

        # User input is OK
        return self.db_api.activate_user(user_id=self.parser.user_id, user_name=self.parser.user_name)

    def deactivate_user(self):
        if self.parser.user_id == NOT_FOUND:
            return ParserError.INVALID_USER_ID
        if self.parser.user_name == NOT_FOUND:
            return ParserError.INVALID_USER_NAME

        # User input is OK
        return self.db_api.deactivate_user(user_id=self.parser.user_id, user_name=self.parser.user_name)

    def query_books_for_loaner(self):
        if self.parser.user_id == NOT_FOUND:
            return ParserError.INVALID_USER_ID
        # User input is OK
        user = self.db_api.get_user(user_id=self.parser.user_id)

        if user is None:
            return DbError.USER_NOT_EXISTS

        return f"User {self.parser.user_id} loaned books: {user.book_list}"

    def query_loaner_for_book(self):
        if self.parser.book_code == NOT_FOUND:
            return ParserError.INVALID_BOOK_ID

        # Looking for book in db
        book = self.db_api.get_book(book_code=self.parser.book_code)

        if book is None:
            return DbError.BOOK_NOT_EXIST

        return f"User {book.loaner_user_id} is a loaner for {self.parser.book_code}"

    def query_top_books(self):
        return f"The top loaners with most books assigned are {self.db_api.get_top_loaners()}"

    @staticmethod
    def query_unknown():
        return DbError.QUERY_INVALID_USER_OR_BOOK_ID
