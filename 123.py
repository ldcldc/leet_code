class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        
        max_past = [0] * n
        max_future = [0] * n
        
        min_price = prices[0]
        max_price = prices[n-1]
        
        for i in range(1,n):
            min_price = min(min_price, prices[i])
            max_price = max(max_price, prices[n-i-1])
            
            max_past[i] = max(max_past[i-1], prices[i] - min_price)
            max_future[n-i-1] = max(max_future[n-i], max_price - prices[n-i-1])

        return max(max_past[i] + max_future[i] for i in range(n))

    def maxProfit_2(self, prices: List[int]) -> int:
        buy1 = buy2 = -float('inf') 
        sell1 = sell2 = 0
        
        for price in prices:

            buy1 = max(buy1, -price)
            sell1 = max(sell1, buy1 + price)
            
            buy2 = max(buy2, sell1 - price)
            sell2 = max(sell2, buy2 + price)
            
        return sell2

a = Solution()
print(a.maxProfit([3,3,5,0,0,3,1,4]))
        