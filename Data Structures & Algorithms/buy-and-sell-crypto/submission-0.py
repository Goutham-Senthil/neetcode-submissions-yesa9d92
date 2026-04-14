class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_index = 0
        min_ = float('inf')
        max_ = 0
        n = len(prices)
        for i in range(n):
            if prices[i] < min_:
                min_ = prices[i]
                min_index = i
            
            if prices[i] - prices[min_index] > max_:
                max_ = prices[i] - prices[min_index]

        # max_ = 0

        # for i in range(min_index,n):
        #     if prices[i] - 
            

        return max_