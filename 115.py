class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        dp = [0] * (len(t) + 1)
        dp[0] = 1 
        
        for char in s:
            for j in range(len(t), 0, -1):
                if char == t[j-1]:
                    dp[j] += dp[j-1]
            print(dp)
        return dp[-1]
                    
                    
                    
a = Solution()
print(a.numDistinct(s = "rabbbit", t = "rabbit"))