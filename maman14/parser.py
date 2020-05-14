
import random

from maman14.linked_list import List
from maman14.min_heap import MinHeap

# Defines
K_NUMBER_OF_SERIALS = 5
MAX_LENGTH = 10
MAX_NUMBER = 100


class Parser(object):

    @staticmethod
    def print_heap(min_heap):
        print("\nPrinting from Min Heap:")

        while min_heap.peak() is not None:
            print(min_heap.pop(), end=" ")

        print()

    @staticmethod
    def copy_to_heap(list_of_linked_list):
        min_heap = MinHeap()

        for linked_list in list_of_linked_list:
            min_heap.add_value(linked_list.head)

        return min_heap

    @staticmethod
    def copy_to_linked_list(user_data_list):
        """
        Copy numbers from lists of user input
        :param user_data_list: list of numbers
        :return list of linked list
        """
        list_of_linked_list = []

        for user_list in user_data_list:
            linked_list = List()
            linked_list.add_list(user_list)
            # Append takes O(1) since it's add the item to the end of the list (see reference in word file)
            list_of_linked_list.append(linked_list)

        return list_of_linked_list

    @staticmethod
    def read_user_data():
        """
        Getting numbers from user
        :return: list of itn list
        """
        list_of_int_list = []
        print("\nEnter numbers for {} serials. After you completed each serial, press Enter:".format(K_NUMBER_OF_SERIALS))

        for serial in range(K_NUMBER_OF_SERIALS):
            raw_input = input()
            string_list = raw_input.split()
            # Casting to int per list:
            # map function takes function and iterator and loop through iterator and applies function for each item
            # Complexity of O(n)
            int_list = list(map(int, string_list))
            # Append takes O(1) since it's add the item to the end of the list (see reference in word file)
            list_of_int_list.append(int_list)

        return list_of_int_list

    @staticmethod
    def user_data_generator():
        """
        Randomize numbers and list length for testing (not required for the Maman)
        :return: list of int lists
        """
        list_of_int_list = []
        print("\n Generating {} random int lists...".format(K_NUMBER_OF_SERIALS))

        for serial in range(K_NUMBER_OF_SERIALS):
            random_length = random.randint(3, MAX_LENGTH)
            # Sample takes list of items and pick randomly n times an item
            random_list = random.sample(range(MAX_NUMBER), random_length)
            # Sorting for testing purpose to make the list in increasing order
            random_list.sort()
            # Append takes O(1) since it's add the item to the end of the list (see reference in word file)
            list_of_int_list.append(random_list)
            print(random_list, end=" ")
        print()

        return list_of_int_list
