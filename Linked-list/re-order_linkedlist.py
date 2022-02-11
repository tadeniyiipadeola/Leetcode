#created a Nodeclass that handles the values and the pointer
class Node:
    def __init__(self, Val, next_ptr =None) -> None:
        self.val = Val
        self.next = next_ptr

#created a list with a None
class List:
    def __init__(self):
        self.head = None
    def traverse(self):
        curr_node = self.head
        while curr_node:
            print(curr_node.val)
            curr_node = curr_node.next
    def reorderlist(self):
        #find the middle 
        slow, fast = self.head, self.head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next 

        #reverse the second list
        second = slow.next
        prev = slow.next = None
        while second:
            temp= second.next
            second.next = prev
            prev = second
            second =temp

        #merge two halfs 
        first, second = self.head, prev
        while second:
            temp1, temp2 = first.next, second.next
            first.next = second
            second.next = temp1
            first, second = temp1, temp2



LinkedList = List()
LinkedList.head = Node("1")
n2 = Node('2')
n3 = Node('3')
n4 = Node('4')
n5 = Node('5')

LinkedList.head.next = n2
n2.next = n3
n3.next = n4
n4.next = n5

LinkedList.traverse()
LinkedList.reorderlist()
LinkedList.traverse()