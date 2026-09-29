class Solution:
    def stoneGameIII(self, stoneValue: list[int]) -> str:
        n = len(stoneValue)
        dp = [0] * (n + 3)
        stoneValue.extend([0, 0])

        for i in range(n-1, -1, -1):
            dp[i] = max(stoneValue[i] - dp[i+1], 
                        stoneValue[i] + stoneValue[i+1] - dp[i+2], 
                        stoneValue[i] + stoneValue[i+1] + stoneValue[i+2] - dp[i+3])

        
        print(dp)
        if dp[0] < 0:
            return "Bob"
        elif dp[0] == 0:
            return "Tie"
        return "Alice"
    
    def stoneGameIII_2(self, stoneValue: list[int]) -> str:
        n = len(stoneValue)
        
        stoneValue.extend([0, 0])
        
        dp1, dp2, dp3 = 0, 0, 0
        
        for i in range(n-1, -1, -1):
            curr = max(
                stoneValue[i] - dp1, 
                stoneValue[i] + stoneValue[i+1] - dp2, 
                stoneValue[i] + stoneValue[i+1] + stoneValue[i+2] - dp3
            )
            
            dp3 = dp2
            dp2 = dp1
            dp1 = curr
            
        if dp1 > 0:
            return "Alice"
        elif dp1 < 0:
            return "Bob"
        else:
            return "Tie"
            
a = Solution()
print(a.stoneGameIII([1,2,3,-9]))
            