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
        print('Head', end =" " )
        while p != None :
            print('->'+str(p.val), end =" " )
            # print(p.val)
            p = p.next   
        print()
    
    def reverse(self):
        temp ,prev, current = None , None, self.head
        while current:
            temp = current.next     # temporarily saved next pointer
            current.next = prev     # swap the direction
            prev = current          # making prev = current
            current=temp            # current = next pointer via temp
        self.head = prev


head = [1,2,3,4,5,6]
myList = LinkedList()
myList.addItems(head)
myList.print()
myList.reverse()
myList.print()