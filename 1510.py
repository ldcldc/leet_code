class Solution:
    def winnerSquareGame(self, n: int) -> bool:
        dp = dict()
        
        curr = 1
        curr_sqrt = 1
        while curr_sqrt <= n:
            dp[curr_sqrt] = True
            curr_sqrt += (curr << 1) + 1
            curr += 1
            
        def dfs(remain: int) -> bool:
            if remain == 0:
                return False
                
            if remain in dp:
                return dp[remain]
                
            i = 1
            i_sqrt = 1
            while i_sqrt <= remain:
                if not dfs(remain - i_sqrt):
                    dp[remain] = True
                    return True
                
                i_sqrt += (i << 1) + 1
                i += 1
                
            dp[remain] = False
            return False
            
        return dfs(n)

    def winnerSquareGame_2(self, n: int) -> bool:
        squares = []
        k = 1
        while k * k <= n:
            squares.append(k * k)
            k += 1
            
        # c는 이게 더 빠른데 파이썬은 아닐 수 있음 연산 수가 중요  
        # k = 1
        # k_sqrt = 1
        # while k_sqrt <= n:
        #     squares.append(k_sqrt)
        #     k_sqrt += (k<<1) + 1
            
        dp = [False] * (n + 1)
        
        for i in range(1, n + 1):
            for sq in squares:
                if i < sq:
                    break
                    
                if not dp[i - sq]:
                    dp[i] = True
                    break
                    
        return dp[n]
                
        
a = Solution()
print(a.winnerSquareGame(24))