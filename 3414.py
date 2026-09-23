import bisect

class Solution:
    def maximumWeight(self, intervals: List[List[int]]) -> List[int]:
        intervals = sorted(enumerate(intervals), key=lambda x: x[1][1])
        n = len(intervals)
        
        ends = [interval[1][1] for interval in intervals]
        
        dp = [[(0, []) for _ in range(5)] for _ in range(n + 1)]
        
        for i in range(1, n + 1):
            o_i, (start, end, w) = intervals[i-1]
            p_i = bisect.bisect_left(ends, start, 0, i - 1)
            
            for k in range(5):
                dp[i][k] = dp[i-1][k] 
                
            for k in range(4):
                new_w = dp[p_i][k][0] + w
                
                if dp[i][k+1][0] < new_w:
                    new_list = sorted([*dp[p_i][k][1], o_i])
                    dp[i][k+1] = (new_w, new_list)
                    
                elif dp[i][k+1][0] == new_w:
                    new_list = sorted([*dp[p_i][k][1], o_i])
                    if dp[i][k+1][1] > new_list:
                        dp[i][k+1] = (new_w, new_list)

        return dp[n][4][1]
a = Solution()
print(a.maximumWeight([[1,1,1000000000],[1,1,1000000000],[1,1,1000000000],[1,1,1000000000]]))