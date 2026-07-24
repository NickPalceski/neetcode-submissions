class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l, r = 0, 1 # Left -> buy, Right -> sell
        maxP = 0
        while r < len(prices):
            if prices[l] < prices[r]:
                profit = prices[r] - prices[l]
                maxP = max(maxP, profit)
            else:
                # not profitable, set new left
                l = r
            r += 1
        return maxP
