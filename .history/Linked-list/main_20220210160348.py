
#Create the Node as needed.
#The node schold have two objects the value and the ptr
#pointer should be None
from platform import node


class Node():
   def __init__(self, val, next_ptr = None):
       self.val = val
       self.next = next_ptr
#Create the LinkedList with the first node, The head as a none
#the node will be later set to this as we the list is added to.    
class SlinkedList:
   def  __init__(self) -> None:
       self.headval = None 
#list are written with {}
#dict are written with []
#tuples are written with ()
arr = [2,5,3,5,78,34,12,21,65,77,56,4,9,52,]
list1 = SlinkedList()
list1.headval = Node("Mon")
e2 = Node("Tue")
e3 = Node("Wed")
e4 = Node("Thur")

#link the first Node to the second node
list1.headval.next = e2
#link the second node to the thrid
e2.next = e3
e3.next = e4

item_curr = list1.headval
while item_curr is not None:
   print(item_curr.val)
   item_curr = item_curr.next

