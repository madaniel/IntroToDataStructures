
from enum import Enum
from maman18.user_id import UserId
from maman18.book_id import BookId

# Define
TOP_COUNT = 10
MAX_BOOKS_CREDIT = 10


class DbApi(object):

    def __init__(self):
        self._books_dict = {}
        self._users_dict = {}

    def activate_user(self, user_id: str, user_name: str):
        if self.is_user_activated(user_id):
            return DbError.USER_ALREADY_ACTIVATED

        new_user = UserId(user_name=user_name, user_id=user_id)
        self._users_dict[str(user_id)] = new_user

        return f"User name {new_user.user_name} id {new_user.user_id} added successfully."

    def deactivate_user(self, user_id: str, user_name: str):
        if not self.is_user_activated(user_id):
            return DbError.USER_ALREADY_DEACTIVATED

        user = self.get_user(user_id)

        if user.user_name != user_name:
            return DbError.USER_ID_AND_NAME_DO_NOT_MATCH

        del self._users_dict[str(user_id)]

        return f"User {user_id} deleted successfully."

    def loan_book(self, book_code: str, user_id: str, user_name: str):
        # Verify user activated
        if not self.is_user_activated(user_id):
            return DbError.USER_NOT_ACTIVATED

        user = self.get_user(user_id)

        # User name and User id do not match
        if user.user_name != user_name:
            return DbError.USER_ID_AND_NAME_DO_NOT_MATCH

        # User over exceed his credit and cannot loan more books
        if len(user.book_list) >= MAX_BOOKS_CREDIT:
            return DbError.USER_OVER_EXCEED_HIS_BOOK_CREDIT

        # User already loan this book
        if book_code in user.book_list:
            return DbError.USER_ALREADY_LOANED_THIS_BOOK

        # Book is new, add it to books db
        if not self.is_book_exist(book_code):
            book = BookId(book_code)
            book.loaner_user_id = user.user_id
            self._books_dict[book_code] = book

        # Book exists
        else:
            book = self.get_book(book_code)

        # Assign book to user
        user.book_list.append(book_code)

        return f"Book {book_code} is loaned to user name {user.user_name} id {user.user_id} successfully."

    def return_book(self, book_code: str):
        book = self.get_book(book_code)

        # Verify book is exists
        if book is None:
            return DbError.BOOK_NOT_EXIST

        # Verify book is loaned
        if book.loaner_user_id is None:
            return DbError.BOOK_NOT_ASSIGNED_TO_USER

        user = self.get_user(user_id=book.loaner_user_id)

        book.loaner_user_id = None
        del self._books_dict[book_code]
        user.book_list.remove(book_code)

        return f"Book {book_code} was returned successfully."

    def get_all_books(self) -> dict:
        return self._books_dict

    def get_all_users(self) -> dict:
        return self._users_dict

    def get_top_loaners(self) -> list:
        all_loaners = [self.get_user(user_id) for user_id in self._users_dict]
        loaners_with_books = [user for user in all_loaners if user.books_count > 0]
        loaners_with_books.sort(key=lambda user: user.books_count, reverse=True)
        top_loaners = loaners_with_books[:TOP_COUNT]
        return [f"{loaner.user_name}: {loaner.user_id} books: {loaner.books_count}" for loaner in top_loaners]

    def is_book_exist(self, book_code: str) -> bool:
        return self._books_dict.get(book_code)

    def is_user_activated(self, user_id):
        user = self._users_dict.get(str(user_id))
        return user is not None

    def get_user(self, user_id: str) -> UserId:
        return self._users_dict.get(str(user_id))

    def get_book(self, book_code: str) -> BookId:
        return self._books_dict.get(book_code)

    def __repr__(self):
        return f"users: {self._users_dict},\n books: {self._books_dict}"


class DbOperation(Enum):
    ACTIVATE_USER = 1
    DEACTIVATE_USER = 2
    LOAN_BOOK = 3
    RETURN_BOOK = 4
    QUERY_INVALID_USER_OR_BOOK_ID = 5
    QUERY_BOOKS_FOR_LOANER = 6
    QUERY_LOANER_FOR_BOOK = 7
    QUERY_TOP_BOOKS = 8
    EXIT = 9


class DbError(Enum):
    USER_NOT_ACTIVATED = 1
    USER_NOT_EXISTS = 2
    BOOK_NOT_EXIST = 3
    BOOK_NOT_ASSIGNED_TO_USER = 4
    OPERATION_UNKNOWN = 5
    USER_ALREADY_ACTIVATED = 6
    USER_ALREADY_DEACTIVATED = 7
    USER_ID_AND_NAME_DO_NOT_MATCH = 8
    USER_OVER_EXCEED_HIS_BOOK_CREDIT = 9
    USER_ALREADY_LOANED_THIS_BOOK = 10
    QUERY_INVALID_USER_OR_BOOK_ID = 11


class ParserError(Enum):
    INVALID_USER_ID = 1
    INVALID_BOOK_ID = 2
    INVALID_OPERATION = 3
    INVALID_USER_NAME = 4
