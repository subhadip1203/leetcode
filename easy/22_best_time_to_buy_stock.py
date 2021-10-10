'''
https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
'''

from typing import List


class Solution:
  def maxProfit(self, prices: List[int]) -> int :
    min = prices[0]
    profit = 0
    for v in prices :
      if min > v :
        min = v
      else:
        if profit < v-min :
          profit = v-min
    return profit

prices = [7,1,5,3,6,4]
print(Solution().maxProfit(prices))

prices = [7,6,4,3,1]
print(Solution().maxProfit(prices))