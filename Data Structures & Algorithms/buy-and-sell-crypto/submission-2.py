class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left, right = 0, 1
        maxprofit = 0
        while right < len(prices):
            profit = prices[right] - prices[left]
            print(left, " ", right)
            if profit < 0:
                left = right
            if profit > maxprofit:
                maxprofit = profit
            right += 1
            
        return maxprofit