'''
https://leetcode.com/problems/merge-k-sorted-lists/
'''
class Node():
  def __init__(self,data):
    self.data = data

class LinkedList():
  def __init__(self,arr):
    self.head = Node(arr[0])
    current = self.head
    for x in arr:
      current.next = Node(x)
      current =current.next

def Solution(lst):
  linkedlist_arr = []
  for l in lst:
    linkedlist_arr.append(LinkedList(l))





lists = [[1,4,5],[1,3,4],[2,6]]