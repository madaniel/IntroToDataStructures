
from maman14.parser import Parser


def main():
    parser = Parser()

    # Generating random input of list of number, based on the defined number in Parser (for testing purpose)
    # user_data_list = parser.user_data_generator()

    # Getting the numbers from the user
    user_data_list = parser.read_user_data()

    # Copying the numbers to linked list
    list_of_linked_list = parser.copy_to_linked_list(user_data_list)

    min_heap = parser.copy_to_heap(list_of_linked_list)
    parser.print_heap(min_heap)


if __name__ == '__main__':
    main()
