class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        '''Solving using 2 pointers aka sliding window'''
        l, r = 0, 1
        best_profit = 0
        
        while r < len(prices):
            if prices[l] < prices[r]:
                current_profit = prices[r] - prices[l]
                best_profit = max(current_profit, best_profit)
            else:
                l = r
            r += 1
        
        return best_profit 