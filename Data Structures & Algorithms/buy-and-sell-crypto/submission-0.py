class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l, r = 0, 1 #Left=buy. Right=sell
        maxP = 0
        while r < len(prices):
            #profitable?
            if prices[l] < prices[r]:
                profit = prices[r] - prices[l]
                maxP = max(maxP, profit)
            else:
                #else, not profitable, set new left to right
                l = r
            r += 1
        return maxP
