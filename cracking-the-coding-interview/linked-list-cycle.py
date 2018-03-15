"""
Detect a cycle in a linked list. Note that the head pointer may be 'None' if the list is empty.

A Node is defined as:

    class Node(object):
        def __init__(self, data = None, next_node = None):
            self.data = data
            self.next = next_node
"""


def has_cycle(head):
    slow = head
    fast = head

    while fast != None:
        slow = slow.next

        if fast.next != None:
            fast = fast.next.next
        else:
            return False

        if slow is fast:
            return True

    return False