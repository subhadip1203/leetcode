'''
link : https://leetcode.com/problems/remove-linked-list-elements/

Given the head of a linked list and an integer val, remove all the nodes of the linked list that has Node.val == val, and return the new head.
'''

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None

    def addItems(self,l):
        current =None
        # prev =None
        for i in l :
            if current == None :
                self.head = ListNode(i)
                current =self.head
            else:               
                n = ListNode(i)
                current.next = n
                current = n

    def print(self):
        p = self.head
        while p != None :
            print(p.val)
            p = p.next   
        print("------------------------")
    def removeElements(self,val):
        current = self.head
        prev =None
        while current :
            if current == self.head and current.val == val :
                current=current.next
                self.head = current
            elif current.val == val:
                prev.next = current.next
                current = current.next
            else:
                prev= current
                current = current.next

head = [6,1,2,6,3,4,5,6]
val = 6
myList = LinkedList()
myList.addItems(head)
myList.print()
myList.removeElements(val)
myList.print()