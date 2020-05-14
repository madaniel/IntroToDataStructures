
# Defines
ROOT_INDEX = 1


class MinHeap(object):

    def __init__(self):
        # First element is dummy
        self._store = [None]

    @property
    def size(self):
        return len(self._store) - ROOT_INDEX

    def add_value(self, node):
        self._store.append(node)
        self._heapify_up(current_index=self.size)

    def peak(self):
        if self.size == 0:
            return None
        else:
            return self._store[ROOT_INDEX].data

    def pop(self):
        if self.size < ROOT_INDEX:
            raise Exception("Heap is empty !")

        min_node = self._store[ROOT_INDEX]

        # If this is the last node in its list
        if min_node.next is None:
            # Switching root with last item
            self._store[ROOT_INDEX] = self._store[-1]
            self._store.pop()  # Removing the last item
        else:
            # Fetching the next item in linked list
            self._store[ROOT_INDEX] = min_node.next

        # Reorder the heap to maintain its property
        self._heapify_down(ROOT_INDEX)

        return min_node

    def _heapify_down(self, current_index):
        while self._has_children(current_index):
            # No need to continue if heap property is satisfied
            if self._is_heap_satisfied(current_index):
                return
            # Get the smallest children and swap it with parent
            smaller_children_index = self._get_smaller_child_index(current_index)
            self._swap(current_index, smaller_children_index)
            # Continue sift down to the smallest child
            current_index = smaller_children_index

    def _heapify_up(self, current_index):
        parent_index = self._get_parent_index(current_index)

        # We check if the current node is un-balanced until the root or until the current node is balanced
        while current_index > ROOT_INDEX and self._get_value(parent_index) > self._store[current_index].data:
            self._swap(index1=current_index, index2=parent_index)
            current_index = self._get_parent_index(current_index)
            parent_index = self._get_parent_index(current_index)
        pass

    def _get_smaller_child_index(self, index):
        left_children_index = self._get_left_child_index(index)
        right_children_index = self._get_right_child_index(index)

        if self._get_value(left_children_index) < self._get_value(right_children_index):
            return left_children_index
        else:
            return right_children_index

    def _get_root(self):
        return self._get_value(ROOT_INDEX)

    def _get_value(self, index):
        if self._has_value(index):
            return self._store[index].data
        else:
            return None

    def _is_heap_satisfied(self, index):
        """
        Checking if parent is smaller from its both children if any exists
        """
        right_child_index = self._get_right_child_index(index)
        right_child_value = self._get_value(right_child_index)

        left_child_index = self._get_left_child_index(index)
        left_child_value = self._get_value(left_child_index)

        current_value = self._get_value(index)
        current_smaller_than_right_child = self._has_right_child(index) and current_value <= right_child_value
        current_smaller_than_left_child = self._has_left_child(index) and current_value <= left_child_value

        no_right_child = not self._has_right_child(index)
        no_left_child = not self._has_left_child(index)

        condition1 = no_right_child or current_smaller_than_right_child
        condition2 = no_left_child or current_smaller_than_left_child

        return condition1 and condition2

    def _has_children(self, index):
        return self._has_left_child(index) and self._has_right_child(index)

    def _has_parent(self, index):
        return self._has_value(self._get_parent_index(index))

    def _has_right_child(self, index):
        return self._has_value(self._get_right_child_index(index))

    def _has_left_child(self, index):
        return self._has_value(self._get_left_child_index(index))

    def _has_value(self, index):
        if ROOT_INDEX <= index <= self.size:
            return True
        else:
            return False

    def _swap(self, index1, index2):
        self._store[index1], self._store[index2] = self._store[index2], self._store[index1]

    @staticmethod
    def _get_parent_index(current_index):
        return current_index // 2

    @staticmethod
    def _get_left_child_index(current_index):
        return 2 * current_index

    @staticmethod
    def _get_right_child_index(current_index):
        return 2 * current_index + 1

    def __repr__(self):
        return str([str(node) for node in self._store if node is not None])

    def __str__(self):
        return str([str(node) for node in self._store if node is not None])
