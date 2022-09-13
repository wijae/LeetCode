class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        ans = 0
        profit_hold = [0 for _ in range(k+1)]
        profit_sell = [0 for _ in range(k+1)]
        
        for idx in range(len(prices) - 1):
            diff = prices[idx+1] - prices[idx]
            
            next_profit_hold = [0 for _ in range(k+1)]
            next_profit_sell = [0 for _ in range(k+1)]
            
            for j in range(1, k+1):
                next_profit_hold[j] = max(profit_hold[j], profit_sell[j-1]) + diff
                
            for j in range(1, k+1):
                next_profit_sell[j] = max(profit_hold[j], profit_sell[j])
                
            profit_hold = next_profit_hold
            profit_sell = next_profit_sell
                
            ans = max(ans, max(profit_hold), max(profit_sell))
                
        return ans
        
        