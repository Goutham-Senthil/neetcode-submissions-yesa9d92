class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l , r = 0 , 1
        min_ = float('inf')
        max_ = 0
        n = len(prices)
        while r < n:
            if prices[r] > prices[l]:
                max_ = max(max_,prices[r]-prices[l])
            else:
                l = r
            r+=1
        return max_