class Solution:
    def hasValidPath(self, grid: list[list[str]]) -> bool:
        match_sign = {'(':0, ')':1}
        n = len(grid)       #세로
        m = len(grid[0])    #가로
        
        half, remain = divmod(m+n-1,2)
        
        if remain:
            return False

        dp = [[set() for _ in range(m+1)] for i in range(n+1)]
        dp[0][1].add((0,0))
        dp[1][0].add((0,0))
        
        for i in range(1,n+1):
            for j in range(1,m+1):
                for temp in dp[i][j-1]:
                    if match_sign[grid[i-1][j-1]]:
                        if temp[1] == temp[0] or temp[1] == half: continue
                        dp[i][j].add((temp[0], temp[1]+1))
                    else:
                        if temp[0] == half: continue
                        dp[i][j].add((temp[0]+1, temp[1]))
                for temp in dp[i-1][j]:
                    if match_sign[grid[i-1][j-1]]:
                        if temp[1] == temp[0] or temp[1] == half: continue
                        dp[i][j].add((temp[0], temp[1]+1))
                    else:
                        if temp[0] == half: continue
                        dp[i][j].add((temp[0]+1, temp[1]))
                        
        if len(dp[n][m]):
            return True
        return False
                
    def hasValidPath_2(self, grid: list[list[str]]) -> bool:
        n, m = len(grid), len(grid[0])
        
        if (n + m - 1) % 2 != 0:
            return False
            
        if grid[0][0] == ')' or grid[n-1][m-1] == '(':
            return False
            
        dp = [[set() for _ in range(m)] for _ in range(n)]
        dp[0][0].add(1) 
        print(dp)
        for i in range(n):
            for j in range(m):
                if not dp[i][j]:
                    continue
                    
                for bal in dp[i][j]:
                    if j + 1 < m:
                        next_bal = bal + (1 if grid[i][j+1] == '(' else -1)
                        remain_dist = (n - 1 - i) + (m - 1 - (j + 1))
                        
                        if 0 <= next_bal <= remain_dist:
                            dp[i][j+1].add(next_bal)
                            
                    if i + 1 < n:
                        next_bal = bal + (1 if grid[i+1][j] == '(' else -1)
                        remain_dist = (n - 1 - (i + 1)) + (m - 1 - j)
                        
                        if 0 <= next_bal <= remain_dist:
                            dp[i+1][j].add(next_bal)
        if len(dp[n][m]):
            return True
        return False

    def hasValidPath_3(self, grid: list[list[str]]) -> bool:
        n, m = len(grid), len(grid[0])
        
        if (n + m - 1) % 2 != 0:
            return False
        if grid[0][0] == ')' or grid[n-1][m-1] == '(':
            return False

        dp = [0] * m
        
        dp[0] = 0b10 
        
        for i in range(n):
            for j in range(m):
                if i == 0 and j == 0:
                    continue

                prev_state = 0
                if i > 0:
                    prev_state |= dp[j] 
                if j > 0:
                    prev_state |= dp[j-1] 
                    
                if grid[i][j] == '(':
                    dp[j] = prev_state << 1
                else:
                    dp[j] = prev_state >> 1
                    
        return (dp[m-1] & 1) == 1
    
a = Solution()
print(a.hasValidPath([["(","(","("],[")","(",")"],["(","(",")"],["(","(",")"]]))