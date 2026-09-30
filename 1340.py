class Solution:
    def maxJumps(self, arr: list[int], d: int) -> int:
        n = len(arr)
        dp = [0] * n
        
        def dfs(i):
            if dp[i]:
                return dp[i]
            
            max_n = 1
            
            for j in range(i - 1, max(-1, i - d - 1), -1):
                if arr[j] >= arr[i]: break
                max_n = max(max_n, dfs(j) + 1)
                
            for j in range(i + 1, min(n, i + d + 1)):
                if arr[j] >= arr[i]: break
                max_n = max(max_n, dfs(j) + 1)
                
            dp[i] = max_n
            return max_n
            
        return max(dfs(i) for i in range(n))

    def maxJumps_2(self, arr: list[int], d: int) -> int:
        n = len(arr)
        dp = [1] * n
        res = 0
        sorted_index = sorted(range(n), key=lambda i: arr[i])
        
        for i in sorted_index:
            for j in range(i - 1, max(-1, i - d - 1), -1):
                if arr[j] >= arr[i]: break
                dp[i] = max(dp[i], dp[j] + 1)
                
            for j in range(i + 1, min(n, i + d + 1)):
                if arr[j] >= arr[i]: break
                dp[i] = max(dp[i], dp[j] + 1)
            res = max(res, dp[i])
        return max(dp)
a = Solution()
print(a.maxJumps(arr = [6,4,14,6,8,13,9,7,10,6,12], d = 2))