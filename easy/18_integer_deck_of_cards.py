'''
Link : https://leetcode.com/problems/x-of-a-kind-in-a-deck-of-cards/

In a deck of cards, each card has an integer written on it.
Return true if and only if you can choose X >= 2 such that it is possible to split the entire deck into 1 or more groups of cards, where:
Each group has exactly X cards.
All the cards in each group have the same integer.
'''

class Solution:
    def hasGroupsSizeX(self, deck):        
        d = {}
        for i in deck: 
            d[i]=d.get(i,0)+1
        
        lowest=None
        secondlowest=None
        for x in d:
            if d[x] == 1:
                return False
            else:
                print(d[x])
                print(lowest,secondlowest)
                if lowest ==None and secondlowest == None:
                    lowest = d[x]
                    secondlowest = d[x]
                elif lowest > d[x]:
                    lowest = d[x]
                elif secondlowest > d[x]:
                    secondlowest = d[x]
        print(lowest,secondlowest)

        for x in d:
            if d[x]%lowest != 0:
                return False
        return True

deck = [1]
print(Solution().hasGroupsSizeX(deck))

deck = [1,2,3,4,4,3,2,1]
print(Solution().hasGroupsSizeX(deck))

deck = [1,1,1,2,2,2,3,3]
print(Solution().hasGroupsSizeX(deck))

deck = [1,1]
print(Solution().hasGroupsSizeX(deck))

deck = [0,0,0,1,1,1,2,2,2]
print(Solution().hasGroupsSizeX(deck))

deck =[1,1,1,1,2,2,2,2,2,2]
print(Solution().hasGroupsSizeX(deck))
