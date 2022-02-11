

class LinkedList:
   def __init__(self, val, next_ptr= None):
      self.val = val
      self.next = next_ptr

class Node:
   def __init__(self) -> None:
      self.head = None
      
myhead = Node("32")

MyList = LinkedList(myhead)


curr_node = MyList
while curr_node.val is not None:
   print(curr_node.val)
   curr_node = curr_node.next