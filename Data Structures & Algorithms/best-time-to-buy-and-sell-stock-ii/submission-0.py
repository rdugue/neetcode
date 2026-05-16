class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        profit = 0
        i = 0
        p = prices[i]
        j = i + 1
        while j < n:
            next = prices[j]
            if next < prices[i]:
                profit += prices[i] - p
                p = next 
            i = j
            j += 1
        if prices[i] > p:
            profit += prices[i] - p
        return profit