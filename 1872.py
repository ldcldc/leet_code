class Solution:
    def stoneGameVIII(self, stones: List[int]) -> int:
        n = len(stones)
        
        dp = [0] * n
        
        prefix_sum = [0] * n
        prefix_sum[0] = stones[0]
        
        for i in range(1,n):
            prefix_sum[i] = prefix_sum[i-1] + stones[i]
        
        dp[n-1] = 0
        dp[n-2] = prefix_sum[n-1]
        
        for i in range(n-3,-1,-1):
            # candidate_dp = [prefix_sum[j] - dp[j] for j in range(i+1,n)]
            # dp[i] = max(candidate_dp)
            
            # prefix_sum[j] - dp[j] for j in range(i+1,n) 와 
            # prefix_sum[i+1] - dp[i+1], dp[i+1]는 같다
            
            dp[i] = max(prefix_sum[i+1] - dp[i+1], dp[i+1])
        
        return dp[0]

a = Solution()
b = a.stoneGameVIII([7,-6,5,10,5,-2,-6])
print(b)