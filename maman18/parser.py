
import re
from maman18.db_api import DbOperation


# Defines
USER_NAME_PATTERN = r"\s[a-zA-Z]+\s|[a-zA-Z]+\s|[a-zA-Z]+$"
USER_ID_PATTERN = r"\s\d\d\d\d\d\d\d\d\d\s|\s\d\d\d\d\d\d\d\d\d"
BOOK_CODE_PATTERN = r"[a-zA-Z][a-zA-Z]\d\d\d\d"
NOT_FOUND = "Not Found"


class Parser(object):

    def __init__(self):
        self._user_input = None
        self.user_name = None
        self.user_id = None
        self.book_code = None
        self.operation = None
        self.is_active = True

    @property
    def user_input(self):
        return self._user_input

    @user_input.setter
    def user_input(self, value):
        if value == "0":
            self.is_active = False
        else:
            self._user_input = value

    def analyze_input(self):
        if not self.is_active:
            return
        # Extract data from user input
        self.set_book_code()
        self.set_user_id()
        self.set_user_name()
        self.set_operation()

    def set_user_name(self):
        found = re.search(USER_NAME_PATTERN, self.user_input)
        self.user_name = found.group().split()[0] if found else NOT_FOUND

    def set_user_id(self):
        found = re.search(USER_ID_PATTERN, self.user_input)
        self.user_id = found.group().split()[0] if found else NOT_FOUND

    def set_book_code(self):
        found = re.search(BOOK_CODE_PATTERN, self.user_input)
        self.book_code = found.group().split()[0] if found else NOT_FOUND

    def set_operation(self):
        self.operation = NOT_FOUND
        self.operation = DbOperation.LOAN_BOOK if "+" in self.user_input and self.book_code != NOT_FOUND else self.operation
        self.operation = DbOperation.RETURN_BOOK if "-" in self.user_input and self.book_code != NOT_FOUND else self.operation
        self.operation = DbOperation.ACTIVATE_USER if "+" in self.user_input and self.book_code == NOT_FOUND else self.operation
        self.operation = DbOperation.DEACTIVATE_USER if "-" in self.user_input and self.book_code == NOT_FOUND else self.operation
        self.operation = DbOperation.QUERY_INVALID_USER_OR_BOOK_ID if "?" in self.user_input else self.operation
        self.operation = DbOperation.QUERY_BOOKS_FOR_LOANER if "?" in self.user_input and self.user_id != NOT_FOUND else self.operation
        self.operation = DbOperation.QUERY_LOANER_FOR_BOOK if "?" in self.user_input and self.book_code != NOT_FOUND else self.operation
        self.operation = DbOperation.QUERY_TOP_BOOKS if "?!" in self.user_input else self.operation

    def reset_variables(self):
        self.book_code = self.user_id = self.user_input = self.user_name = self.operation = None

    def __repr__(self):
        user_name_print = f"Username: {self.user_name}\n" if self.user_name != NOT_FOUND else ""
        user_id_print = f"UserId: {self.user_id}\n" if self.user_id != NOT_FOUND else ""
        book_code_print = f"BookCode: {self.book_code}\n" if self.book_code != NOT_FOUND else ""
        operation_print = f"Operation: {self.operation}\n" if self.operation else ""

        return user_name_print + user_id_print + book_code_print + operation_print
