class Node:
    def __init__(self, value, next_ptr=None):
        self.val = value
        self.next = next_ptr

class LinkedList:
    def __init__(self) -> None:
        self.head = None

    def traverse(self):
        curr_node = self.head
        while curr_node:
            print(curr_node.val)
            curr_node = curr_node.next

    def mergeKlists(self, lists):
        if not lists or len(lists) == 0:
            return None


MyList = LinkedList()
MyList.head = Node("5")
n2 = Node("7")
n3 = Node("3")
n4 = Node("8")

MyList.head.next = n2
n2.next = n3
n3.next = n4

MyList.traverse()