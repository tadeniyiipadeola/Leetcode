

class Node:
   def __init__(self, val, next_ptr= None):
      self.val = val
      self.next = next_ptr

class LinkedList:
   def __init__(self) -> None:
      self.head = None
   
   def front_insert(self):
      temp_node = Node(input)
      temp_node.val = self.head
      self.head = temp_node(input)
      
      
   
   
      


MyList = LinkedList()
MyList.head = Node("32")
curr_node = MyList
while curr_node.val is not None:
   print(curr_node.val)
   curr_node = curr_node.next