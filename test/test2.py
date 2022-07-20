'''
Design a booking system for a conference room. The system will have a book function that will be called multiple times with a time interval. If the room is available, the system will return true and will store that time interval. If it's not available, it will just return false.
The room can only be booked if the time interval does not overlap with any other booked time intervals.
Example:
* book(10, 20) —> true
* book(20, 30) —> true
* book(5, 15) —> false
The 3rd time interval overlaps with the first one, so that's why it returns false.

'''

class Node:
  def __init__(self,data=None):
    self.data=data
    self.next=None

class LinkedList:
  def __init__(self):
    self.head = None

  def append(self,data):
    new_node = Node(data)
    if self.head ==None:
      self.head=new_node
    