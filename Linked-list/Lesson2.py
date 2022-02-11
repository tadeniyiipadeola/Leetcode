

class Node:
   def __init__(self, val, next_ptr= None):
      self.val = val
      self.next = next_ptr

class LinkedList:
   def __init__(self) -> None:
      self.head = None
   
   def front_insert(self, input):
      temp_node = Node(input)
      temp_node.val = self.head
      self.head = temp_node
      
   def printlist(self, head):
      curr_node = head
      while curr_node is not None:
         print(curr_node.val)
         curr_node = curr_node.next

MyList = LinkedList()
MyList.head = Node("32")
value = input()
MyList.front_insert(value)
MyList.printlist(MyList.head)