class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        if len(prices) == 0:
            return 0
        
        minprice, maxprofit = prices[0], 0
        
        for i in range (1,len(prices)):
            minprice = min(minprice, prices[i])
            maxprofit = max(maxprofit, prices[i]-minprice)
            
        return maxprofit