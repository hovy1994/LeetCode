class Solution(object):
    def maxProfit(self, prices):
        curStock = prices[0]
        result =0
        
        for i in range(1, len(prices)):
            if curStock < prices[i]:
                result += prices[i]-curStock
            
            curStock = prices[i]
                
        return result