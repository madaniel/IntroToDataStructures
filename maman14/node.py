

class Node(object):

    def __init__(self, data):
        assert isinstance(data, int), "Node data should be int instead of {}".format(type(data))
        self.data = data
        self.next = None

    def __str__(self):
        # To add readability - not essential
        return str(self.data)

    def __repr__(self):
        # For debugging purpose - represent the linked list
        return self.data
