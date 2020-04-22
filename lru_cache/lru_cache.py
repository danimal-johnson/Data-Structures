import sys
sys.path.append('../doubly_linked_list')
from doubly_linked_list import ListNode, DoublyLinkedList


class LRUCache:
    """
    Our LRUCache class keeps track of the max number of nodes it
    can hold, the current number of nodes it is holding, a doubly-
    linked list that holds the key-value entries in the correct
    order, as well as a storage dict that provides fast access
    to every node stored in the cache.
    """

    def __init__(self, limit=10):
        self.size = 0
        self.storage = DoublyLinkedList()
        self.limit = limit

    """
    Retrieves the value associated with the given key. Also
    needs to move the key-value pair to the end of the order
    such that the pair is considered most-recently used.
    Returns the value associated with the key or None if the
    key-value pair doesn't exist in the cache.
    """

    def get(self, key):
        current_node = self.storage.head
        index = 0
        while index < len(self.storage):  # self.size:
            node_value = current_node.value

            if node_value != None:
                return_value = node_value.get(key)
                if return_value != None:
                    self.storage.move_to_front(current_node)
                    return return_value

            current_node = current_node.next
            index += 1
        return None

    """
    Adds the given key-value pair to the cache. The newly-
    added pair should be considered the most-recently used
    entry in the cache. If the cache is already at max capacity
    before this entry is added, then the oldest entry in the
    cache needs to be removed to make room. Additionally, in the
    case that the key already exists in the cache, we simply
    want to overwrite the old value associated with the key with
    the newly-specified value.
    """

    def set(self, key, value):

        # We will always create a new node for the head
        # (the most-recently-used position)
        new_node = ListNode({key: value})

        # If a node with the value already existed, delete it first.
        current_node = self.storage.head
        index = 0
        while index < len(self.storage):  # self.size:
            node_value = current_node.value
            if node_value != None:
                previous_value = node_value.get(key)
                if previous_value != None:
                    self.storage.delete(current_node)
                    self.size -= 1
            current_node = current_node.next
            index += 1

        # If the cache is too long, delete the tail
        # (the least-recently-used position)
        if self.size == self.limit:
            self.storage.remove_from_tail()
            self.size -= 1

        # Now add the new node to the cache.
        self.storage.add_to_head(new_node.value)
        self.size += 1
